"""
THE 2035 EXPEDITION
A creative reframing of Majid Al Futtaim's adaptability analysis as a
desert caravan's journey to 2035 — six real business lenses become six
expedition resources, and the group's own strategic recommendations
become dials on a weather-control panel.

Global Adaptability 2 (MGB BUS 305) — Project-Based Learning
"""

import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# ----------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="The 2035 Expedition — Majid Al Futtaim",
    page_icon="🏜️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------
# REAL DATA — every figure here is sourced; see the Sources page.
# ----------------------------------------------------------------------
BASE_SCORES = {
    "Provisions (Economic)": 3.7,
    "Terrain (Geopolitical)": 3.0,
    "Instruments (Technological)": 3.2,
    "The Caravan (Social)": 3.4,
    "Camels & Wagons (Infrastructure)": 3.8,
    "Water Reserves (Sustainability)": 3.9,
}
SHORT_LABELS = ["Provisions", "Terrain", "Instruments", "Caravan", "Camels & Wagons", "Water Reserves"]
LENS_KEYS = list(BASE_SCORES.keys())

STATUS_COLOR = {
    "strong": "#8FA36B",   # olive green
    "watch": "#B08D57",    # copper
    "risk": "#A85D3D",     # terracotta
}


def status_of(score: float) -> str:
    if score >= 3.5:
        return "strong"
    if score >= 3.2:
        return "watch"
    return "risk"


# ----------------------------------------------------------------------
# CUSTOM STYLE — theme the whole app around sand, charcoal, and the
# arch motif drawn from Majid Al Futtaim's own 2013 rebrand (sand colour
# + an arch inspired by the Mall of the Emirates dome).
# ----------------------------------------------------------------------
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
      html, body, [class*="css"]  { font-family: 'Inter', sans-serif; }
      h1, h2, h3 { font-family: 'Fraunces', serif !important; }
      .stApp { background-color: #2A2925; }

      .expedition-banner {
          background: linear-gradient(180deg, #38362F 0%, #2A2925 100%);
          border: 1px solid rgba(245,241,232,0.12);
          border-radius: 18px 18px 6px 6px;
          padding: 28px 32px;
          margin-bottom: 22px;
      }
      .dune-divider {
          height: 1px;
          background: linear-gradient(90deg, transparent, rgba(201,184,150,0.4), transparent);
          margin: 22px 0;
      }
      .resource-card {
          background: #38362F;
          border: 1px solid rgba(245,241,232,0.10);
          border-left: 3px solid var(--accent, #B08D57);
          border-radius: 4px 12px 4px 4px;
          padding: 14px 18px;
          margin-bottom: 10px;
      }
      .caravan-quote {
          font-family: 'Fraunces', serif;
          font-style: italic;
          font-size: 17px;
          color: #C9B896;
          border-left: 2px solid #B08D57;
          padding: 6px 0 6px 16px;
          margin: 14px 0;
      }
      div[data-testid="stSidebar"] { background-color: #232220; }
      .stButton>button {
          border-radius: 8px 8px 3px 3px;
          border: 1px solid rgba(245,241,232,0.25);
          background-color: #38362F;
          color: #F5F1E8;
      }
      .stButton>button:hover { border-color: #B08D57; color: #B08D57; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------
# SESSION STATE — the four "weather dials" persist across reruns and
# double as the inputs for the road-ahead projection.
# ----------------------------------------------------------------------
defaults = {"dial_gov": 50, "dial_repo": 50, "dial_ai": 50, "dial_sus": 50}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


def apply_preset(gov, repo, ai, sus):
    st.session_state["dial_gov"] = gov
    st.session_state["dial_repo"] = repo
    st.session_state["dial_ai"] = ai
    st.session_state["dial_sus"] = sus


def dial_to_score(base: float, dial: int, spread: float) -> float:
    return max(1.0, min(5.0, base + ((dial - 50) / 50) * spread))


# ----------------------------------------------------------------------
# ORIGINAL SVG ARTWORK — hand-drawn vector art, not photography or any
# real company logo/trademark, to keep everything safely original.
# ----------------------------------------------------------------------
LOGO_SVG = """
<svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
  <path d="M4 36 V18 A16 16 0 0 1 36 18 V36 Z" fill="none" stroke="#C9B896" stroke-width="2"/>
  <circle cx="20" cy="22" r="6" fill="none" stroke="#B08D57" stroke-width="1.6"/>
  <path d="M20 17 L20 22 L23 25" stroke="#B08D57" stroke-width="1.4" fill="none" stroke-linecap="round"/>
</svg>
"""

BANNER_SVG = """
<svg viewBox="0 0 900 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3A3833"/>
      <stop offset="100%" stop-color="#2A2925"/>
    </linearGradient>
    <linearGradient id="duneFar" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4A4739"/>
      <stop offset="100%" stop-color="#3A3833"/>
    </linearGradient>
    <linearGradient id="duneNear" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#5C563F"/>
      <stop offset="100%" stop-color="#3A3833"/>
    </linearGradient>
  </defs>
  <rect width="900" height="220" fill="url(#sky)"/>
  <circle cx="740" cy="55" r="34" fill="#C9B896" opacity="0.9"/>
  <path d="M0 130 Q150 90 320 125 T640 110 T900 130 V220 H0 Z" fill="url(#duneFar)"/>
  <path d="M20 150 A150 150 0 0 1 300 150 V220 H20 Z" fill="none" stroke="#8f8468" stroke-width="2" opacity="0.55"/>
  <path d="M0 170 Q180 130 380 168 T780 155 T900 175 V220 H0 Z" fill="url(#duneNear)"/>
  <g opacity="0.9" transform="translate(430,158)">
    <ellipse cx="0" cy="18" rx="13" ry="7" fill="#2A2925"/>
    <path d="M-13 18 Q-6 2 2 10 Q9 -2 14 12" fill="none" stroke="#2A2925" stroke-width="3.5" stroke-linecap="round"/>
    <line x1="10" y1="0" x2="10" y2="-14" stroke="#2A2925" stroke-width="3" stroke-linecap="round"/>
    <circle cx="-9" cy="22" r="2.6" fill="#2A2925"/><circle cx="4" cy="23" r="2.6" fill="#2A2925"/>
  </g>
  <g opacity="0.85" transform="translate(490,168) scale(0.8)">
    <ellipse cx="0" cy="18" rx="13" ry="7" fill="#232220"/>
    <path d="M-13 18 Q-6 2 2 10 Q9 -2 14 12" fill="none" stroke="#232220" stroke-width="3.5" stroke-linecap="round"/>
    <circle cx="-9" cy="22" r="2.6" fill="#232220"/><circle cx="4" cy="23" r="2.6" fill="#232220"/>
  </g>
</svg>
"""

ICONS = {
    "coins": '<svg width="26" height="26" viewBox="0 0 26 26"><ellipse cx="13" cy="19" rx="9" ry="3.4" fill="none" stroke="#B08D57" stroke-width="1.6"/><ellipse cx="13" cy="14" rx="9" ry="3.4" fill="none" stroke="#B08D57" stroke-width="1.6"/><ellipse cx="13" cy="9" rx="9" ry="3.4" fill="none" stroke="#C9B896" stroke-width="1.6"/></svg>',
    "compass": '<svg width="26" height="26" viewBox="0 0 26 26"><circle cx="13" cy="13" r="10" fill="none" stroke="#A85D3D" stroke-width="1.6"/><path d="M13 6 L16 13 L13 20 L10 13 Z" fill="#A85D3D" opacity="0.8"/></svg>',
    "tools": '<svg width="26" height="26" viewBox="0 0 26 26"><path d="M6 20 L15 11" stroke="#B08D57" stroke-width="2.2" stroke-linecap="round"/><path d="M14 6 a3 3 0 1 0 6 3 l-2 -1 0 -2 z" fill="none" stroke="#B08D57" stroke-width="1.6"/><circle cx="6" cy="20" r="2.2" fill="none" stroke="#C9B896" stroke-width="1.5"/></svg>',
    "people": '<svg width="26" height="26" viewBox="0 0 26 26"><circle cx="9" cy="8" r="3.2" fill="none" stroke="#8FA36B" stroke-width="1.6"/><path d="M3 20 q0 -7 6 -7 t6 7" fill="none" stroke="#8FA36B" stroke-width="1.6"/><circle cx="18" cy="9" r="2.6" fill="none" stroke="#C9B896" stroke-width="1.4"/><path d="M14 20 q0 -6 5 -6 t5 6" fill="none" stroke="#C9B896" stroke-width="1.4"/></svg>',
    "camel": '<svg width="26" height="26" viewBox="0 0 26 26"><ellipse cx="12" cy="17" rx="9" ry="4.5" fill="none" stroke="#B08D57" stroke-width="1.6"/><path d="M4 17 Q10 3 14 11 Q17 1 21 12" fill="none" stroke="#B08D57" stroke-width="1.8" stroke-linecap="round"/><line x1="7" y1="21" x2="7" y2="25" stroke="#B08D57" stroke-width="1.6"/><line x1="17" y1="21" x2="17" y2="25" stroke="#B08D57" stroke-width="1.6"/></svg>',
    "droplet": '<svg width="26" height="26" viewBox="0 0 26 26"><path d="M13 3 C8 11 5 15 5 18.5 a8 8 0 0 0 16 0 C21 15 18 11 13 3 Z" fill="none" stroke="#8FA36B" stroke-width="1.8"/></svg>',
}


def svg_icon(name: str) -> str:
    return ICONS.get(name, "")


def current_scores():
    return {
        "Provisions (Economic)": dial_to_score(3.7, st.session_state["dial_repo"], 1.0),
        "Terrain (Geopolitical)": dial_to_score(3.0, st.session_state["dial_gov"], 1.5),
        "Instruments (Technological)": dial_to_score(3.2, st.session_state["dial_ai"], 1.5),
        "The Caravan (Social)": 3.4,
        "Camels & Wagons (Infrastructure)": 3.8,
        "Water Reserves (Sustainability)": dial_to_score(3.9, st.session_state["dial_sus"], 0.8),
    }


def overall_readiness(scores: dict) -> float:
    return sum(scores.values()) / len(scores)


# ----------------------------------------------------------------------
# SIDEBAR NAVIGATION
# ----------------------------------------------------------------------
st.sidebar.markdown(
    f"<div style='display:flex;align-items:center;gap:10px;margin-bottom:2px;'>{LOGO_SVG}"
    "<div><div style='font-family:Fraunces,serif;font-weight:600;font-size:16px;color:#F5F1E8;line-height:1.2;'>"
    "The 2035 Expedition</div></div></div>",
    unsafe_allow_html=True,
)
st.sidebar.caption("Majid Al Futtaim — Global Adaptability 2")
page = st.sidebar.radio(
    "Navigate",
    [
        "🧭 The Expedition Map",
        "🎒 Supply Manifest",
        "🌦️ Weather Control Panel",
        "🛤️ The Road Ahead",
        "🤝 Who Rides in This Caravan?",
        "📜 Field Notes & Sources",
    ],
    label_visibility="collapsed",
)
st.sidebar.markdown("<div class='dune-divider'></div>", unsafe_allow_html=True)
st.sidebar.caption(
    "Six real business lenses, reframed as expedition resources. "
    "Every figure is sourced — see Field Notes."
)

# ----------------------------------------------------------------------
# PAGE 1 — THE EXPEDITION MAP (Overview)
# ----------------------------------------------------------------------
if page == "🧭 The Expedition Map":
    st.markdown(BANNER_SVG, unsafe_allow_html=True)
    st.markdown(
        """
        <div class="expedition-banner">
        <h1 style="margin-bottom:6px;">Majid Al Futtaim's Caravan to 2035</h1>
        <p style="color:#C9B896; font-size:15px; margin:0;">
        A real, currently-operating Dubai conglomerate — Mall of the Emirates, the MENA Carrefour
        franchise, VOX Cinemas — charted as a desert expedition. The terrain is genuinely
        uncertain: a live governance transition and an unproven regional repositioning are both
        unfolding right now.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1.3])

    with col1:
        overall = overall_readiness(current_scores())
        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=overall,
                number={"suffix": " / 5", "font": {"size": 46, "color": "#F5F1E8", "family": "Fraunces"}},
                gauge={
                    "axis": {"range": [0, 5], "tickcolor": "#9D9787"},
                    "bar": {"color": "#B08D57"},
                    "bgcolor": "#38362F",
                    "borderwidth": 0,
                    "steps": [
                        {"range": [0, 2.5], "color": "rgba(168,93,61,0.25)"},
                        {"range": [2.5, 3.5], "color": "rgba(176,141,87,0.20)"},
                        {"range": [3.5, 5], "color": "rgba(143,163,107,0.22)"},
                    ],
                },
                title={"text": "Expedition Readiness", "font": {"size": 15, "color": "#C9B896"}},
            )
        )
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", height=280, margin=dict(l=20, r=20, t=50, b=10)
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(
            "<p class='caravan-quote'>\"Structurally sound, strategically exposed.\" "
            "Real strength in the wagons and the water — real risk on the terrain ahead.</p>",
            unsafe_allow_html=True,
        )

    with col2:
        scores = current_scores()
        fig2 = go.Figure()
        fig2.add_trace(
            go.Scatterpolar(
                r=list(scores.values()) + [list(scores.values())[0]],
                theta=SHORT_LABELS + [SHORT_LABELS[0]],
                fill="toself",
                fillcolor="rgba(176,141,87,0.25)",
                line=dict(color="#B08D57", width=2),
                name="Readiness",
            )
        )
        fig2.update_layout(
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(visible=True, range=[0, 5], color="#9D9787", gridcolor="rgba(245,241,232,0.12)"),
                angularaxis=dict(color="#C9B896", gridcolor="rgba(245,241,232,0.12)"),
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="#F5F1E8",
            height=340,
            margin=dict(l=60, r=60, t=30, b=30),
            showlegend=False,
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("<div class='dune-divider'></div>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Revenue, FY2025", "AED35.9B", "+6% YoY")
    c2.metric("Crew (employees)", "45,000", "14+ countries")
    c3.metric("Water Reserves target", "2040", "Net Positive")
    c4.metric("Governance", "2025", "Dubai govt. restructured board")

# ----------------------------------------------------------------------
# PAGE 2 — SUPPLY MANIFEST (Balanced Scorecard, expedition-themed)
# ----------------------------------------------------------------------
elif page == "🎒 Supply Manifest":
    st.markdown("## The Supply Manifest")
    st.caption(
        "Every expedition lives or dies on its supplies. Here's what's really in the wagons — "
        "the same evidence, organised as a Balanced Scorecard."
    )

    tabs = st.tabs(["💰 Provisions", "🧭 Terrain", "🛠️ Instruments", "👥 The Caravan", "🐫 Camels & Wagons", "💧 Water Reserves"])

    with tabs[0]:
        st.markdown(f"<div style='display:flex;align-items:center;gap:10px;'>{svg_icon('coins')}<h4 style='margin:0;'>Provisions — the Financial perspective</h4></div>", unsafe_allow_html=True)
        st.write("**Can the expedition keep moving when both the terrain and its own leadership are in flux?**")
        st.markdown(
            "- **AED35.9B** FY2025 revenue, +6% YoY — but H1 2026 growth slowed to just **1%**\n"
            "- **AED3.6B** net profit, +41% YoY, aided by property valuation gains\n"
            "- **32%** net debt-to-equity — the lowest in a decade, real capacity in reserve"
        )
        st.info("Waypoint target: keep provisions growing through 2028 despite repositioning costs.")

    with tabs[1]:
        st.markdown(f"<div style='display:flex;align-items:center;gap:10px;'>{svg_icon('compass')}<h4 style='margin:0;'>Terrain — the Geopolitical perspective</h4></div>", unsafe_allow_html=True)
        st.write("**Is the ground underfoot stable, or shifting?**")
        st.markdown(
            "- Active regional conflict and instability since **February 2026**\n"
            "- Exited Carrefour in **Kuwait & Bahrain** (2025); re-entered **Riyadh** via the Diriyah deal, same year\n"
            "- Parent-company governance restructured by Dubai's government, June 2025 — a hybrid board of "
            "5 government and 4 family representatives"
        )
        st.warning("This is the caravan's roughest ground — our lowest readiness score sits here.")

    with tabs[2]:
        st.markdown(f"<div style='display:flex;align-items:center;gap:10px;'>{svg_icon('tools')}<h4 style='margin:0;'>Instruments — the Technological perspective</h4></div>", unsafe_allow_html=True)
        st.write("**Does the caravan have the tools to navigate what's ahead?**")
        st.markdown(
            "- A real AI/data partnership with **DEWA** for energy optimisation, announced Oct 2025\n"
            "- UAE digital infrastructure faces an estimated **50,000 cyberattacks per day**\n"
            "- 85% of global retailers haven't yet scaled multi-agent AI — a real window, not yet an advantage"
        )

    with tabs[3]:
        st.markdown(f"<div style='display:flex;align-items:center;gap:10px;'>{svg_icon('people')}<h4 style='margin:0;'>The Caravan — the Learning & Growth perspective</h4></div>", unsafe_allow_html=True)
        st.write("**Does the crew itself have what this journey demands?**")
        st.markdown(
            "- **45,000** people, across 14+ countries\n"
            "- Roughly **78%** of the regional workforce is expatriate — cross-cultural leadership is core work, not a footnote\n"
            "- **Emiratisation** is a named strategic priority"
        )

    with tabs[4]:
        st.markdown(f"<div style='display:flex;align-items:center;gap:10px;'>{svg_icon('camel')}<h4 style='margin:0;'>Camels & Wagons — the Infrastructure perspective</h4></div>", unsafe_allow_html=True)
        st.write("**Can the caravan actually carry what it needs to?**")
        st.markdown(
            "- **475+** stores across 14 countries (Carrefour, HyperMax, Supeco, Myli, Sava)\n"
            "- **AED5B** committed to transforming Mall of the Emirates\n"
            "- **11 consecutive years** of GRESB Green Star certification"
        )
        st.success("The strongest wagons in the caravan — this is where the expedition is best equipped.")

    with tabs[5]:
        st.markdown(f"<div style='display:flex;align-items:center;gap:10px;'>{svg_icon('droplet')}<h4 style='margin:0;'>Water Reserves — the Sustainability perspective</h4></div>", unsafe_allow_html=True)
        st.write("**The one resource the desert never forgives running out of.**")
        st.markdown(
            "- Committed since **2017** to Net Positive in carbon *and* water by **2040** — first in the region\n"
            "- **$1.5B** sustainability-linked loan financing real, measurable targets\n"
            "- An operating solar park already powers all 35 Carrefour branches in Jordan"
        )
        st.success("The deepest reserves in the caravan — a genuine, financed, differentiator.")

# ----------------------------------------------------------------------
# PAGE 3 — WEATHER CONTROL PANEL (What-if simulator)
# ----------------------------------------------------------------------
elif page == "🌦️ Weather Control Panel":
    st.markdown("## The Weather Control Panel")
    st.caption(
        "Four dials, each one a real strategic recommendation. Turn them to see how conviction "
        "in each move changes the caravan's readiness — or jump straight to one of three named futures."
    )

    pc1, pc2, pc3, pc4 = st.columns(4)
    if pc1.button("☀️ Governed for Growth"):
        apply_preset(90, 90, 90, 90)
        st.rerun()
    if pc2.button("⛅ Steady Hand, Slow Roads"):
        apply_preset(50, 50, 50, 50)
        st.rerun()
    if pc3.button("🌪️ Fractured Empire"):
        apply_preset(10, 10, 10, 10)
        st.rerun()
    if pc4.button("↺ Reset to Today"):
        apply_preset(50, 50, 50, 50)
        st.rerun()

    st.markdown("<div class='dune-divider'></div>", unsafe_allow_html=True)

    left, right = st.columns([1, 1.1])

    with left:
        st.markdown("**Communicate governance stability**")
        st.caption("Affects: Terrain (Geopolitical)")
        st.session_state["dial_gov"] = st.slider(
            "gov", 0, 100, st.session_state["dial_gov"], label_visibility="collapsed", key="slider_gov"
        )

        st.markdown("**Phase the regional repositioning well**")
        st.caption("Affects: Provisions (Economic)")
        st.session_state["dial_repo"] = st.slider(
            "repo", 0, 100, st.session_state["dial_repo"], label_visibility="collapsed", key="slider_repo"
        )

        st.markdown("**Scale the DEWA AI model**")
        st.caption("Affects: Instruments (Technological)")
        st.session_state["dial_ai"] = st.slider(
            "ai", 0, 100, st.session_state["dial_ai"], label_visibility="collapsed", key="slider_ai"
        )

        st.markdown("**Lead with Net Positive sustainability**")
        st.caption("Affects: Water Reserves (Sustainability)")
        st.session_state["dial_sus"] = st.slider(
            "sus", 0, 100, st.session_state["dial_sus"], label_visibility="collapsed", key="slider_sus"
        )

        st.caption("Camels & Wagons and The Caravan are held steady — these four dials don't directly target them.")

    with right:
        scores = current_scores()
        overall = overall_readiness(scores)

        fig = go.Figure(
            go.Bar(
                x=list(scores.values()),
                y=SHORT_LABELS,
                orientation="h",
                marker_color=[STATUS_COLOR[status_of(v)] for v in scores.values()],
            )
        )
        fig.update_layout(
            xaxis=dict(range=[0, 5], gridcolor="rgba(245,241,232,0.08)", color="#9D9787"),
            yaxis=dict(color="#C9B896"),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=300,
            margin=dict(l=10, r=10, t=10, b=10),
            font_color="#F5F1E8",
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown(f"### {overall:.1f} / 5 Expedition Readiness")
        if overall >= 4.0:
            verdict = "Clear skies — this mix approaches **Governed for Growth**."
        elif overall <= 2.4:
            verdict = "Storm warning — this mix approaches **Fractured Empire**."
        else:
            verdict = "Overcast but moving — this closely matches today's real position."
        st.markdown(f"<p class='caravan-quote'>{verdict}</p>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# PAGE 4 — THE ROAD AHEAD (Strategy impact / prediction)
# ----------------------------------------------------------------------
elif page == "🛤️ The Road Ahead":
    st.markdown("## The Road Ahead")
    st.caption(
        "A transparent, adjustable model — not a black-box forecast — showing how far the caravan "
        "plausibly travels by 2035 if it does nothing differently, versus if it follows the strategy "
        "set on the Weather Control Panel."
    )

    scores = current_scores()
    overall = overall_readiness(scores)
    strategy_rate = 0.01 + (overall - 3.3) * 0.02
    base_rate = 0.01

    years = list(range(2026, 2036))
    do_nothing = [100]
    with_strategy = [100]
    for _ in years[1:]:
        do_nothing.append(round(do_nothing[-1] * (1 + base_rate), 1))
        with_strategy.append(round(with_strategy[-1] * (1 + strategy_rate), 1))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=do_nothing, name="Do nothing (1.0% p.a.)",
                              line=dict(color="#7D7A6E", width=2, dash="dot")))
    fig.add_trace(go.Scatter(x=years, y=with_strategy, name="With strategy (current dials)",
                              line=dict(color="#B08D57", width=3), fill="tonexty",
                              fillcolor="rgba(176,141,87,0.12)"))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(gridcolor="rgba(245,241,232,0.06)", color="#9D9787"),
        yaxis=dict(title="Distance covered (2026 = 100)", gridcolor="rgba(245,241,232,0.08)", color="#9D9787"),
        legend=dict(orientation="h", y=-0.2, font=dict(color="#C9B896")),
        height=380, margin=dict(l=10, r=10, t=20, b=10), font_color="#F5F1E8",
    )
    st.plotly_chart(fig, use_container_width=True)

    c1, c2 = st.columns(2)
    c1.metric("2035, do nothing", f"{do_nothing[-1]}")
    c2.metric("2035, with strategy", f"{with_strategy[-1]}", f"{round(with_strategy[-1]-do_nothing[-1],1)} vs. baseline")

    with st.expander("Show the formula"):
        st.code(
            "growth_with_strategy = 1.0%  +  (Readiness_Score − 3.3) × 2 percentage points\n"
            "compounded annually, 2026 → 2035",
            language="text",
        )
        st.caption(
            f"Current readiness score: {overall:.2f} → implied strategy growth rate: {strategy_rate*100:.2f}% per year. "
            "Change the dials on the Weather Control Panel page and revisit this page — it updates automatically."
        )

# ----------------------------------------------------------------------
# PAGE 5 — WHO RIDES IN THIS CARAVAN? (Ethics & stakeholders)
# ----------------------------------------------------------------------
elif page == "🤝 Who Rides in This Caravan?":
    st.markdown("## Who Rides in This Caravan?")
    st.caption("Two real tensions, and four real groups who experience them differently.")

    st.markdown("#### Whose interests come first in a government-led restructuring?")
    st.write(
        "Dubai's government stepped in to resolve a family succession dispute — stabilising for the "
        "company, but one where minority family heirs, 45,000 employees, and Dubai's own economic "
        "interests aren't automatically aligned. The company insists operations are unaffected, but a "
        "board reshaped with a government-appointed majority inevitably raises the question of whose "
        "priorities actually govern decisions."
    )

    st.markdown("#### Emiratisation vs. an expatriate-majority workforce")
    st.write(
        "Emiratisation is an explicit strategic priority, in a region where roughly 78% of the "
        "workforce is expatriate. Pursued well, this builds genuine national capability; pursued "
        "carelessly, it risks treating the majority of frontline staff as replaceable."
    )

    st.markdown("<div class='dune-divider'></div>", unsafe_allow_html=True)
    st.markdown("#### How it lands, by stakeholder")

    s1, s2 = st.columns(2)
    with s1:
        st.markdown(
            "<div class='resource-card' style='--accent:#A85D3D;'><b>Consumers</b><br>"
            "Want an uninterrupted mall and retail experience, unaffected by boardroom turmoil.</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div class='resource-card' style='--accent:#B08D57;'><b>Employees (45,000)</b><br>"
            "Want job security and clear direction while ownership and leadership remain unresolved.</div>",
            unsafe_allow_html=True,
        )
    with s2:
        st.markdown(
            "<div class='resource-card' style='--accent:#8FA36B;'><b>Family shareholders</b><br>"
            "Want fair value preservation as government representatives now hold majority board seats.</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div class='resource-card' style='--accent:#C9B896;'><b>Dubai government / regulators</b><br>"
            "Want stable governance and continued Emiratisation progress from one of the emirate's "
            "largest employers.</div>",
            unsafe_allow_html=True,
        )

# ----------------------------------------------------------------------
# PAGE 6 — FIELD NOTES & SOURCES
# ----------------------------------------------------------------------
else:
    st.markdown("## Field Notes & Sources")
    st.caption("Every figure in this expedition is real and traceable — organised by lens.")

    with st.expander("💰 Provisions (Economic)", expanded=True):
        st.markdown(
            "- Majid Al Futtaim, Press Release — *Record FY 2025 Results with 41% Net Profit Growth*, Mar 2026 — majidalfuttaim.com\n"
            "- FashionNetwork — *Majid al Futtaim sees 'resilient' 2025 with 6% revenue rise* — us.fashionnetwork.com\n"
            "- S&P Global Ratings — Majid Al Futtaim Holding LLC credit rating report, Aug 2025"
        )
    with st.expander("🧭 Terrain (Geopolitical / Governance)"):
        st.markdown(
            "- AGBI — *Dubai takes control of Majid Al Futtaim amid succession dispute*, June 2025 — agbi.com\n"
            "- Washington Times — *Dubai orders Mall of the Emirates owner to restructure its board*, June 2025\n"
            "- Khaleej Times — *Dubai's Majid Al Futtaim says business unaffected after parent company board changes*"
        )
    with st.expander("🛠️ Instruments (Technological)"):
        st.markdown(
            "- SolarQuarter — *DEWA and Majid Al Futtaim Discuss Strategic Collaboration...*, Oct 2025\n"
            "- TCS — Global Retail Outlook 2026 press release"
        )
    with st.expander("👥 The Caravan (Social)"):
        st.markdown(
            "- Gulf News — *Expatriates make up 78% of GCC's 24.6 million workers*\n"
            "- Gulf News — *Majid Al Futtaim Group reports 'resilient' Dh15.6b in H1-2021 revenue* (gender diversity loan targets)"
        )
    with st.expander("🐫 Camels & Wagons (Infrastructure)"):
        st.markdown("- Zawya — *Majid Al Futtaim receives GRESB 'Green Star' rating for the 11th consecutive year*")
    with st.expander("💧 Water Reserves (Sustainability)"):
        st.markdown(
            "- Construction Week Online — *Majid Al Futtaim to become net positive by 2040*\n"
            "- Built Environment ME — *Majid Al Futtaim closer to becoming net positive* (2021 Sustainability-Linked Loan)\n"
            "- ME Retail News — ESG progress report (Jordan solar park, Bahrain solar plant plans)"
        )

    st.markdown("<div class='dune-divider'></div>", unsafe_allow_html=True)
    st.caption(f"Built for Global Adaptability 2 (MGB BUS 305) · Project-Based Learning · Generated {datetime.now().strftime('%B %Y')}")
