"""
OpenRouter — Kimi K2.6 Configuration Snippet
=============================================
Provider   : OpenRouter (open-weight routing)
Model      : moonshotai/kimi-k2-6
Rationale  : Open-weight model — host competition on OpenRouter yields
             30-50% cost savings vs direct Moonshot API at high volume.
Updated    : 2026-06-25
Owner      : Yannick (Y-OS)

SECURITY: API key is read from environment variable OPENROUTER_API_KEY.
          Never hardcode the key in source code or documentation.
"""

import os
import requests
from typing import Optional

# ─────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
KIMI_K2_MODEL       = "moonshotai/kimi-k2-6"
DEFAULT_MAX_TOKENS  = 262144
DEFAULT_TEMPERATURE = 0.7

# Cost tracking tags (for logging / billing attribution)
COST_TAGS = {
    "provider":          "openrouter",
    "model":             "kimi-k2-6",
    "optimisation_rule": "open_weight_cheaper",
}

# Fallback: if OpenRouter fails, retry against Moonshot direct API
FALLBACK_POLICY = "retry_direct_moonshot"
MOONSHOT_BASE_URL = "https://api.moonshot.cn/v1"


def _get_api_key() -> str:
    """Retrieve OpenRouter API key from environment. Never hardcode."""
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise EnvironmentError(
            "OPENROUTER_API_KEY is not set. "
            "Add it to Manus Secrets or your environment before calling this function."
        )
    return key


def call_kimi_k2(
    prompt: str,
    system_prompt: Optional[str] = None,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    temperature: float = DEFAULT_TEMPERATURE,
    enable_fallback: bool = True,
) -> dict:
    """
    Call Kimi K2.6 via OpenRouter.

    Args:
        prompt:         User message / query.
        system_prompt:  Optional system instruction.
        max_tokens:     Max output tokens (default: 262144).
        temperature:    Sampling temperature (default: 0.7).
        enable_fallback: If True, retry against Moonshot direct API on failure.

    Returns:
        dict with keys: content, model, provider, usage, cost_tags
    """
    api_key = _get_api_key()

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        # OpenRouter best-practice headers for attribution / rate-limit tiers
        "HTTP-Referer": "https://manus.im",
        "X-Title": "Y-OS LLM Router",
    }

    payload = {
        "model":       KIMI_K2_MODEL,
        "messages":    messages,
        "max_tokens":  max_tokens,
        "temperature": temperature,
    }

    try:
        response = requests.post(
            f"{OPENROUTER_BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            timeout=120,
        )
        response.raise_for_status()
        data = response.json()
        return {
            "content":   data["choices"][0]["message"]["content"],
            "model":     data.get("model", KIMI_K2_MODEL),
            "provider":  "openrouter",
            "usage":     data.get("usage", {}),
            "cost_tags": COST_TAGS,
        }

    except requests.RequestException as exc:
        if enable_fallback:
            return _fallback_moonshot_direct(prompt, system_prompt, max_tokens, temperature)
        raise RuntimeError(f"OpenRouter call failed and fallback disabled: {exc}") from exc


def _fallback_moonshot_direct(
    prompt: str,
    system_prompt: Optional[str],
    max_tokens: int,
    temperature: float,
) -> dict:
    """
    Fallback: call Moonshot direct API when OpenRouter is unavailable.
    Requires MOONSHOT_API_KEY environment variable.
    """
    moonshot_key = os.environ.get("MOONSHOT_API_KEY")
    if not moonshot_key:
        raise EnvironmentError(
            "OpenRouter failed and MOONSHOT_API_KEY is not set for fallback. "
            "Set MOONSHOT_API_KEY in Manus Secrets."
        )

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    headers = {
        "Authorization": f"Bearer {moonshot_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model":       "moonshot-v1-128k",  # Moonshot direct model slug
        "messages":    messages,
        "max_tokens":  max_tokens,
        "temperature": temperature,
    }

    response = requests.post(
        f"{MOONSHOT_BASE_URL}/chat/completions",
        headers=headers,
        json=payload,
        timeout=120,
    )
    response.raise_for_status()
    data = response.json()
    return {
        "content":   data["choices"][0]["message"]["content"],
        "model":     data.get("model", "moonshot-v1-128k"),
        "provider":  "moonshot_direct_fallback",
        "usage":     data.get("usage", {}),
        "cost_tags": {**COST_TAGS, "provider": "moonshot_direct", "fallback": True},
    }


# ─────────────────────────────────────────
# Quick CLI test
# ─────────────────────────────────────────
if __name__ == "__main__":
    import json, sys

    query = sys.argv[1] if len(sys.argv) > 1 else "Explain the Y-OS LLM routing strategy in 3 sentences."
    result = call_kimi_k2(query)
    print(json.dumps(result, indent=2, ensure_ascii=False))
