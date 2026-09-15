# Speaker notes — Insightful AI Access (CMO)

## Opening

AI curiosity across marketing is rising. So is interest in putting **Insightful** into agents and AI-backed tools. We need a sanctioned path — or teams will invent workarounds.

## The three pressures

**Demand.** Product and insights teams want Insightful inside the AI experiences they are building.

**Governance.** Delay creates shadow copies, scrapes, and private RAG experiments. That is a security and brand problem, not just a tooling gap.

**Proprietary lens.** Stravito was not chosen as a file dump. It democratizes knowledge in a social, easy-to-use way. Backend semantic understanding of AT&T taxonomy, a marketing-research approach to questions, and curated collections built by teams everywhere are assets. Any long-term internal domain must earn that bar — not assume upload equals replacement.

## Recommendation in one breath

Enable **MCP** as the primary pattern for agent builders; enable **API** for custom apps that cannot use MCP yet. Keep the Ask AT&T knowledge domain moving as a **strategic side goal** with real staffing — not as the near-term demand fix.

### Why MCP over API for agents?

- Agents need a standard way to discover and call tools. MCP is that pattern.
- One governed connector scales across many AI projects.
- Live Insightful reduces copy-drift risk versus Ask Docs alone.

### Why still API?

- Many internal tools will not support MCP immediately.
- Search / Lookup / usage patterns fit backends and embedded AI features.
- Same live knowledge; different client surface.

### Why not lead with the knowledge domain?

- Security already drove a full copy (content + metadata) into Ask AT&T. Good.
- We are at **golden questions** — the quality gate — not production confidence.
- Domain Q&A does not yet replace Stravito’s UX, collections, or research-tuned assistant.
- Completing it is an operating model, not a project checkbox.

---

## Architecture wireframe (slide talking points)

Walk top → bottom:

1. **Who needs knowledge:** agent builders, custom AI tools, Ask AT&T employees  
2. **How they connect:** MCP (primary now) · API (companion) · Knowledge domain (side goal)  
3. **Where knowledge lives:**  
   - Left: **live Insightful on Stravito** (MCP + API) — semantic layer, taxonomy, collections  
   - Right: **Ask AT&T copy** — already uploaded; golden questions next; sync forever  

Punch line: *sanctioned connections, no shadow copies.* MCP/API serve demand against the live system; domain is the security-backed Ask Docs path that still needs quality work.

---

## Domain journey & timeframe (slide talking points)

Indicative **8–10 weeks** to gated pilot, then ongoing:

| Stage | When | What |
| --- | --- | --- |
| Corpus ready | DONE | Content + metadata in Ask Docs |
| Design golden set | Wks 1–2 | 50–150 questions |
| Truth answers | Wks 2–4 | SME / steward expected answers + cites |
| Blind run & score | Wks 4–5 | Scorecard vs truth |
| Tune & retest | Wks 5–8 | Fix retrieval/metadata; hit threshold |
| Gate go-live | Wk 8–9 | Policy + support + quality signed |
| Regression ops | Ongoing | Re-test on sync/model change |

**You are here:** between corpus ready and designing the golden set.  
**Say out loud:** MCP + API enablement runs in parallel — domain go-live is not a blocker for agent demand.

---

## Golden questions — how the process proceeds

You are at the right stage. Treat this like a product QA harness for knowledge.

### Step 1 — Design the golden set

Build 50–150 questions with a cross-functional SME panel.

Cover:

- High-volume business questions (brands, segments, campaigns, categories)
- AT&T taxonomy and proprietary terms (confirm the model uses our language)
- Time- and region-sensitive questions
- Ambiguous / multi-doc synthesis questions
- “Should refuse / insufficient evidence” questions (negative controls)
- Collection-specific questions (prove curated collections still matter)

Owner: Knowledge Steward. Contributors: Insights SME panel.

### Step 2 — Write truth answers

For each question, stewards/SMEs write:

- The expected answer (concise, decision-useful)
- Must-cite source documents (and metadata fields that should surface)
- Acceptable alternate phrasings
- Hard fail criteria (e.g., wrong brand, outdated wave, missing citation)

Version the pack. This becomes the regression suite.

### Step 3 — Blind run against Ask Docs

Run the full set through the domain. Score each item:

| Dimension | Pass example |
| --- | --- |
| Correctness | Facts match truth answer |
| Completeness | Key caveats present |
| Citation quality | Points to right doc / page / asset |
| Taxonomy fluency | Uses AT&T terms correctly |
| Refusal quality | Declines when evidence is weak |

Target a go-live threshold (example: ≥85% pass on priority questions; 0 critical safety fails).

### Step 4 — Tune and retest

Failures drive fixes: metadata mapping, chunking, retrieval filters, prompt instructions, sync gaps. Re-run until threshold holds.

### Step 5 — Gate go-live

Do not open broad Ask AT&T access until:

- Scorecard signed by Steward + Insights lead
- Access policy approved
- Support / escalation path live
- Sync cadence documented

### Step 6 — Ongoing regression

Re-run golden set when:

- Corpus syncs in bulk
- Model or Ask Docs config changes
- Major taxonomy or collection changes land

---

## Knowledge Steward — role sketch

**Standing accountability (indicative 0.4–0.6 FTE):**

1. Own golden-question bank and truth-answer currency  
2. Decide domain access requests against CMO-endorsed policy  
3. Monitor quality metrics; escalate wrong-answer incidents  
4. Coordinate Insightful → Ask Docs sync and metadata gaps  
5. Partner with MCP/API owner so agents and Ask AT&T cite the same sources  
6. Quarterly CMO readout: quality, usage, risk, capacity  

**SME panel:** rotating insights experts for truth answers and edge cases (~40–80 hours stand-up; light monthly thereafter).

**MCP/API program owner (0.25–0.4 FTE):** vendor enablement, client onboarding, scopes, rate limits, usage reporting, anti-sprawl guardrails.

---

## Processes to put in place (domain)

- Access request + approval workflow (and periodic access review)
- Content sync runbook (success/fail, stale content, metadata parity checks)
- Incident process for incorrect or sensitive answers
- Change calendar tied to golden-set regression
- Feedback loop from Ask AT&T users back into Insightful tagging/collections
- Clear statement: domain is complementary until quality and UX thresholds are met — Stravito remains system of engagement for curated research

---

## Decisions to ask the CMO for

1. Approve MCP + API commercial/security path for sanctioned AI projects  
2. Name MCP/API owner and interim Knowledge Steward; confirm SME panel  
3. Fund domain stand-up (golden questions + steward model) without blocking agent demand on domain go-live  
4. Endorse access policy / anti-workaround stance  

## Closing line

Serve demand with MCP + API. Build the domain with discipline. That keeps Insightful’s advantage working for AT&T’s AI ecosystem — and keeps Ask AT&T on a path that is governed, tested, and staffed to last.
