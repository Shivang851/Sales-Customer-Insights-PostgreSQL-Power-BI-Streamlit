# Sales & Customer Insights — PostgreSQL + Power BI + Streamlit

**Live Portfolio Project by Shivang Sharma**

---

## Project Structure

```
sales_dashboard/
├── app.py              ← Main Streamlit app
├── requirements.txt    ← Dependencies
└── charts/             ← Slide/chart images (from Power BI)
    ├── slide-01.jpg
    ├── slide-02.jpg
    └── ...
```

---

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open: http://localhost:8501

---

## Deploy to Streamlit Cloud (Free)

1. Push this folder to GitHub
2. Go to https://share.streamlit.io
3. Connect repo → select `app.py` → Deploy
4. Get your public link!

---

## Stack

- **PostgreSQL** — Data analysis queries (CTEs, Window Functions, Aggregations)
- **Power BI** — Interactive dashboard with Star Schema & DAX
- **Python + Streamlit** — This interactive case study
