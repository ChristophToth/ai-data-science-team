# Chief of Staff briefing — CMO Insightful AI Access

**To:** Human owner  
**From:** Chief of Staff Grok  
**Date:** 2026-09-16  
**Meeting purpose:** Get a CMO yes on sanctioned access to **live Insightful** — without treating Ask AT&T as the near-term demand fix.

---

## Bottom line

The recommendation is locked, packaged, and merged. You can take it to the CMO.

**Ask:** Approve **MCP or API access by use case** to live Insightful (Stravito, AT&T-branded). Agents / agent platforms → MCP. Custom apps / backends → API. One pipe does not cover all use cases.

**Do not ask:** To wait on the Ask AT&T / Ask Docs knowledge domain. That is a **separate goal**. The secured copy is already uploaded; the work is now golden questions, stewards, and a quality gate — not a substitute for live access.

If the room drifts into “can’t we just use Ask AT&T,” pull back to: *upload ≠ production confidence; domain Q&A does not replace Stravito’s UX, collections, or research-tuned assistant.*

---

## Status

| Item | State |
| --- | --- |
| Framing | Locked. Live only in Insightful today. Near-term = MCP/API by use case. Domain = separate. |
| Package | Ready. 12-slide browser deck + speaker notes + 17-slide PPTX + build script. |
| PR | **Merged.** [PR #2](https://github.com/ChristophToth/ai-data-science-team/pull/2) → `master`. |
| Not ready | Named owners, calibrated FTE, access-policy one-pager, CMO 6-slide cut, rehearsal Q&A. |

Do **not** present from the GitHub merge screen. Download the file and open it locally.

---

## What’s ready (use these)

**Meeting deck (preferred):** [view.html](https://github.com/ChristophToth/ai-data-science-team/blob/master/presentations/cmo-insightful-ai-access/view.html) — 12 slides, keyboard ← →. Fastest for rehearsal and screenshare.

**PowerPoint (download):** [CMO_Insightful_AI_Access_Recommendation.pptx](https://github.com/ChristophToth/ai-data-science-team/blob/master/presentations/cmo-insightful-ai-access/CMO_Insightful_AI_Access_Recommendation.pptx) — 17 slides; extra option-detail and steward RACI. Same recommendation, longer run time.

**Talking points:** [SPEAKER_NOTES.md](https://github.com/ChristophToth/ai-data-science-team/blob/master/presentations/cmo-insightful-ai-access/SPEAKER_NOTES.md)

**Package index:** [README.md](https://github.com/ChristophToth/ai-data-science-team/blob/master/presentations/cmo-insightful-ai-access/README.md)

**PR:** https://github.com/ChristophToth/ai-data-science-team/pull/2

**Folder:** `presentations/cmo-insightful-ai-access/`

**Decisions on the close slide (do not add a fifth):**

1. Approve MCP or API to live Insightful **by use case**.
2. Name access owner + interim Knowledge Steward; confirm SME panel.
3. Fund domain stand-up **without** blocking demand on domain go-live.
4. Endorse access policy / anti-workaround stance.

---

## Risks that can lose the meeting

1. **Wrong artifact.** HTML is 12 slides; PPTX is 17. If you walk the PPTX cold, you will overrun and bury the ask. Pick one. Default: HTML; PPTX as leave-behind.
2. **Domain hijack.** Security already copied content + metadata. That looks “done.” It is not. You are between corpus-ready and golden-set design (~8–10 weeks to a gated pilot, then ongoing). Say out loud: MCP/API runs **in parallel**.
3. **Unnamed people.** FTE on the deck is still *indicative* (steward 0.4–0.6; MCP/API owner 0.25–0.4; SME panel 40–80 hrs stand-up). A CMO will ask who. “We’ll figure it out” invites delay.
4. **Policy vacuum.** Without MCP-vs-API intake rules and an anti-workaround line, approval becomes a slogan and shadow RAG continues.
5. **Vendor/security lag.** MCP needs enablement; not every tool speaks MCP. Have a one-line answer: *that is why API exists for custom apps — choose per project, don’t stall all access.*

---

## Five moves before the CMO sits down

1. **Lock the run-of-show.** Use the 12-slide HTML for the meeting. Time it to ~12–15 minutes plus discussion. If the calendar is tighter, cut to six: Ask → Why now → Architecture → Recommendation → Domain “you are here” → Decisions. Do not change the recommendation.
2. **Name the two owners.** Bring a proposed MCP/API access owner and an interim Knowledge Steward (plus 4–6 SME names). Decision 2 should be a confirmation, not a brainstorm.
3. **Calibrate the hours.** Replace “indicative” with a real capacity read from Insights leadership. Same ranges are fine if someone will staff them.
4. **One-page policy.** Who gets MCP, who gets API, who does **not** get to copy the corpus, what happens if they do, and that Ask AT&T domain access is gated on the golden-question scorecard. One page. Bring it as a decision aid, not a new strategy.
5. **Pre-wire the objection.** CMO / security / IT will ask “why not just Ask AT&T?” Answer in one breath: *the copy is a security control and a future employee Q&A path; it is at golden questions, not production confidence; it does not serve agents or custom apps; live Insightful via MCP or API is how we stop workarounds now.*

Optional sixth, if there is time after naming owners: a 10-question starter golden set (brands, taxonomy, time-sensitive, refuse/insufficient-evidence) so domain work has a first Tuesday — without implying domain go-live is the CMO’s near-term fix.

---

## How you should open

AI demand for Insightful is already here. Content and the assistant live only in Insightful today. Approve the right pipe by use case to the live system. Build the Ask AT&T domain as its own staffed goal. That is how we meet demand, keep governance, and protect what Stravito was chosen to do.
