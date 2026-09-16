# The 2035 Expedition — Majid Al Futtaim Adaptability Analysis

An interactive Streamlit app that reframes a real strategic analysis of
**Majid Al Futtaim** (Mall of the Emirates, the MENA Carrefour franchise,
VOX Cinemas, Ski Dubai) as a desert caravan's journey to 2035.

Built for **Global Adaptability 2 (MGB BUS 305)**, Project-Based Learning.

## What's inside

- **🧭 The Expedition Map** — overview gauge + radar chart of overall readiness
- **🎒 Supply Manifest** — the six business lenses (Economic, Geopolitical,
  Technological, Social, Infrastructure, Sustainability) reframed as
  expedition resources, each backed by real, sourced data
- **🌦️ Weather Control Panel** — four live sliders, one per strategic
  recommendation, that recalculate the Adaptability Score in real time,
  plus three preset buttons for the group's three named future scenarios
- **🛤️ The Road Ahead** — a transparent, adjustable growth projection to
  2035, comparing "do nothing" against "with strategy"
- **🤝 Who Rides in This Caravan?** — the ethical tensions and stakeholder
  view
- **📜 Field Notes & Sources** — every source used, organised by lens

## Run it locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL Streamlit prints (usually `http://localhost:8501`).

## Deploy it for free on Streamlit Community Cloud

1. **Create a GitHub repository** and push this folder to it:

   ```bash
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git branch -M main
   git push -u origin main
   ```

   (Create the empty repo first at github.com/new — don't initialise it
   with a README, since this folder already has one.)

2. Go to **[share.streamlit.io](https://share.streamlit.io)** and sign in
   with your GitHub account.

3. Click **"New app"**, select your repository, branch (`main`), and set
   the main file path to `app.py`.

4. Click **Deploy**. Streamlit Cloud installs `requirements.txt`
   automatically and gives you a public URL like
   `https://<your-app-name>.streamlit.app` within a minute or two.

5. Every time you `git push` new changes to `main`, the deployed app
   updates automatically.

## A note on the numbers

Every statistic in this app is real and sourced — see the **Field Notes
& Sources** page. The Weather Control Panel's scoring model and The Road
Ahead's growth projection are transparent, simple linear models built for
this analysis, not certified forecasts — the formula is shown on-screen
so it can be checked, adjusted, or challenged.
