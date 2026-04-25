# MarketLab Paper Viewer

A Streamlit application showcasing the research paper *Bridging the Prediction-Profitability Gap: A Regime-Aware Gating Framework for Machine-Learning Trading in Indian Equity Markets*.

**Author:** Anzar Shaikh ([ORCID 0009-0005-7844-5792](https://orcid.org/0009-0005-7844-5792))
**Affiliation:** B.E. Artificial Intelligence and Data Science, University of Mumbai
**Contact:** anzarsk098@gmail.com

---

## What this app does

A clean, professional viewer for the research paper that lets visitors:

- Read the paper inline (embedded PDF)
- Download the PDF
- See headline findings and key metrics
- Browse all 14 figures with explanations
- Read a 90-second methods summary
- Get the citation in BibTeX format
- Find contact information for press, journals, recruiters

---

## Repo structure

```
.
├── app.py                       # Main Streamlit app
├── requirements.txt             # Python dependencies (just streamlit)
├── .streamlit/
│   └── config.toml              # Theme settings
├── assets/
│   ├── marketlab_paper.pdf      # The research paper (21 pages)
│   └── figures/
│       ├── fig01_prediction_profit_gap.png
│       ├── fig02_methodology_pipeline.png
│       ├── ... (14 figures total)
│       └── fig14_ablation2_feature_ablation.png
└── README.md                    # This file
```

---

## Deploy to Streamlit Cloud (10 minutes)

### Step 1 — Create a new GitHub repo

1. Go to <https://github.com/new>
2. Repository name: `marketlab-paper` (or similar; do NOT name it `marketlab-event_aware` — that's your existing code repo)
3. Visibility: **Public**
4. Initialize: leave unchecked (no README, no .gitignore, no license — we'll add them)
5. Click "Create repository"

### Step 2 — Upload the files

**Option A — Web interface (easiest):**

1. On the new repo page, click "uploading an existing file"
2. Drag the entire `marketlab-paper-app` folder contents (including the `assets/` and `.streamlit/` subfolders)
3. Commit message: "Initial deployment"
4. Click "Commit changes"

**Option B — Git CLI:**

```bash
cd marketlab-paper-app
git init
git add .
git commit -m "Initial deployment"
git branch -M main
git remote add origin https://github.com/anzr101/marketlab-paper.git
git push -u origin main
```

### Step 3 — Deploy to Streamlit Cloud

1. Go to <https://streamlit.io/cloud> and sign in with GitHub
2. Click **"New app"**
3. Select:
   - **Repository:** `anzr101/marketlab-paper`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. (Optional) **App URL** subdomain: pick something memorable like `marketlab-paper`
5. Click **"Deploy!"**

Deployment takes 2-3 minutes. Your app will be live at:

```
https://marketlab-paper.streamlit.app
```

(Or whatever subdomain you chose.)

### Step 4 — Verify

Open the URL in a browser and confirm:
- ✅ Title and abstract render correctly
- ✅ "Read the Paper" tab shows the embedded PDF
- ✅ "Headline Findings" tab shows the metric cards
- ✅ "Figures Gallery" tab shows all 14 figures
- ✅ "Methods Summary" tab loads
- ✅ "About" tab loads
- ✅ Sidebar shows author info, ORCID link, GitHub link
- ✅ Download PDF button in sidebar works

---

## To update the paper later

If you produce a new version of the paper (v5, journal-formatted version, etc.):

1. Replace `assets/marketlab_paper.pdf` in the GitHub repo
2. (Optional) Replace any updated figures in `assets/figures/`
3. Push to GitHub
4. Streamlit Cloud auto-redeploys within 1-2 minutes

No app code changes needed.

---

## Memory and performance

- **App memory usage:** ~150 MB (well under Streamlit Cloud's 1 GB free-tier limit)
- **Cold start time:** ~5 seconds on first visit
- **Subsequent loads:** under 1 second (PDF cached, figures cached)
- **Cost:** free forever for public apps

---

## Local development

To preview locally before deploying:

```bash
pip install streamlit
cd marketlab-paper-app
streamlit run app.py
```

App opens at <http://localhost:8501>.

---

## Common issues

**"PDF not found at expected path"** — The `assets/marketlab_paper.pdf` file did not upload to GitHub. Check the GitHub repo and re-upload if missing. The file is ~600 KB.

**Some figures missing** — Same cause. Verify all 14 PNG files are in `assets/figures/` on GitHub.

**Streamlit Cloud says "App is sleeping"** — Free-tier apps go to sleep after 7 days of no traffic. Click the "Wake up" button; first load takes ~30 seconds, then normal performance.

**Want a custom domain (e.g., `paper.anzarshaikh.com`)?** — Streamlit's free tier doesn't support custom domains. You can either pay $20/month for a Streamlit team plan, or use a GitHub Pages redirect from your domain to the Streamlit URL.

---

## License and attribution

App code: MIT. Paper content: CC BY 4.0. Figures generated from the author's research data.

If you use the paper in your own research, please cite per the BibTeX entry shown in the app.

---

## Contact

- Email: [anzarsk098@gmail.com](mailto:anzarsk098@gmail.com)
- ORCID: <https://orcid.org/0009-0005-7844-5792>
- GitHub: <https://github.com/anzr101/marketlab-event_aware>
