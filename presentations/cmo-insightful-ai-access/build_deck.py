#!/usr/bin/env python3
"""Build CMO recommendation deck: Insightful AI access options."""

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt, Emu

# AT&T brand palette
ATT_BLUE = RGBColor(0x06, 0x7A, 0xB4)
ATT_BLUE_HL = RGBColor(0x3A, 0xA5, 0xDC)
ATT_DARK = RGBColor(0x0C, 0x25, 0x77)
ATT_ORANGE = RGBColor(0xFF, 0x72, 0x00)
BLACK = RGBColor(0x00, 0x00, 0x00)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GRAY = RGBColor(0x5A, 0x5A, 0x5A)
LT_GRAY = RGBColor(0xF2, 0xF4, 0xF7)
MED_GRAY = RGBColor(0xBC, 0xC9, 0xD6)
GREEN = RGBColor(0x6E, 0xBB, 0x1F)

W, H = Inches(13.333), Inches(7.5)


def set_run(run, size=18, bold=False, color=BLACK, font="Arial"):
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color


def add_textbox(slide, left, top, width, height, text, size=18, bold=False, color=BLACK, align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    set_run(run, size=size, bold=bold, color=color)
    return box


def add_paras(slide, left, top, width, height, lines, size=16, color=BLACK, bold_first=False, spacing=8):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(spacing)
        run = p.add_run()
        run.text = line
        set_run(run, size=size, bold=(bold_first and i == 0), color=color)
    return box


def bar(slide, color=ATT_BLUE, height=Inches(0.12)):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def footer(slide, page, total=14):
    add_textbox(slide, Inches(0.6), Inches(7.05), Inches(8), Inches(0.3), "AT&T Marketing | Insightful AI Access", size=10, color=GRAY)
    add_textbox(slide, Inches(11.5), Inches(7.05), Inches(1.3), Inches(0.3), f"{page}", size=10, color=GRAY, align=PP_ALIGN.RIGHT)


def bg(slide, color=WHITE):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    # send to back
    spTree = slide.shapes._spTree
    sp = shape._element
    spTree.remove(sp)
    spTree.insert(2, sp)


def card(slide, left, top, width, height, fill=LT_GRAY):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.fill.background()
    shape.adjustments[0] = 0.05
    return shape


def rect(slide, left, top, width, height, fill, line=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    if line is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = line
        shape.line.width = Pt(1.25)
    return shape


def wire_box(slide, left, top, width, height, title, subtitle="", fill=WHITE, title_color=ATT_DARK, border=ATT_BLUE):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = border
    shape.line.width = Pt(1.5)
    shape.adjustments[0] = 0.08
    add_textbox(slide, left + Inches(0.12), top + Inches(0.12), width - Inches(0.24), Inches(0.35), title, size=12, bold=True, color=title_color, align=PP_ALIGN.CENTER)
    if subtitle:
        add_textbox(
            slide,
            left + Inches(0.1),
            top + Inches(0.42),
            width - Inches(0.2),
            height - Inches(0.5),
            subtitle,
            size=10,
            color=GRAY,
            align=PP_ALIGN.CENTER,
        )
    return shape


def h_line(slide, left, top, width, color=ATT_BLUE):
    shape = rect(slide, left, top, width, Pt(2.5), color)
    return shape


def v_line(slide, left, top, height, color=ATT_BLUE):
    shape = rect(slide, left, top, Pt(2.5), height, color)
    return shape


def build():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H
    blank = prs.slide_layouts[6]
    page = 0

    def new():
        nonlocal page
        page += 1
        s = prs.slides.add_slide(blank)
        bg(s)
        return s

    # 1 Title
    s = new()
    bar(s, ATT_DARK, Inches(7.5))
    shape = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.35), H)
    shape.fill.solid()
    shape.fill.fore_color.rgb = ATT_BLUE
    shape.line.fill.background()
    add_textbox(s, Inches(0.9), Inches(1.8), Inches(11), Inches(0.4), "RECOMMENDATION FOR CMO", size=14, bold=True, color=ATT_BLUE_HL)
    add_textbox(s, Inches(0.9), Inches(2.3), Inches(11.5), Inches(1.5), "Unlocking Insightful for AT&T’s AI Ecosystem", size=36, bold=True, color=WHITE)
    add_textbox(
        s,
        Inches(0.9),
        Inches(4.0),
        Inches(11),
        Inches(1.0),
        "Meet rising demand for agent-ready knowledge — with governance,\nwithout workarounds, without losing what Stravito already perfected.",
        size=18,
        color=MED_GRAY,
    )
    add_textbox(s, Inches(0.9), Inches(5.6), Inches(11), Inches(0.4), "Marketing Knowledge Management  |  Confidential", size=12, color=MED_GRAY)

    # 2 The ask
    s = new()
    bar(s)
    add_textbox(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.5), "The ask", size=28, bold=True, color=ATT_DARK)
    add_textbox(s, Inches(0.6), Inches(1.1), Inches(12), Inches(0.6), "Approve a dual-track approach to Insightful AI access.", size=20, color=BLACK)
    card(s, Inches(0.6), Inches(2.0), Inches(5.8), Inches(3.8))
    add_textbox(s, Inches(0.9), Inches(2.25), Inches(5.2), Inches(0.4), "PRIMARY — NOW", size=12, bold=True, color=ATT_ORANGE)
    add_textbox(s, Inches(0.9), Inches(2.7), Inches(5.2), Inches(0.8), "Sign on for MCP (preferred) and API", size=22, bold=True, color=ATT_DARK)
    add_paras(
        s,
        Inches(0.9),
        Inches(3.6),
        Inches(5.2),
        Inches(2.0),
        [
            "Gives teams building agents and AI-backed tools a governed way to pull Insightful knowledge into their work.",
            "Solves immediate demand and reduces shadow integrations.",
        ],
        size=15,
        color=GRAY,
    )
    card(s, Inches(6.8), Inches(2.0), Inches(5.8), Inches(3.8))
    add_textbox(s, Inches(7.1), Inches(2.25), Inches(5.2), Inches(0.4), "STRATEGIC — PARALLEL", size=12, bold=True, color=ATT_BLUE)
    add_textbox(s, Inches(7.1), Inches(2.7), Inches(5.2), Inches(0.8), "Advance Ask AT&T knowledge domain", size=22, bold=True, color=ATT_DARK)
    add_paras(
        s,
        Inches(7.1),
        Inches(3.6),
        Inches(5.2),
        Inches(2.0),
        [
            "Corpus copy + metadata already uploaded for security. Next: golden questions, truth answers, governance, stewards.",
            "Treat as a side goal we invest in — not the near-term demand fix.",
        ],
        size=15,
        color=GRAY,
    )
    footer(s, page)

    # 3 Why now
    s = new()
    bar(s)
    add_textbox(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.5), "Why this matters now", size=28, bold=True, color=ATT_DARK)
    add_textbox(
        s,
        Inches(0.6),
        Inches(1.05),
        Inches(12),
        Inches(0.5),
        "AI curiosity is growing. So is interest in Insightful’s knowledge base.",
        size=18,
        color=GRAY,
    )
    labels = ["DEMAND", "GOVERNANCE", "PROPRIETARY LENS"]
    titles = [
        "People want Insightful inside their AI projects",
        "If access lags, workarounds appear",
        "Stravito is not just a document store",
    ]
    bodies = [
        "Teams building agents and AI tools need a sanctioned path to insert curated insights into product experiences.",
        "Unauthorized copies, one-off scrapes, and local RAG experiments create security, quality, and brand risk.",
        "Chosen because it democratizes knowledge socially — semantic layer, AT&T taxonomy, marketing-research AI, curated collections.",
    ]
    for i, (lab, title, body) in enumerate(zip(labels, titles, bodies)):
        left = Inches(0.6 + i * 4.15)
        card(s, left, Inches(1.9), Inches(3.95), Inches(4.2))
        add_textbox(s, left + Inches(0.25), Inches(2.15), Inches(3.45), Inches(0.35), lab, size=12, bold=True, color=ATT_BLUE)
        add_textbox(s, left + Inches(0.25), Inches(2.6), Inches(3.45), Inches(1.0), title, size=18, bold=True, color=ATT_DARK)
        add_textbox(s, left + Inches(0.25), Inches(3.8), Inches(3.45), Inches(2.0), body, size=14, color=GRAY)
    footer(s, page)

    # 4 Proprietary value
    s = new()
    bar(s)
    add_textbox(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.5), "What we would lose if we treat Insightful as “just docs”", size=26, bold=True, color=ATT_DARK)
    items = [
        ("Semantic + taxonomy fluency", "Understands AT&T terms, categories, and how marketers actually search and speak."),
        ("Marketing-research AI posture", "Assistant approaches questions like an insights professional — not a generic chatbot."),
        ("Curated collections as assets", "Team-built collections across the org are knowledge products in themselves."),
        ("Social democratization", "Easy, trusted discovery that made the platform the system of engagement."),
    ]
    for i, (t, b) in enumerate(items):
        y = Inches(1.2 + i * 1.25)
        shape = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), y, Inches(0.12), Inches(1.0))
        shape.fill.solid()
        shape.fill.fore_color.rgb = ATT_ORANGE if i == 0 else ATT_BLUE
        shape.line.fill.background()
        add_textbox(s, Inches(1.0), y, Inches(11.5), Inches(0.4), t, size=18, bold=True, color=ATT_DARK)
        add_textbox(s, Inches(1.0), y + Inches(0.4), Inches(11.5), Inches(0.5), b, size=15, color=GRAY)
    footer(s, page)

    # 5 Three options overview
    s = new()
    bar(s)
    add_textbox(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.5), "Three paths to Insightful in the AI ecosystem", size=26, bold=True, color=ATT_DARK)
    opts = [
        ("01  MCP", "Model Context Protocol", "Standard tool interface so agents can search and retrieve Insightful live, with controlled actions."),
        ("02  API", "Application programming interface", "Direct Search / Lookup connections for apps and backends that need Insightful inside custom AI tools."),
        ("03  Knowledge domain", "Ask AT&T / Ask Docs", "Q&A against a secured copy of Insightful content + metadata already loaded for data security."),
    ]
    for i, (h, sub, body) in enumerate(opts):
        y = Inches(1.2 + i * 1.8)
        card(s, Inches(0.6), y, Inches(12.1), Inches(1.6), LT_GRAY)
        add_textbox(s, Inches(0.9), y + Inches(0.25), Inches(3.5), Inches(0.4), h, size=20, bold=True, color=ATT_DARK)
        add_textbox(s, Inches(4.5), y + Inches(0.3), Inches(7.8), Inches(0.35), sub, size=14, bold=True, color=ATT_BLUE)
        add_textbox(s, Inches(4.5), y + Inches(0.7), Inches(7.8), Inches(0.7), body, size=15, color=GRAY)
    footer(s, page)

    # 6 Pros cons MCP
    s = new()
    bar(s)
    add_textbox(s, Inches(0.6), Inches(0.35), Inches(12), Inches(0.45), "Option 1 — MCP", size=26, bold=True, color=ATT_DARK)
    add_textbox(s, Inches(0.6), Inches(0.9), Inches(12), Inches(0.4), "Best fit for groups building agents and AI-backed tools.", size=16, color=GRAY)
    card(s, Inches(0.6), Inches(1.5), Inches(5.9), Inches(4.8), RGBColor(0xE8, 0xF5, 0xE9))
    add_textbox(s, Inches(0.9), Inches(1.75), Inches(5.3), Inches(0.4), "Pros", size=18, bold=True, color=GREEN)
    add_paras(
        s,
        Inches(0.9),
        Inches(2.3),
        Inches(5.3),
        Inches(3.6),
        [
            "• Agent-native: tools discover and call Insightful in agent frameworks",
            "• Live source — less drift than a copied corpus",
            "• Permissions and actions can ride with the connecting identity",
            "• Scales across many AI projects with one integration pattern",
            "• Aligns with where enterprise AI platforms are standardizing",
        ],
        size=14,
        color=BLACK,
        spacing=10,
    )
    card(s, Inches(6.8), Inches(1.5), Inches(5.9), Inches(4.8), RGBColor(0xFF, 0xF3, 0xE0))
    add_textbox(s, Inches(7.1), Inches(1.75), Inches(5.3), Inches(0.4), "Cons / watch-outs", size=18, bold=True, color=ATT_ORANGE)
    add_paras(
        s,
        Inches(7.1),
        Inches(2.3),
        Inches(5.3),
        Inches(3.6),
        [
            "• Requires vendor enablement and AT&T security review",
            "• Not every internal tool supports MCP yet",
            "• Needs clear tool scopes (search vs. retrieve vs. write)",
            "• Operational ownership: who approves agent clients?",
            "• Still depends on Stravito platform availability/SLA",
        ],
        size=14,
        color=BLACK,
        spacing=10,
    )
    footer(s, page)

    # 7 Pros cons API
    s = new()
    bar(s)
    add_textbox(s, Inches(0.6), Inches(0.35), Inches(12), Inches(0.45), "Option 2 — API", size=26, bold=True, color=ATT_DARK)
    add_textbox(s, Inches(0.6), Inches(0.9), Inches(12), Inches(0.4), "Strong companion path for custom apps and non-MCP surfaces.", size=16, color=GRAY)
    card(s, Inches(0.6), Inches(1.5), Inches(5.9), Inches(4.8), RGBColor(0xE8, 0xF5, 0xE9))
    add_textbox(s, Inches(0.9), Inches(1.75), Inches(5.3), Inches(0.4), "Pros", size=18, bold=True, color=GREEN)
    add_paras(
        s,
        Inches(0.9),
        Inches(2.3),
        Inches(5.3),
        Inches(3.6),
        [
            "• Proven enterprise pattern (Search, Lookup, usage logs)",
            "• Fits backends, intranet widgets, and bespoke AI apps",
            "• Live Insightful content and metadata",
            "• Easier for teams already shipping REST integrations",
            "• Complements MCP where MCP is not available",
        ],
        size=14,
        color=BLACK,
        spacing=10,
    )
    card(s, Inches(6.8), Inches(1.5), Inches(5.9), Inches(4.8), RGBColor(0xFF, 0xF3, 0xE0))
    add_textbox(s, Inches(7.1), Inches(1.75), Inches(5.3), Inches(0.4), "Cons / watch-outs", size=18, bold=True, color=ATT_ORANGE)
    add_paras(
        s,
        Inches(7.1),
        Inches(2.3),
        Inches(5.3),
        Inches(3.6),
        [
            "• Each product team reinvents orchestration unless we provide a shared pattern",
            "• More engineering lift per project than MCP for agent builders",
            "• Rate limits, auth, and client sprawl need central guardrails",
            "• Does not by itself teach agents “when” to call Insightful",
            "• Still platform-dependent on Stravito",
        ],
        size=14,
        color=BLACK,
        spacing=10,
    )
    footer(s, page)

    # 8 Pros cons KD
    s = new()
    bar(s)
    add_textbox(s, Inches(0.6), Inches(0.35), Inches(12), Inches(0.45), "Option 3 — Knowledge domain (Ask AT&T)", size=26, bold=True, color=ATT_DARK)
    add_textbox(s, Inches(0.6), Inches(0.9), Inches(12), Inches(0.4), "Secured copy is uploaded. We are at golden-question setup — not yet production-ready.", size=16, color=GRAY)
    card(s, Inches(0.6), Inches(1.5), Inches(5.9), Inches(4.8), RGBColor(0xE8, 0xF5, 0xE9))
    add_textbox(s, Inches(0.9), Inches(1.75), Inches(5.3), Inches(0.4), "Pros", size=18, bold=True, color=GREEN)
    add_paras(
        s,
        Inches(0.9),
        Inches(2.3),
        Inches(5.3),
        Inches(3.6),
        [
            "• Meets data-security ask: copy of content + metadata inside AT&T",
            "• Natural fit for Ask AT&T / Ask Docs employee experience",
            "• Long-term option to broaden reach beyond Stravito UI",
            "• Can become strategic internal Q&A surface for marketing knowledge",
        ],
        size=14,
        color=BLACK,
        spacing=10,
    )
    card(s, Inches(6.8), Inches(1.5), Inches(5.9), Inches(4.8), RGBColor(0xFF, 0xF3, 0xE0))
    add_textbox(s, Inches(7.1), Inches(1.75), Inches(5.3), Inches(0.4), "Cons / watch-outs", size=18, bold=True, color=ATT_ORANGE)
    add_paras(
        s,
        Inches(7.1),
        Inches(2.3),
        Inches(5.3),
        Inches(3.6),
        [
            "• Answers a copy — freshness and sync are ongoing work",
            "• Does not yet replace Stravito’s social UX, collections, or research-tuned assistant",
            "• Quality depends on golden questions, truth answers, and testing",
            "• Needs governance, stewards, and sustained support — not a one-time upload",
            "• Wrong primary fix for teams shipping agents this quarter",
        ],
        size=14,
        color=BLACK,
        spacing=10,
    )
    footer(s, page)

    # 9 Architecture wireframe — how the options connect
    s = new()
    bar(s)
    add_textbox(s, Inches(0.5), Inches(0.28), Inches(12), Inches(0.4), "Architecture wireframe — how the options connect", size=24, bold=True, color=ATT_DARK)
    add_textbox(
        s,
        Inches(0.5),
        Inches(0.72),
        Inches(12.3),
        Inches(0.3),
        "One source of curated knowledge. Three sanctioned connection patterns. No shadow copies.",
        size=13,
        color=GRAY,
    )

    # Top consumers
    wire_box(s, Inches(0.5), Inches(1.15), Inches(3.7), Inches(0.95), "Agent builders", "Cursor / Copilot agents / internal agent platforms", fill=LT_GRAY, border=ATT_ORANGE)
    wire_box(s, Inches(4.8), Inches(1.15), Inches(3.7), Inches(0.95), "Custom AI-backed tools", "Apps, intranet, backends needing Search / Lookup", fill=LT_GRAY, border=ATT_BLUE)
    wire_box(s, Inches(9.1), Inches(1.15), Inches(3.7), Inches(0.95), "Employees via Ask AT&T", "Ask Docs Q&A experience", fill=LT_GRAY, border=ATT_DARK)

    # Connector drops
    v_line(s, Inches(2.3), Inches(2.1), Inches(0.35), ATT_ORANGE)
    v_line(s, Inches(6.6), Inches(2.1), Inches(0.35), ATT_BLUE)
    v_line(s, Inches(10.9), Inches(2.1), Inches(0.35), ATT_DARK)

    # Protocol layer
    wire_box(s, Inches(0.5), Inches(2.5), Inches(3.7), Inches(1.05), "MCP  ·  PRIMARY NOW", "Tool calls: search · retrieve · cite\nLive Insightful, agent-native", fill=WHITE, title_color=ATT_ORANGE, border=ATT_ORANGE)
    wire_box(s, Inches(4.8), Inches(2.5), Inches(3.7), Inches(1.05), "API  ·  COMPANION NOW", "REST Search / Lookup / logs\nLive Insightful for custom apps", fill=WHITE, title_color=ATT_BLUE, border=ATT_BLUE)
    wire_box(s, Inches(9.1), Inches(2.5), Inches(3.7), Inches(1.05), "Knowledge domain  ·  SIDE GOAL", "Q&A on secured copy + metadata\nAsk Docs golden-question path", fill=WHITE, title_color=ATT_DARK, border=ATT_DARK)

    # Merge lines into live platform (left two) vs copy (right)
    v_line(s, Inches(2.3), Inches(3.55), Inches(0.4), ATT_ORANGE)
    v_line(s, Inches(6.6), Inches(3.55), Inches(0.4), ATT_BLUE)
    h_line(s, Inches(2.3), Inches(3.95), Inches(4.3), ATT_BLUE)
    v_line(s, Inches(4.45), Inches(3.95), Inches(0.35), ATT_BLUE)
    v_line(s, Inches(10.9), Inches(3.55), Inches(0.75), ATT_DARK)

    # Bottom systems
    wire_box(
        s,
        Inches(0.9),
        Inches(4.4),
        Inches(6.6),
        Inches(1.55),
        "Insightful on Stravito  ·  LIVE SYSTEM OF ENGAGEMENT",
        "Semantic layer · AT&T taxonomy · marketing-research assistant\nCurated collections · permissions · source of truth for MCP & API",
        fill=RGBColor(0xE8, 0xF1, 0xF8),
        title_color=ATT_DARK,
        border=ATT_BLUE,
    )
    wire_box(
        s,
        Inches(8.3),
        Inches(4.4),
        Inches(4.5),
        Inches(1.55),
        "Ask AT&T domain COPY",
        "Full content + metadata uploaded\nYou are here → golden questions\nSync / freshness required ongoing",
        fill=RGBColor(0xF5, 0xF5, 0xF8),
        title_color=ATT_DARK,
        border=ATT_DARK,
    )

    # Legend strip
    rect(s, Inches(0.5), Inches(6.2), Inches(12.3), Inches(0.65), LT_GRAY)
    add_textbox(
        s,
        Inches(0.7),
        Inches(6.32),
        Inches(11.9),
        Inches(0.45),
        "Read left→right for demand: MCP/API unlock agents now against live Insightful.  Right path = security-driven copy for Ask AT&T — strategic, staffed, tested before broad trust.",
        size=12,
        color=GRAY,
    )
    footer(s, page)

    # 10 Recommendation
    s = new()
    bar(s)
    add_textbox(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.5), "Recommendation", size=28, bold=True, color=ATT_DARK)
    card(s, Inches(0.6), Inches(1.15), Inches(12.1), Inches(1.6), ATT_DARK)
    add_textbox(
        s,
        Inches(0.95),
        Inches(1.4),
        Inches(11.4),
        Inches(1.1),
        "Sign on for MCP as the primary path for agent builders; enable API alongside it for custom AI tools. Advance the Ask AT&T knowledge domain as a strategic side investment — not the near-term demand solution.",
        size=18,
        color=WHITE,
    )
    add_paras(
        s,
        Inches(0.6),
        Inches(3.1),
        Inches(12),
        Inches(3.5),
        [
            "Why MCP first for agents: it is the cleanest way for AI tools to call Insightful as a governed capability — search, retrieve, cite — without each team inventing a private pipeline.",
            "Why API with it: many AT&T apps will not speak MCP yet; Search/Lookup covers those surfaces with the same live knowledge.",
            "Why domain stays strategic: security already drove a full copy into Ask Docs. That investment is real — and unfinished. Completing it requires golden questions, stewards, and operating cadence before it can rival Insightful’s curated experience.",
        ],
        size=15,
        color=GRAY,
        spacing=12,
    )
    footer(s, page)

    # 10 Golden questions process
    s = new()
    bar(s)
    add_textbox(s, Inches(0.6), Inches(0.3), Inches(12), Inches(0.45), "Knowledge domain — where we are: golden questions", size=24, bold=True, color=ATT_DARK)
    add_textbox(
        s,
        Inches(0.6),
        Inches(0.85),
        Inches(12),
        Inches(0.4),
        "This is the quality gate before Ask AT&T should be trusted with Insightful answers.",
        size=15,
        color=GRAY,
    )
    steps = [
        ("1. Design the set", "50–150 questions spanning priority brands, categories, regions, taxonomy terms, and hard negatives."),
        ("2. Write truth answers", "SME / steward authors expected answers with citations to source docs and metadata."),
        ("3. Run & score", "Ask Docs answers each golden question; score correctness, completeness, citation quality, refusal behavior."),
        ("4. Tune & retest", "Fix retrieval, metadata, chunking, prompts; re-run until threshold met."),
        ("5. Gate go-live", "Publish only when quality bar + access policy + support model are signed."),
        ("6. Regression", "Re-run golden set when corpus syncs or models change."),
    ]
    for i, (t, b) in enumerate(steps):
        col = i % 3
        row = i // 3
        left = Inches(0.6 + col * 4.15)
        top = Inches(1.4 + row * 2.5)
        card(s, left, top, Inches(3.95), Inches(2.25))
        add_textbox(s, left + Inches(0.2), top + Inches(0.25), Inches(3.5), Inches(0.4), t, size=16, bold=True, color=ATT_BLUE)
        add_textbox(s, left + Inches(0.2), top + Inches(0.75), Inches(3.5), Inches(1.3), b, size=13, color=GRAY)
    footer(s, page)

    # 12 Knowledge domain journey + timeframe
    s = new()
    bar(s)
    add_textbox(s, Inches(0.5), Inches(0.28), Inches(12), Inches(0.4), "Knowledge domain journey — Q&A quality path and timeframe", size=22, bold=True, color=ATT_DARK)
    add_textbox(
        s,
        Inches(0.5),
        Inches(0.7),
        Inches(12.3),
        Inches(0.3),
        "Indicative ~8–10 week stand-up to gated pilot, then ongoing steward operations. Calibrate to SME capacity.",
        size=12,
        color=GRAY,
    )

    # Timeline base line
    h_line(s, Inches(0.7), Inches(1.55), Inches(11.9), MED_GRAY)

    journey = [
        ("DONE", "Corpus ready", "Content + metadata\ncopied into Ask Docs", ATT_BLUE, True),
        ("Wks 1–2", "Design golden set", "50–150 Qs across\ntaxonomy & edge cases", ATT_ORANGE, True),
        ("Wks 2–4", "Truth answers", "SME / steward writes\nexpected answers + cites", ATT_DARK, False),
        ("Wks 4–5", "Blind run & score", "Ask Docs answers;\nscorecard vs truth", ATT_DARK, False),
        ("Wks 5–8", "Tune & retest", "Fix retrieval / metadata;\nre-run to threshold", ATT_DARK, False),
        ("Wk 8–9", "Gate go-live", "Policy + support +\nquality bar signed", ATT_DARK, False),
        ("Ongoing", "Regression ops", "Re-test on sync /\nmodel change; steward", GREEN, False),
    ]
    n = len(journey)
    span = 11.6
    start_x = 0.75
    for i, (when, title, detail, color, current) in enumerate(journey):
        cx = start_x + (span * i / (n - 1))
        # dot
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx), Inches(1.42), Inches(0.28), Inches(0.28))
        dot.fill.solid()
        dot.fill.fore_color.rgb = color
        dot.line.fill.background()
        # card below or above alternating for readability — all below with vertical stub
        v_line(s, Inches(cx + 0.12), Inches(1.7), Inches(0.25), color)
        card_top = Inches(2.0)
        fill = RGBColor(0xFF, 0xF3, 0xE0) if current and when != "DONE" else (RGBColor(0xE8, 0xF1, 0xF8) if when == "DONE" else LT_GRAY)
        if when == "Ongoing":
            fill = RGBColor(0xE8, 0xF5, 0xE9)
        box_w = Inches(1.65)
        left = Inches(cx - 0.68)
        card(s, left, card_top, box_w, Inches(2.35), fill)
        add_textbox(s, left + Inches(0.08), card_top + Inches(0.12), box_w - Inches(0.16), Inches(0.28), when, size=10, bold=True, color=color, align=PP_ALIGN.CENTER)
        add_textbox(s, left + Inches(0.08), card_top + Inches(0.42), box_w - Inches(0.16), Inches(0.55), title, size=11, bold=True, color=ATT_DARK, align=PP_ALIGN.CENTER)
        add_textbox(s, left + Inches(0.08), card_top + Inches(1.05), box_w - Inches(0.16), Inches(1.1), detail, size=10, color=GRAY, align=PP_ALIGN.CENTER)

    # You are here callout
    rect(s, Inches(0.5), Inches(4.55), Inches(12.3), Inches(1.0), RGBColor(0xFF, 0xF3, 0xE0))
    add_textbox(s, Inches(0.7), Inches(4.65), Inches(3.2), Inches(0.35), "YOU ARE HERE", size=12, bold=True, color=ATT_ORANGE)
    add_textbox(
        s,
        Inches(0.7),
        Inches(5.0),
        Inches(11.8),
        Inches(0.45),
        "Upload complete. Next critical path = design golden questions + truth answers with SME panel, then score Ask Docs before any broad access.",
        size=13,
        color=BLACK,
    )

    # Parallel note
    add_textbox(
        s,
        Inches(0.5),
        Inches(5.8),
        Inches(12.3),
        Inches(0.9),
        "Parallel track (not on this timeline): MCP + API vendor enablement and security review can proceed immediately to serve agent demand — domain go-live is not a blocker.",
        size=12,
        color=GRAY,
    )
    footer(s, page)

    # 13 What domain needs (pitch)
    s = new()
    bar(s)
    add_textbox(s, Inches(0.6), Inches(0.35), Inches(12), Inches(0.45), "Strategic investment: what the knowledge domain needs", size=24, bold=True, color=ATT_DARK)
    needs = [
        ("Golden Q&A pack", "Question bank + truth answers owned by insights SMEs; versioned like a product artifact."),
        ("Governance & access", "Who may query, who may publish, DLP/classification, audit of Ask AT&T usage."),
        ("Knowledge steward role", "Named owner for corpus health, sync exceptions, answer quality, and escalation."),
        ("Sync & freshness", "Cadence from Insightful → domain copy; metadata parity; stale-content playbook."),
        ("Testing & release", "Pre-release golden-set scorecard; change management when models or chunking change."),
        ("Ongoing support", "Tier-1 user help, steward office hours, feedback loop into collections and tagging."),
        ("Success metrics", "Answer quality %, citation hit rate, time-to-insight, deflection from workarounds."),
        ("Risk controls", "Wrong-answer escalation, “I don’t know” policy, sensitive-topic handling."),
    ]
    for i, (t, b) in enumerate(needs):
        col = i % 4
        row = i // 4
        left = Inches(0.5 + col * 3.2)
        top = Inches(1.1 + row * 2.85)
        card(s, left, top, Inches(3.05), Inches(2.6))
        add_textbox(s, left + Inches(0.15), top + Inches(0.2), Inches(2.75), Inches(0.55), t, size=14, bold=True, color=ATT_DARK)
        add_textbox(s, left + Inches(0.15), top + Inches(0.85), Inches(2.75), Inches(1.5), b, size=12, color=GRAY)
    footer(s, page)

    # 12 Human impact / steward
    s = new()
    bar(s)
    add_textbox(s, Inches(0.6), Inches(0.35), Inches(12), Inches(0.45), "Human impact — roles, hours, support", size=26, bold=True, color=ATT_DARK)
    add_textbox(s, Inches(0.6), Inches(0.9), Inches(12), Inches(0.35), "Indicative planning ranges for CMO discussion (calibrate with HR / insights capacity).", size=13, color=GRAY)
    # table-like cards
    rows = [
        ("Knowledge Steward (lead)", "Standing role", "0.4–0.6 FTE ongoing", "Corpus quality, golden set, access requests, sync exceptions, SME coordination"),
        ("Insights SMEs (panel)", "Rotating", "~40–80 hrs stand-up; 4–8 hrs/mo", "Truth answers, taxonomy edge cases, approve go-live scorecard"),
        ("KM / platform ops", "Shared", "~20–40 hrs stand-up; 2–4 hrs/wk", "Sync jobs, metadata, Ask AT&T config, release testing"),
        ("Security / compliance", "Checkpoint", "~15–25 hrs initial", "Access model, audit, data-class controls, exception review"),
        ("MCP / API program owner", "Standing", "0.25–0.4 FTE", "Vendor enablement, client onboarding, guardrails, usage reporting"),
    ]
    headers = ["Role", "Mode", "Effort", "Responsibility"]
    y0 = Inches(1.35)
    for j, h in enumerate(headers):
        xs = [0.6, 3.4, 5.3, 8.0]
        ws = [2.7, 1.8, 2.6, 4.6]
        add_textbox(s, Inches(xs[j]), y0, Inches(ws[j]), Inches(0.35), h, size=12, bold=True, color=ATT_BLUE)
    for i, row in enumerate(rows):
        y = Inches(1.8 + i * 0.9)
        if i % 2 == 0:
            shape = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), y - Inches(0.1), Inches(12.3), Inches(0.85))
            shape.fill.solid()
            shape.fill.fore_color.rgb = LT_GRAY
            shape.line.fill.background()
        xs = [0.6, 3.4, 5.3, 8.0]
        ws = [2.7, 1.8, 2.6, 4.6]
        for j, cell in enumerate(row):
            add_textbox(s, Inches(xs[j]), y, Inches(ws[j]), Inches(0.7), cell, size=12, bold=(j == 0), color=BLACK)
    footer(s, page)

    # 13 Steward RACI snippet
    s = new()
    bar(s)
    add_textbox(s, Inches(0.6), Inches(0.35), Inches(12), Inches(0.45), "Knowledge Steward — proposed accountability", size=26, bold=True, color=ATT_DARK)
    duties = [
        "Own the golden-question bank and truth-answer currency with SME panel.",
        "Approve / deny domain access requests against CMO-endorsed policy.",
        "Monitor answer quality metrics and escalate wrong-answer incidents.",
        "Coordinate Insightful → Ask Docs sync issues and metadata gaps.",
        "Partner with MCP/API owner so agent experiences cite the same sources of truth.",
        "Report quarterly to CMO: quality, usage, risks, and capacity needs.",
    ]
    for i, d in enumerate(duties):
        y = Inches(1.15 + i * 0.85)
        num = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.7), y, Inches(0.45), Inches(0.45))
        num.fill.solid()
        num.fill.fore_color.rgb = ATT_BLUE
        num.line.fill.background()
        add_textbox(s, Inches(0.78), y + Inches(0.05), Inches(0.35), Inches(0.35), str(i + 1), size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
        add_textbox(s, Inches(1.4), y + Inches(0.05), Inches(11), Inches(0.6), d, size=16, color=BLACK)
    footer(s, page)

    # 14 Decision / next steps
    s = new()
    bar(s)
    add_textbox(s, Inches(0.6), Inches(0.35), Inches(12), Inches(0.45), "Decision requested", size=28, bold=True, color=ATT_DARK)
    cards_data = [
        ("1", "Approve MCP + API path", "Authorize commercial/security engagement to enable Insightful MCP and API for sanctioned AI projects."),
        ("2", "Name program owners", "Assign MCP/API owner and interim Knowledge Steward; confirm SME panel."),
        ("3", "Fund domain as side goal", "Endorse golden-question stand-up and steward operating model — without blocking agent demand on domain go-live."),
        ("4", "Set access policy", "CMO-backed rules: who gets MCP/API credentials; who gets Ask AT&T domain access; anti-workaround stance."),
    ]
    for i, (n, t, b) in enumerate(cards_data):
        col = i % 2
        row = i // 2
        left = Inches(0.6 + col * 6.3)
        top = Inches(1.1 + row * 2.6)
        card(s, left, top, Inches(6.0), Inches(2.35))
        add_textbox(s, left + Inches(0.3), top + Inches(0.3), Inches(0.5), Inches(0.4), n, size=22, bold=True, color=ATT_ORANGE)
        add_textbox(s, left + Inches(0.9), top + Inches(0.35), Inches(4.8), Inches(0.45), t, size=18, bold=True, color=ATT_DARK)
        add_textbox(s, left + Inches(0.3), top + Inches(1.0), Inches(5.4), Inches(1.1), b, size=14, color=GRAY)
    footer(s, page)

    # 15 Closing
    s = new()
    bar(s, ATT_DARK, H)
    shape = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.35), H)
    shape.fill.solid()
    shape.fill.fore_color.rgb = ATT_BLUE
    shape.line.fill.background()
    add_textbox(s, Inches(0.9), Inches(2.2), Inches(11.5), Inches(1.2), "Serve demand with MCP + API.\nBuild the domain with discipline.", size=32, bold=True, color=WHITE)
    add_textbox(
        s,
        Inches(0.9),
        Inches(3.8),
        Inches(11),
        Inches(1.2),
        "That keeps Insightful’s proprietary advantage working for AT&T’s AI ecosystem —\nand keeps Ask AT&T on a path that is governed, tested, and staffed to last.",
        size=16,
        color=MED_GRAY,
    )
    add_textbox(s, Inches(0.9), Inches(5.5), Inches(11), Inches(0.4), "AT&T Marketing  |  Insightful AI Access Recommendation", size=12, color=MED_GRAY)

    out = "/workspace/presentations/cmo-insightful-ai-access/CMO_Insightful_AI_Access_Recommendation.pptx"
    prs.save(out)
    print(out)


if __name__ == "__main__":
    build()
