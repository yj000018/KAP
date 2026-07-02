#!/usr/bin/env python3
"""Web Citation Policy Validator — CONN-WEB-01. Validates URLs against citation policy rules."""
FORBIDDEN_DOMAINS = ["sci-hub.se","libgen.is","piratebay.org"]
ALLOWED_CONTENT_TYPES = ["text/html","application/json","text/plain","application/pdf"]

def validate_url(url: str) -> dict:
    from urllib.parse import urlparse
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    issues = []
    if any(f in domain for f in FORBIDDEN_DOMAINS): issues.append("FORBIDDEN_DOMAIN")
    if not url.startswith("https://"): issues.append("NOT_HTTPS")
    return {"url": url, "valid": len(issues) == 0, "issues": issues}

if __name__ == "__main__":
    import sys, json
    urls = sys.argv[1:] or ["https://manus.im","http://example.com"]
    results = [validate_url(u) for u in urls]
    print(json.dumps(results, indent=2))
