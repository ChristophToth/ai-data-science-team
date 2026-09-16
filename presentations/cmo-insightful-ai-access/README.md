# CMO Recommendation — Insightful AI Access

**Audience:** CMO  

**Recommendation:** Approve **MCP or API access by use case** to live Insightful. Treat the **Ask AT&T knowledge domain** as a **separate goal**.

**Today:** Content and the AI assistant live only in Insightful (Stravito, AT&T-branded).

## Deliverables

| File | Use |
| --- | --- |
| `view.html` | **Easiest** — open in any browser (← → / Prev-Next) |
| `CMO_Insightful_AI_Access_Recommendation.pptx` | Executive PowerPoint |
| `SPEAKER_NOTES.md` | Talking points + golden-question process |
| `build_deck.py` | Regenerates the PPTX |

## Story spine

1. AI curiosity ↑ → demand for Insightful in AI projects ↑  
2. Three pressures: **Demand**, **Governance** (workarounds), **Proprietary lens** (why Stravito was chosen)  
3. Three options: MCP / API / Ask AT&T knowledge domain  
4. **Architecture wireframe** — MCP or API by use case against live Insightful; domain = separate copy path  
5. Recommend: approve the right pipe per use case; domain stays its own track  
6. Domain is at golden questions — journey + ~8–10 week timeframe  
7. Decisions: access by use case, owners, steward funding, policy  

## Regenerate PPTX

```bash
pip install python-pptx
python presentations/cmo-insightful-ai-access/build_deck.py
```
