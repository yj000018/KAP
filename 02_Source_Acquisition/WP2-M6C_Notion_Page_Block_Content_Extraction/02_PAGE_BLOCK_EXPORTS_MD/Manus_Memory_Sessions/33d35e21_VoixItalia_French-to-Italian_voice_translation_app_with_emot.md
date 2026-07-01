---
source_id: KAP-WP2-M6C-Manus_Memory_Sessions-33d35e21
notion_page_id: 33d35e21-8cf8-810b-8584-dd88b6a3f85e
notion_database_id: 5e51ded4-0b46-4a68-acc2-4e90886a2499
title: "VoixItalia: French-to-Italian voice translation app with emotional fidelity"
database_name: Manus_Memory_Sessions
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# VoixItalia: French-to-Italian voice translation app with emotional fidelity

**Page ID:** `33d35e21-8cf8-810b-8584-dd88b6a3f85e`  
**Database:** Manus_Memory_Sessions  
**Created:** 2026-04-09  
**Last Edited:** 2026-04-09  

## Properties

- **Length:** long
- **Language:** mixed
- **Subthemes:** ElevenLabs API, speech synthesis, mobile UI/UX, iOS native sharing, SSML audio tags
- **Project:** UNKNOWN
- **UID:** 6V4cCKQoKVTkkApzrqHqi4
- **Date:** 2026-03-10
- **Themes:** AI voice translation, mobile web development, emotional fidelity, TTS/STS integration
- **Archived:** True
- **Depth:** substantial
- **Title:** VoixItalia: French-to-Italian voice translation app with emotional fidelity

## Content


## Executive Summary

Built VoixItalia, a complete French-to-Italian voice translation web app with emotional fidelity preservation. Overcame multiple TTS integration challenges (Forge API limitations, OpenAI access issues, Web Speech API iOS bugs) to ultimately implement ElevenLabs eleven_v3 with SSML audio tags. Final architecture: browser audio recording → S3 → Whisper transcription → LLM translation with emotion detection → ElevenLabs TTS with audio tags → emotional Italian speech synthesis. Mobile-first single-screen design optimized for iPhone 14 Pro Max with native iOS sharing integration.


## Context & Intent

User requested a mobile webapp for real-time French-to-Italian voice translation with preservation of emotions, intonations, pauses, and vocal emphasis. Key requirement was maintaining the emotional fidelity of the original speech in the translated output.


## What Was Done

Built complete pipeline from scratch: mobile-responsive UI with recording interface, S3 audio storage, Whisper transcription, LLM-powered translation with emotion analysis, multiple TTS provider integrations, native iOS sharing, and public shareable links. Iterated through Web Speech API, OpenAI TTS, ElevenLabs STS, and finally ElevenLabs TTS with SSML tags.


## Outputs Produced

- [web application] VoixItalia — Complete mobile web app with 4 screens: Home, Recorder, Result, History
- [backend pipeline] Translation API — Node.js/Express server with S3, Whisper, LLM, and ElevenLabs integrations
- [database schema] Translations DB — SQLite schema with audio storage, transcriptions, and emotion metadata
- [test suite] Vitest tests — 11 passing tests covering API endpoints and core functionality

## Key Decisions & Validations

- Switched from server-side TTS to ElevenLabs API for emotional fidelity
- Chose eleven_v3 model over turbo_v2_5 for SSML audio tags interpretation
- Implemented dual text storage: clean display text vs tagged synthesis text
- Selected Gus (Italian native voice) over Aria (English voice) for natural pronunciation
- Used single-screen mobile layout optimized for iPhone 14 Pro Max dimensions

## Lessons Learned

Worked well:

- ElevenLabs eleven_v3 with SSML audio tags for emotional speech synthesis
- LLM-based emotion detection and SSML tag injection
- Native iOS Web Share API for seamless file sharing
- S3 integration for reliable audio storage and public sharing
Failed / suboptimal:

- Web Speech API unreliable on iOS Safari for programmatic synthesis
- ElevenLabs STS reproduces source language instead of translating
- eleven_turbo_v2_5 reads SSML tags literally instead of interpreting them
- Forge API lacks TTS endpoints, OpenAI keys not available in server environment
Discoveries:

- iOS Safari requires user gesture for reliable SpeechSynthesis events
- ElevenLabs STS preserves voice characteristics but not target language
- SSML audio tags only work with eleven_v3 model, not turbo variants
- Mobile translation apps need careful UX for single-screen workflows

## Challenges & Blockers

- Multiple TTS provider failures (Forge API limitations, OpenAI access, Web Speech iOS bugs)
- ElevenLabs payment issue temporarily blocking STS testing
- Complex emotion-to-SSML mapping requiring extensive prompt engineering
- iOS Safari audio synthesis reliability issues requiring architecture changes

## Open Questions

- Should voice selection be exposed to users or kept with current Gus default?
- How to handle longer recordings beyond ElevenLabs character limits?
- Whether to add debug mode showing SSML tags for transparency
- Potential integration with other Italian voice models for comparison

## Next Steps

- Add voice selector (Gus/Luca Brasi/Sami) on Recorder screen
- Implement 60-second recording limit with circular progress indicator
- Add debug toggle to show SSML-tagged text alongside clean translation
- Enhance public share page with both audio players and transcriptions
---
UID: 6V4cCKQoKVTkkApzrqHqi4 | Model: claude-sonnet-4-20250514 | Cost: $0.0476
