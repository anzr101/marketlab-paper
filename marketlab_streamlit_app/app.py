"""
MarketLab Paper Viewer
A Streamlit application showcasing the research paper:
"Bridging the Prediction-Profitability Gap: A Regime-Aware Gating
Framework for Machine-Learning Trading in Indian Equity Markets"

Author: Anzar Shaikh (ORCID 0009-0005-7844-5792)

Inline preview strategy: pre-rendered PNG page images.
- No iframes (avoids Chrome data-URI blocking)
- No GitHub raw URLs (avoids Content-Disposition: attachment headers)
- No external dependencies (no pdf.js, no Google Docs viewer)
- Native st.image() rendering, works identically in every browser
"""

from pathlib import Path

import streamlit as st

# =====================================================================
#  PAGE CONFIG
# =====================================================================
st.set_page_config(
    page_title="MarketLab — Prediction-Profitability Gap",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": (
            "Research paper viewer for *Bridging the Prediction-Profitability "
            "Gap: A Regime-Aware Gating Framework for Machine-Learning "
            "Trading in Indian Equity Markets* — Anzar Shaikh, B.E. AI & DS, "
            "University of Mumbai, 2026."
        )
    },
)

# =====================================================================
#  STYLING
# =====================================================================
st.markdown(
    """
    <style>
    .main .block-container {padding-top: 2rem; padding-bottom: 2rem; max-width: 1100px;}
    h1, h2, h3 {color: #1f3a5f;}
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8eef5 100%);
        padding: 1rem; border-radius: 8px; border-left: 4px solid #1f3a5f;
        margin-bottom: 0.6rem;
    }
    .citation-block {
        background: #f8f9fa; padding: 1rem; border-radius: 6px;
        font-family: 'Courier New', monospace; font-size: 0.85em;
        white-space: pre-wrap; border: 1px solid #dee2e6;
    }
    .badge {
        display: inline-block; padding: 0.2rem 0.6rem; border-radius: 12px;
        font-size: 0.8em; margin-right: 0.3rem; background: #1f3a5f;
        color: white;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.05rem; font-weight: 500;
    }
    .page-image-container {
        background: #f8f9fa; padding: 1rem; border-radius: 6px;
        border: 1px solid #dee2e6; margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =====================================================================
#  PATHS
# =====================================================================
APP_DIR     = Path(__file__).parent
ASSETS      = APP_DIR / "assets"
FIGURES     = ASSETS / "figures"
PAPER_PAGES = ASSETS / "paper_pages"
PDF_PATH    = ASSETS / "marketlab_paper.pdf"


# =====================================================================
#  HELPERS
# =====================================================================
@st.cache_data(show_spinner=False)
def load_pdf_bytes(path: Path) -> bytes:
    return path.read_bytes()


@st.cache_data(show_spinner=False)
def list_paper_pages() -> list:
    """Return sorted list of pre-rendered paper page image paths."""
    if not PAPER_PAGES.exists():
        return []
    pages = sorted(PAPER_PAGES.glob("page-*.png"))
    return pages


# =====================================================================
#  SIDEBAR
# =====================================================================
with st.sidebar:
    st.markdown("## 📈 MarketLab")
    st.caption("Research preprint and supplementary materials")

    st.markdown("---")
    st.markdown("### Author")
    st.markdown(
        "**Anzar Shaikh**  \n"
        "B.E. Artificial Intelligence and Data Science  \n"
        "University of Mumbai"
    )
    st.markdown(
        "[ORCID: 0009-0005-7844-5792]"
        "(https://orcid.org/0009-0005-7844-5792)"
    )
    st.markdown("[📧 anzarsk098@gmail.com](mailto:anzarsk098@gmail.com)")

    st.markdown("---")
    st.markdown("### Quick Links")
    st.markdown(
        "[💻 Code on GitHub]"
        "(https://github.com/anzr101/marketlab-event_aware)"
    )
    st.markdown("[📊 Live demo dashboard]"
                "(https://market-optimization-lab.streamlit.app)")

    st.markdown("---")
    if PDF_PATH.exists():
        st.markdown("### Download")
        with open(PDF_PATH, "rb") as f:
            st.download_button(
                label="⬇️ Download paper (PDF)",
                data=f.read(),
                file_name="marketlab_paper.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="sidebar_dl",
            )

    st.markdown("---")
    st.markdown("### Cite this work")
    st.code(
        "@misc{shaikh2026marketlab,\n"
        "  author = {Anzar Shaikh},\n"
        "  title  = {Bridging the Prediction-\n"
        "            Profitability Gap},\n"
        "  year   = {2026}\n"
        "}",
        language="bibtex",
    )

# =====================================================================
#  HEADER
# =====================================================================
st.title("Bridging the Prediction–Profitability Gap")
st.markdown(
    "##### A Regime-Aware Gating Framework for Machine-Learning Trading "
    "in Indian Equity Markets"
)

st.markdown(
    '<span class="badge">arXiv preprint</span>'
    '<span class="badge">q-fin.TR</span>'
    '<span class="badge">cs.LG</span>'
    '<span class="badge">21 pages</span>'
    '<span class="badge">14 figures</span>',
    unsafe_allow_html=True,
)

st.markdown("**Anzar Shaikh** — University of Mumbai — April 2026")
st.markdown("---")

# =====================================================================
#  TABS
# =====================================================================
tab_paper, tab_findings, tab_figs, tab_methods, tab_about = st.tabs(
    ["📄 Read the Paper", "🎯 Headline Findings", "📊 Figures Gallery",
     "🔬 Methods Summary", "ℹ️ About"]
)

# =====================================================================
#  TAB 1: PAPER VIEWER (pre-rendered page images)
# =====================================================================
with tab_paper:
    st.markdown("### Full paper")

    pages = list_paper_pages()
    n_pages = len(pages)

    if n_pages == 0:
        st.error(
            "Pre-rendered paper pages not found at "
            f"`{PAPER_PAGES}`. Verify the `assets/paper_pages/` folder "
            "is included in the repo."
        )
        if PDF_PATH.exists():
            with open(PDF_PATH, "rb") as f:
                st.download_button(
                    label="⬇️ Download PDF",
                    data=f.read(),
                    file_name="marketlab_paper.pdf",
                    mime="application/pdf",
                )
    else:
        st.caption(
            f"21 pages, 14 figures, 8 tables. Use the controls below to "
            "navigate or scroll through all pages."
        )

        # Top action buttons
        c1, c2, c3 = st.columns(3)
        with c1:
            if PDF_PATH.exists():
                with open(PDF_PATH, "rb") as f:
                    st.download_button(
                        label="⬇️ Download PDF",
                        data=f.read(),
                        file_name="marketlab_paper.pdf",
                        mime="application/pdf",
                        use_container_width=True,
                        key="paper_tab_dl_main",
                    )
        with c2:
            st.link_button(
                "💻 Code on GitHub",
                "https://github.com/anzr101/marketlab-event_aware",
                use_container_width=True,
            )
        with c3:
            st.link_button(
                "📧 Email author",
                "mailto:anzarsk098@gmail.com?subject=MarketLab paper",
                use_container_width=True,
            )

        st.markdown("---")

        # View mode selector
        view_mode = st.radio(
            "View mode",
            options=["📖 Single page", "📚 All pages (scroll)"],
            horizontal=True,
            label_visibility="collapsed",
        )

        if view_mode == "📖 Single page":
            # Page-by-page navigator
            page_num = st.slider(
                "Page",
                min_value=1,
                max_value=n_pages,
                value=1,
                step=1,
                key="page_slider",
            )

            cn1, cn2, cn3 = st.columns([1, 2, 1])
            with cn1:
                if st.button("⬅️ Previous", use_container_width=True,
                             disabled=(page_num == 1),
                             key="prev_page"):
                    st.session_state["page_slider"] = max(1, page_num - 1)
                    st.rerun()
            with cn2:
                st.markdown(
                    f"<div style='text-align:center; "
                    f"font-weight:500; padding-top:0.3rem;'>"
                    f"Page {page_num} of {n_pages}</div>",
                    unsafe_allow_html=True,
                )
            with cn3:
                if st.button("Next ➡️", use_container_width=True,
                             disabled=(page_num == n_pages),
                             key="next_page"):
                    st.session_state["page_slider"] = min(n_pages, page_num + 1)
                    st.rerun()

            st.markdown("")
            st.image(
                str(pages[page_num - 1]),
                use_container_width=True,
            )

        else:
            # All pages, scrollable
            st.info(
                "Showing all 21 pages. Scroll to read; use the sidebar "
                "Download button to get the PDF."
            )
            for i, page_path in enumerate(pages, start=1):
                st.markdown(f"**Page {i} of {n_pages}**")
                st.image(str(page_path), use_container_width=True)
                if i < n_pages:
                    st.markdown("---")

# =====================================================================
#  TAB 2: HEADLINE FINDINGS
# =====================================================================
with tab_findings:
    st.markdown("### The paradox we identified")
    st.markdown(
        "An ensemble of 1,386 machine-learning models trained on twenty "
        "years of NSE data reported a peak coefficient of determination "
        "of $R^{2}=0.9986$. Yet, when traded over the 2022–2024 "
        "out-of-sample window, the same models lost **14.02%** "
        "annually while a passive buy-and-hold benchmark lost only "
        "0.85%. We call this divergence the **prediction–profitability "
        "gap**, formalize it mathematically, and propose a resolution."
    )

    st.markdown("---")
    st.markdown("### Headline numbers")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("ML-only annualized return", "−14.02%",
                  "−13.17 pp vs Buy & Hold", delta_color="inverse")
        st.metric("Best level-target R²", "0.9986",
                  "diagnosed as autoregressive leak",
                  delta_color="off")
    with c2:
        st.metric("Event-gated annualized return", "+9.92%",
                  "+23.94 pp vs ML-only")
        st.metric("Median R² on returns (Ablation 1)", "−0.152",
                  "100% of models negative",
                  delta_color="inverse")
    with c3:
        st.metric("Sharpe ratio improvement", "−0.89 → +0.24",
                  "Δ = +1.13")
        st.metric("Max drawdown reduction",
                  "−47.14% → −22.95%",
                  "51.3% reduction")

    st.markdown("---")
    st.markdown("### What we built")
    st.markdown(
        "A **two-layer trading architecture**:"
    )
    st.markdown(
        "1. **Signal layer** — an ML forecaster generates positions "
        "(traditional ML pipeline, 1,386 models trained).\n"
        "2. **Gating layer** — a separate event-classification system "
        "reads news, classifies events into six categories, scores "
        "their impact on a 0–10 scale, and *attenuates* exposure "
        "during high-impact regimes via a deterministic rule."
    )
    st.markdown(
        "The gating layer is **non-expansive** (it can only reduce "
        "exposure, never increase it), **deterministic** (same regime "
        "always produces the same exposure), and **interpretable** "
        "(every trade is traceable to a categorized event), making "
        "it compatible with SEBI audit requirements."
    )

    st.markdown("---")
    st.markdown("### Crisis-period case studies")

    case_data = [
        ("Russia invades Ukraine",  "2022-02-24", "3.75 h", "98.7%",
         "−₹10,200", "−₹600",   "₹9,600 saved"),
        ("Fed 75 bp hike",          "2022-06-15", "15.25 h", "99.8%",
         "−₹3,300",  "−₹990",   "₹2,310 saved"),
        ("Silicon Valley Bank fail","2023-03-10", "1.25 h", "94.2%",
         "−₹7,660",  "−₹1,860", "₹5,800 saved"),
        ("US–Iran / Red Sea strikes","2024-01-11", "3.5 h", "96.5%",
         "−₹4,960",  "−₹800",   "₹4,160 saved"),
    ]
    table_md = (
        "| Event | Date | Lead time | Confidence | ML loss | "
        "Gated loss | Outcome |\n"
        "|---|---|---|---|---|---|---|\n"
    )
    for row in case_data:
        table_md += "| " + " | ".join(row) + " |\n"
    st.markdown(table_md)
    st.markdown(
        "**Aggregate across 4 events:** ML lost ₹26,120; the gated "
        "system lost only ₹4,250. **Total saved: ₹21,870** on a "
        "₹1,00,000 simulated portfolio."
    )

    st.markdown("---")
    st.markdown("### Statistical validation")
    st.markdown(
        "- Paired *t*-test, gated vs ML-only: $t=7.49$, "
        "$p=1.9\\times 10^{-13}$\n"
        "- Diebold–Mariano test: $DM=2.21$, $p=0.027$\n"
        "- Levene's test on return-variance equality: $p=0.001$"
    )

# =====================================================================
#  TAB 3: FIGURES GALLERY
# =====================================================================
with tab_figs:
    st.markdown("### All 14 figures from the paper")
    st.caption(
        "Each figure is generated from the actual research data."
    )

    figures_meta = [
        ("fig01_prediction_profit_gap.png",
         "Figure 1 — The prediction–profitability gap",
         "Annualized returns: Buy & Hold (−0.85%), ML Model (−14.02%), "
         "Event-Gated (+9.92%). The 23.94 pp swing illustrates the "
         "central finding."),
        ("fig02_methodology_pipeline.png",
         "Figure 2 — Methodology pipeline",
         "Eight-phase research pipeline from data collection through "
         "ablation studies."),
        ("fig03_cumulative_returns.png",
         "Figure 3 — Cumulative portfolio value (782 days)",
         "Three strategies traced over the 2022–2024 out-of-sample "
         "window, with the four crisis events marked."),
        ("fig04_event_accuracy_by_category.png",
         "Figure 4 — Event classification accuracy",
         "Per-category accuracy on 40 validated events. Three "
         "categories at 100%; overall 90.0%."),
        ("fig05_event_pipeline.png",
         "Figure 5 — Event intelligence pipeline",
         "News sources → classification engine "
         "(keyword + FinBERT + BART) → category + impact score → "
         "action rules."),
        ("fig06_risk_metrics.png",
         "Figure 6 — Risk-adjusted metrics",
         "Sharpe, Sortino, and Calmar ratios. The gated overlay is "
         "the only strategy producing positive values across all "
         "three."),
        ("fig07_case_study_us_iran.png",
         "Figure 7 — US–Iran case study (worked example)",
         "Detection timeline, matched keywords, and benchmark "
         "comparison for 11 January 2024."),
        ("fig08_case_studies_summary.png",
         "Figure 8 — Four-event case study summary",
         "P&L comparison across Russia–Ukraine, Fed 75bp, SVB, and "
         "US–Iran events."),
        ("fig09_r2_distribution.png",
         "Figure 9 — R² distribution across 1,056 ML runs",
         "The headline R²=0.9986 is an outlier. Median R² is 0.254; "
         "47% of models produce negative R²."),
        ("fig10_production_architecture.png",
         "Figure 10 — Production architecture",
         "Four-layer event-driven microservices design with three "
         "deployment tiers ($300, $800, $2,000 per month)."),
        ("fig11_feature_diagnostic.png",
         "Figure 11 — Feature importance diagnostic",
         "Top features dominated by short-lag moving averages "
         "(ema_3, sma_3, close_lag_1), inducing near-autoregression."),
        ("fig12_drawdowns.png",
         "Figure 12 — Drawdown path comparison",
         "ML reaches −47.14% drawdown; the gated overlay caps "
         "drawdown at −22.95%."),
        ("fig13_ablation1_r2_collapse.png",
         "Figure 13 — Ablation 1: R² collapses on returns",
         "Same models, same features. Only the prediction target "
         "changes from level to return. R² collapses from 0.981 to "
         "−0.152; 100% of models produce negative R²."),
        ("fig14_ablation2_feature_ablation.png",
         "Figure 14 — Ablation 2: Feature ablation",
         "Removing 10 short-lag features leaves R² essentially "
         "unchanged. The autoregressive leak is pervasive across the "
         "feature category, not localized."),
    ]

    for filename, title, caption in figures_meta:
        path = FIGURES / filename
        if path.exists():
            st.markdown(f"#### {title}")
            st.image(str(path), caption=caption, use_container_width=True)
            st.markdown("---")
        else:
            st.warning(f"Figure not found: `{filename}`")

# =====================================================================
#  TAB 4: METHODS SUMMARY
# =====================================================================
with tab_methods:
    st.markdown("### Research approach in 90 seconds")

    st.markdown("#### Data")
    st.markdown(
        "- **Universe:** 50 large-cap NSE stocks across 6 sectors "
        "(Banking, IT, Auto, Pharma, FMCG, Energy)\n"
        "- **Time coverage:** 2004-01-01 to 2024-12-31 "
        "(~5,200 trading days)\n"
        "- **Train/validation:** 2004–2021\n"
        "- **Out-of-sample (test):** 2022-01-03 to 2024-12-31 "
        "(782 trading days, the crisis-laden period)\n"
        "- **Features:** 325 technical indicators"
    )

    st.markdown("#### Model ensemble (1,386 models)")
    st.markdown(
        "- **Classical ML (1,326 models):** 51 stocks × 26 algorithms\n"
        "- **Deep learning (60 models):** 12 stocks × 5 architectures "
        "(LSTM, GRU, BiLSTM, CNN-LSTM, Transformer)\n"
        "- **Cross-validation:** Walk-forward with expanding train "
        "windows"
    )

    st.markdown("#### Event intelligence layer")
    st.markdown(
        "- **Six-category taxonomy:** Geopolitical, Economic Policy, "
        "Corporate, Regulatory, Natural Disaster, Technological\n"
        "- **Detection:** keyword scoring + ProsusAI FinBERT + "
        "facebook/bart-large-mnli zero-shot fallback\n"
        "- **Output:** category + impact score on 0–10 scale\n"
        "- **Action mapping:** deterministic rule table mapping "
        "impact to exposure attenuation (1.00, 0.60, 0.30, 0.00)"
    )

    st.markdown("#### Backtesting")
    st.markdown(
        "- **Starting capital:** ₹1,00,000\n"
        "- **Transaction cost:** 0.35% round-trip\n"
        "- **Slippage:** 0.2% on large-cap orders\n"
        "- **Position sizing:** Kelly-fractional bounded at 25% per "
        "trade\n"
        "- **Drawdown circuit breaker:** 15% portfolio level"
    )

    st.markdown("#### Two ablation studies")
    st.markdown(
        "- **Ablation 1 (target restatement):** Retrained on next-day "
        "returns instead of price levels. Median R² collapsed from "
        "0.981 to −0.152; **100% of models produced negative R²**.\n"
        "- **Ablation 2 (feature ablation):** Removed ten short-lag "
        "features. R² changed by only 0.000013, showing the "
        "autoregressive leak is **pervasive** across the entire "
        "technical-indicator category."
    )

# =====================================================================
#  TAB 5: ABOUT
# =====================================================================
with tab_about:
    st.markdown("### About this work")
    st.markdown(
        "This research was conducted as part of the B.E. Artificial "
        "Intelligence and Data Science programme at the University "
        "of Mumbai, completed in 2026. The full paper is available "
        "as a preprint, with code and supplementary materials on "
        "GitHub."
    )

    st.markdown("### Contact")
    st.markdown(
        "**Author:** Anzar Shaikh  \n"
        "**Email:** [anzarsk098@gmail.com](mailto:anzarsk098@gmail.com)  \n"
        "**ORCID:** "
        "[0009-0005-7844-5792](https://orcid.org/0009-0005-7844-5792)  \n"
        "**GitHub:** "
        "[anzr101/marketlab-event_aware]"
        "(https://github.com/anzr101/marketlab-event_aware)"
    )

    st.markdown("### Press and media")
    st.markdown(
        "For media enquiries, please email "
        "[anzarsk098@gmail.com](mailto:anzarsk098@gmail.com) with "
        "subject *MarketLab — Press*."
    )

    st.markdown("### Citation")
    st.code(
        "@misc{shaikh2026marketlab,\n"
        "  author = {Anzar Shaikh},\n"
        "  title  = {Bridging the Prediction-Profitability Gap: "
        "A Regime-Aware Gating Framework for Machine-Learning Trading "
        "in Indian Equity Markets},\n"
        "  year   = {2026},\n"
        "  howpublished = {\\url{https://github.com/anzr101/marketlab-event_aware}},\n"
        "  note   = {Preprint}\n"
        "}",
        language="bibtex",
    )

    st.markdown("---")
    st.caption(
        "App built with Streamlit. Last updated April 2026. "
        "© 2026 Anzar Shaikh. Paper licensed CC BY 4.0."
    )
