"""
MarketLab Paper Viewer
A Streamlit application showcasing the research paper:
"Bridging the Prediction-Profitability Gap: A Regime-Aware Gating
Framework for Machine-Learning Trading in Indian Equity Markets"

Author: Anzar Shaikh (ORCID 0009-0005-7844-5792)
"""

from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------------
#  PAGE CONFIG
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="MarketLab — Prediction-Profitability Gap",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": (
            "Research paper viewer for *Bridging the Prediction-Profitability "
            "Gap: A Regime-Aware Gating Framework for Machine-Learning Trading "
            "in Indian Equity Markets* — Anzar Shaikh, B.E. AI & DS, "
            "University of Mumbai, 2026."
        )
    },
)

# ---------------------------------------------------------------------
#  STYLING
# ---------------------------------------------------------------------
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
        font-size: 0.8em; margin-right: 0.3rem; background: #1f3a5f; color: white;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.05rem; font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------
#  PATHS
# ---------------------------------------------------------------------
APP_DIR  = Path(__file__).parent
ASSETS   = APP_DIR / "assets"
FIGURES  = ASSETS / "figures"
PDF_PATH = ASSETS / "marketlab_paper.pdf"


# ---------------------------------------------------------------------
#  CONFIG — set these to YOUR GitHub repo for the Streamlit app
# ---------------------------------------------------------------------
GITHUB_USER = "anzr101"
GITHUB_REPO = "marketlab-paper"
GITHUB_BRANCH = "main"
PDF_REPO_PATH = "marketlab_streamlit_app/assets/marketlab_paper.pdf"
GITHUB_PDF_RAW_URL = (
    f"https://raw.githubusercontent.com/{GITHUB_USER}/"
    f"{GITHUB_REPO}/{GITHUB_BRANCH}/{PDF_REPO_PATH}"
)
GITHUB_PDF_BLOB_URL = (
    f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/"
    f"blob/{GITHUB_BRANCH}/{PDF_REPO_PATH}"
)

# ---------------------------------------------------------------------
#  HELPERS
# ---------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_pdf_bytes(path: Path) -> bytes:
    return path.read_bytes()


def render_pdf_via_github_url(pdf_url: str, height: int = 900):
    """Embed a PDF using a GitHub raw URL.

    This avoids Chrome's restrictions on large base64 data-URIs in iframes,
    which is what causes the 'This page has been blocked by Chrome' error
    when using the data-URI embed strategy.
    """
    pdf_iframe = (
        f'<iframe src="{pdf_url}" '
        f'width="100%" height="{height}" type="application/pdf" '
        f'style="border: 1px solid #dee2e6; border-radius: 6px;"></iframe>'
    )
    st.markdown(pdf_iframe, unsafe_allow_html=True)



# ---------------------------------------------------------------------
#  SIDEBAR
# ---------------------------------------------------------------------
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
    st.markdown("### Cite this work")
    st.code(
        "@misc{shaikh2026marketlab,\n"
        "  author = {Anzar Shaikh},\n"
        "  title  = {Bridging the Prediction-\n"
        "            Profitability Gap},\n"
        "  year   = {2026},\n"
        "  url    = {https://github.com/\n"
        "    anzr101/marketlab-event_aware}\n"
        "}",
        language="bibtex",
    )

    st.markdown("---")
    if PDF_PATH.exists():
        with open(PDF_PATH, "rb") as f:
            st.download_button(
                label="⬇️ Download PDF",
                data=f.read(),
                file_name="marketlab_paper.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

# ---------------------------------------------------------------------
#  HEADER
# ---------------------------------------------------------------------
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

# ---------------------------------------------------------------------
#  TABS
# ---------------------------------------------------------------------
tab_paper, tab_findings, tab_figs, tab_methods, tab_about = st.tabs(
    ["📄 Read the Paper", "🎯 Headline Findings", "📊 Figures Gallery",
     "🔬 Methods Summary", "ℹ️ About"]
)

# =====================================================================
# TAB 1: PAPER PDF EMBED
# =====================================================================
with tab_paper:
    st.markdown("### Full paper")
    st.caption(
        "21 pages, 14 figures, 8 tables. The embedded PDF below is "
        "served directly from GitHub; if your browser blocks the embed, "
        "use one of the fallback options."
    )

    # Top: prominent action buttons (always visible — never blocked)
    c1, c2, c3 = st.columns([1.2, 1.2, 1.6])
    with c1:
        if PDF_PATH.exists():
            with open(PDF_PATH, "rb") as f:
                st.download_button(
                    label="⬇️ Download PDF",
                    data=f.read(),
                    file_name="marketlab_paper.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    key="paper_tab_dl",
                )
    with c2:
        st.link_button(
            "🔗 Open in new tab",
            GITHUB_PDF_RAW_URL,
            use_container_width=True,
        )
    with c3:
        st.link_button(
            "📁 View on GitHub",
            GITHUB_PDF_BLOB_URL,
            use_container_width=True,
        )

    st.markdown("---")
    st.markdown("#### Inline preview")

    if PDF_PATH.exists():
        # Strategy 1: load PDF from GitHub raw URL (avoids Chrome
        # blocking large base64 data URIs)
        try:
            render_pdf_via_github_url(GITHUB_PDF_RAW_URL, height=900)
        except Exception as e:
            st.warning(
                f"Could not embed PDF inline: {e}. "
                "Use the buttons above to download or open in new tab."
            )

        st.markdown(
            "<small style='color:#666'>If the inline preview is blocked "
            "by your browser (Chrome occasionally blocks PDF iframes for "
            "security reasons), please use the **Download PDF** or "
            "**Open in new tab** buttons above. The paper renders "
            "perfectly in any standalone PDF viewer.</small>",
            unsafe_allow_html=True,
        )
    else:
        st.error(
            f"PDF not found at expected path: `{PDF_PATH}`. "
            "Verify `assets/marketlab_paper.pdf` is included in the repo."
        )

# =====================================================================
# TAB 2: HEADLINE FINDINGS
# =====================================================================
with tab_findings:
    st.markdown("### The paradox we identified")

    st.markdown(
        "An ensemble of 1,386 machine-learning models trained on twenty "
        "years of NSE data reported a peak coefficient of determination "
        "of $R^{2}=0.9986$. Yet, when traded over the 2022–2024 "
        "out-of-sample window, the same models lost **14.02%** annually "
        "while a passive buy-and-hold benchmark lost only 0.85%. "
        "We call this divergence the **prediction–profitability gap**, "
        "formalize it mathematically, and propose a resolution."
    )

    st.markdown("---")
    st.markdown("### Headline numbers")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            '<div class="metric-card">',
            unsafe_allow_html=True,
        )
        st.metric("ML-only annualized return", "−14.02%",
                  "−13.17 pp vs Buy & Hold", delta_color="inverse")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(
            '<div class="metric-card">',
            unsafe_allow_html=True,
        )
        st.metric("Best level-target R²", "0.9986",
                  "diagnosed as autoregressive leak",
                  delta_color="off")
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown(
            '<div class="metric-card">',
            unsafe_allow_html=True,
        )
        st.metric("Event-gated annualized return", "+9.92%",
                  "+23.94 pp vs ML-only")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(
            '<div class="metric-card">',
            unsafe_allow_html=True,
        )
        st.metric("Median R² on returns (Ablation 1)", "−0.152",
                  "100% of models negative",
                  delta_color="inverse")
        st.markdown('</div>', unsafe_allow_html=True)

    with c3:
        st.markdown(
            '<div class="metric-card">',
            unsafe_allow_html=True,
        )
        st.metric("Sharpe ratio improvement", "−0.89 → +0.24",
                  "Δ = +1.13")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(
            '<div class="metric-card">',
            unsafe_allow_html=True,
        )
        st.metric("Max drawdown reduction", "−47.14% → −22.95%",
                  "51.3% reduction")
        st.markdown('</div>', unsafe_allow_html=True)

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
        "their impact on a 0–10 scale, and *attenuates* exposure during "
        "high-impact regimes via a deterministic rule."
    )
    st.markdown(
        "The gating layer is **non-expansive** (it can only reduce "
        "exposure, never increase it), **deterministic** (same regime "
        "always produces the same exposure), and **interpretable** "
        "(every trade is traceable to a categorized event), making it "
        "compatible with SEBI audit requirements."
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
        ("US-Iran / Red Sea strikes","2024-01-11", "3.5 h", "96.5%",
         "−₹4,960",  "−₹800",   "₹4,160 saved"),
    ]
    st.markdown(
        "| Event | Date | Lead time | Confidence | ML loss | Gated loss | Outcome |\n"
        "|---|---|---|---|---|---|---|"
    )
    for row in case_data:
        st.markdown("| " + " | ".join(row) + " |")

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
# TAB 3: FIGURES GALLERY
# =====================================================================
with tab_figs:
    st.markdown("### All 14 figures from the paper")
    st.caption(
        "Each figure is generated from the actual research data. "
        "Click any figure to view at full size in a new tab."
    )

    figures_meta = [
        ("fig01_prediction_profit_gap.png",
         "Figure 1 — The prediction–profitability gap",
         "Annualized returns: Buy & Hold (−0.85%), ML Model "
         "(−14.02%), Event-Gated (+9.92%). The 23.94 percentage-point "
         "swing illustrates the central finding."),
        ("fig02_methodology_pipeline.png",
         "Figure 2 — Methodology pipeline",
         "Eight-phase research pipeline from data collection through "
         "ablation studies."),
        ("fig03_cumulative_returns.png",
         "Figure 3 — Cumulative portfolio value (782 days)",
         "Three strategies traced over the 2022-2024 out-of-sample "
         "window, with the four crisis events marked."),
        ("fig04_event_accuracy_by_category.png",
         "Figure 4 — Event classification accuracy",
         "Per-category accuracy on 40 validated events. Three "
         "categories at 100%; overall 90.0%."),
        ("fig05_event_pipeline.png",
         "Figure 5 — Event intelligence pipeline",
         "News sources → classification engine (keyword + FinBERT + "
         "BART) → category + impact score → action rules."),
        ("fig06_risk_metrics.png",
         "Figure 6 — Risk-adjusted metrics",
         "Sharpe, Sortino, and Calmar ratios. The gated overlay is "
         "the only strategy producing positive values across all three."),
        ("fig07_case_study_us_iran.png",
         "Figure 7 — US-Iran case study (worked example)",
         "Detection timeline, matched keywords, and benchmark "
         "comparison for 11 January 2024."),
        ("fig08_case_studies_summary.png",
         "Figure 8 — Four-event case study summary",
         "P&L comparison across Russia-Ukraine, Fed 75bp, SVB, "
         "and US-Iran events."),
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
# TAB 4: METHODS SUMMARY
# =====================================================================
with tab_methods:
    st.markdown("### Research approach in 90 seconds")

    st.markdown("#### Data")
    st.markdown(
        "- **Universe:** 50 large-cap NSE stocks across 6 sectors "
        "(Banking, IT, Auto, Pharma, FMCG, Energy)\n"
        "- **Time coverage:** 2004-01-01 to 2024-12-31 "
        "(approximately 5,200 trading days)\n"
        "- **Train/validation:** 2004–2021\n"
        "- **Out-of-sample (test):** 2022-01-03 to 2024-12-31 "
        "(782 trading days, the crisis-laden period)\n"
        "- **Features:** 325 technical indicators "
        "(SMA/EMA/VWAP at multiple windows, RSI, Stochastic, ROC, "
        "MACD, ATR, Bollinger, OBV, Ichimoku, lagged prices/returns, "
        "range and quantile features)"
    )

    st.markdown("#### Model ensemble (1,386 models)")
    st.markdown(
        "- **Classical ML (1,326 models):** 51 stocks × 26 algorithms "
        "(Linear, Ridge, Lasso, ElasticNet, BayesianRidge, Huber, "
        "TheilSen, RANSAC, Passive-Aggressive, SGD, SVR-RBF, "
        "SVR-Linear, Decision Tree, Random Forest, Extra Trees, "
        "AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost, "
        "KNN, MLP, Gaussian Process, Bagging, Stacking, Voting)\n"
        "- **Deep learning (60 models):** 12 stocks × 5 architectures "
        "(LSTM, GRU, BiLSTM, CNN-LSTM, Transformer with 4 attention "
        "heads)\n"
        "- **Cross-validation:** Walk-forward with expanding train "
        "windows, preserving temporal ordering"
    )

    st.markdown("#### Event intelligence layer")
    st.markdown(
        "- **Six-category taxonomy:** Geopolitical, Economic Policy, "
        "Corporate, Regulatory, Natural Disaster, Technological\n"
        "- **Detection:** keyword scoring + ProsusAI FinBERT for "
        "sentiment + facebook/bart-large-mnli zero-shot fallback\n"
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
        "- **Drawdown circuit breaker:** 15% portfolio level\n"
        "- **Statistical tests:** paired *t*-test, Diebold–Mariano, "
        "Levene"
    )

    st.markdown("#### Two ablation studies (the crucial integrity check)")
    st.markdown(
        "- **Ablation 1 (target restatement):** Retrained on "
        "next-day returns instead of price levels. Median R² "
        "collapsed from 0.981 to −0.152; **100% of robust-subset "
        "models produced negative R²**, confirming that the headline "
        "R²=0.9986 was an autoregressive leak, not genuine forecasting "
        "skill.\n"
        "- **Ablation 2 (feature ablation):** Removed ten short-lag "
        "features. R² changed by only 0.000013, showing the "
        "autoregressive leak is **pervasive** across the entire "
        "technical-indicator category rather than localized to a few "
        "specific columns."
    )

# =====================================================================
# TAB 5: ABOUT
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
        "the subject line *MarketLab — Press*. Pre-prepared assets "
        "(figures, headline numbers, quote-ready statements) are "
        "available on request."
    )

    st.markdown("### Citation")
    st.markdown(
        "If you use this work, please cite:"
    )
    st.markdown(
        '<div class="citation-block">'
        "@misc{shaikh2026marketlab,\n"
        "  author = {Anzar Shaikh},\n"
        "  title  = {Bridging the Prediction-Profitability Gap: "
        "A Regime-Aware Gating Framework for Machine-Learning Trading "
        "in Indian Equity Markets},\n"
        "  year   = {2026},\n"
        "  howpublished = {\\url{https://github.com/anzr101/marketlab-event_aware}},\n"
        "  note   = {Preprint}\n"
        "}"
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("### Acknowledgments")
    st.markdown(
        "The author thanks the open-source maintainers of "
        "scikit-learn, TensorFlow, XGBoost, LightGBM, the HuggingFace "
        "transformers library, and the ProsusAI FinBERT contributors."
    )

    st.markdown("---")
    st.caption(
        "App built with Streamlit. Last updated April 2026. "
        "© 2026 Anzar Shaikh. Paper licensed CC BY 4.0."
    )
