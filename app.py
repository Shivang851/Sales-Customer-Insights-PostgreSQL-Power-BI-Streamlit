import streamlit as st
from PIL import Image
import os

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Sales & Customer Insights | Shivang Sharma",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    background-color: #0d0d0d;
    color: #f0ece4;
}
.stApp { background-color: #0d0d0d; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0a0a0a !important;
    border-right: 1px solid #1e1e1e;
}
section[data-testid="stSidebar"] * { color: #aaa !important; }
section[data-testid="stSidebar"] .stRadio label { 
    font-family: 'DM Mono', monospace !important;
    font-size: 0.8rem !important;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #0d0d0d 0%, #111 50%, #0d1a00 100%);
    border: 1px solid #1e1e1e;
    border-radius: 16px;
    padding: 3rem 3rem 2.5rem 3rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -50%; right: -10%;
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(200,255,0,0.04) 0%, transparent 70%);
    pointer-events: none;
}
.hero-tag {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    color: #c8ff00;
    text-transform: uppercase;
    letter-spacing: 3px;
    margin-bottom: 1rem;
    display: block;
}
.hero-title {
    font-size: 2.8rem;
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -2px;
    color: #f0ece4;
    margin: 0 0 0.8rem 0;
}
.hero-title span { color: #c8ff00; }
.hero-sub {
    font-family: 'DM Mono', monospace;
    font-size: 0.8rem;
    color: #555;
    letter-spacing: 1px;
}
.stack-pill {
    display: inline-block;
    background: #111;
    border: 1px solid #2a2a2a;
    color: #888;
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    padding: 4px 12px;
    border-radius: 100px;
    margin: 4px 4px 0 0;
}

/* KPI Row */
.kpi-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: #1a1a1a;
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 2.5rem;
    border: 1px solid #1a1a1a;
}
.kpi-card {
    background: #0f0f0f;
    padding: 1.4rem 1.6rem;
}
.kpi-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    color: #444;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 0.4rem;
}
.kpi-value {
    font-size: 2.2rem;
    font-weight: 800;
    color: #c8ff00;
    letter-spacing: -1.5px;
    line-height: 1;
}
.kpi-note {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    color: #333;
    margin-top: 5px;
}

/* Section Header */
.section-header {   
    display: flex;
    align-items: baseline;
    gap: 1rem;
    margin: 2.5rem 0 1.5rem 0;
    padding-bottom: 0.8rem;
    border-bottom: 1px solid #1a1a1a;
}
.section-num {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    color: #c8ff00;
    letter-spacing: 2px;
}
.section-title {
    font-size: 1.4rem;
    font-weight: 800;
    color: #f0ece4;
    letter-spacing: -0.5px;
    margin: 0;
}

/* Analysis card */
.analysis-card {
    background: #0f0f0f;
    border: 1px solid #1e1e1e;
    border-radius: 14px;
    overflow: hidden;
    margin-bottom: 2rem;
}
.analysis-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    color: #007cf9;
    text-transform: uppercase;
    letter-spacing: 2px;
    padding: 1rem 1.4rem 0 1.4rem;
}
.analysis-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #f0ece4;
    padding: 0.3rem 1.4rem 1rem 1.4rem;
}

/* SQL block */
.sql-wrap {
    background: #FFFFFF;
    border-top: 1px solid #1a1a1a;
    border-bottom: 1px solid #1a1a1a;
    padding: 1.2rem 1.4rem;
}
.sql-title {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    color: #191970;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 0.6rem;
}
.sql-code {
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    color: #191970;
    line-height: 1.8;
    white-space: pre;
    overflow-x: auto;
    margin: 0;
}
.kw  { color: #007cf9; }
.fn  { color: #79c7ff; }
.str { color: #ff9d5c; }
.cm  { color: #2e2e2e; }

/* Insights */
.insights-wrap {
    padding: 1.2rem 1.4rem 1.4rem 1.4rem;
}
.insight-heading {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    color: #ffffff;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 0.8rem;
}
.insight-item {
    display: flex;
    gap: 0.7rem;
    margin-bottom: 0.5rem;
    align-items: flex-start;
}
.insight-dot {
    width: 6px; height: 6px;
    background: #c8ff00;
    border-radius: 50%;
    margin-top: 6px;
    flex-shrink: 0;
}
.insight-text {
    font-size: 0.85rem;
    color: #bbb;
    line-height: 1.6;
}
.implication-box {
    background: #0d1a00;
    border: 1px solid #1a3300;
    border-left: 3px solid #c8ff00;
    border-radius: 8px;
    padding: 0.9rem 1.1rem;
    margin-top: 0.8rem;
}
.implication-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    color: #c8ff00;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 0.4rem;
}
.implication-text {
    font-size: 0.82rem;
    color: #88aa55;
    line-height: 1.6;
}

/* Recommendations */
.rec-card {
    background: #0f0f0f;
    border: 1px solid #1e1e1e;
    border-radius: 12px;
    padding: 1.3rem 1.5rem;
    margin-bottom: 0.8rem;
    display: flex;
    gap: 1rem;
    align-items: flex-start;
}
.rec-num {
    font-family: 'DM Mono', monospace;
    font-size: 1.1rem;
    font-weight: 700;
    color: #c8ff00;
    min-width: 28px;
}
.rec-text {
    font-size: 0.9rem;
    color: #ccc;
    line-height: 1.6;
    padding-top: 2px;
}

/* Footer */
.footer {
    border-top: 1px solid #1a1a1a;
    padding: 1.5rem 0;
    margin-top: 3rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.footer-text {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    color: #333;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# ── Helpers ───────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHARTS = os.path.join(BASE_DIR, "Charts")
# CHARTS = os.path.join(os.path.dirname(Charts, "charts")
def load_img(fname):
    path = os.path.join(CHARTS, fname)
    if os.path.exists(path):
        return Image.open(path)
    return None

def analysis_block(label, title, img_file, sql_html, findings, implication):
    img = load_img(img_file)
    st.markdown(f"""
    <div class="analysis-card">
        <div class="analysis-label">{label}</div>
        <div class="analysis-title">{title}</div>
    </div>
    """, unsafe_allow_html=True)

    col_img, col_right = st.columns([1.4, 1])

    with col_img:
        if img:
            st.image(img, use_container_width=True)
        else:
            st.info("Add chart image to charts/ folder")

    with col_right:
        # SQL
        st.markdown(f"""
        <div class="sql-wrap">
            <div class="sql-title">▸ SQL Query</div>
            <pre class="sql-code">{sql_html}</pre>
        </div>
        """, unsafe_allow_html=True)

        # Insights
        items_html = "".join(
            f'<div class="insight-item"><div class="insight-dot"></div>'
            f'<div class="insight-text">{f}</div></div>'
            for f in findings
        )
        st.markdown(f"""
        <div class="insights-wrap">
            <div class="insight-heading">Key Findings</div>
            {items_html}
            <div class="implication-box">
                <div class="implication-label">Business Implication</div>
                <div class="implication-text">{implication}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:1.5rem 0 1rem 0">
        <div style="font-family:'DM Mono',monospace;font-size:0.6rem;
             color:#c8ff00;letter-spacing:2px;text-transform:uppercase;
             margin-bottom:0.3rem">Portfolio Project</div>
        <div style="font-size:1rem;font-weight:700;color:#f0ece4">
            Sales Insights
        </div>
        <div style="font-family:'DM Mono',monospace;font-size:0.65rem;
             color:#444;margin-top:4px">by Shivang Sharma</div>
    </div>
    <hr style="border-color:#1e1e1e;margin:0 0 1rem 0">
    """, unsafe_allow_html=True)

    section = st.radio(
        "Navigate",
        ["🏠 Overview",
         "🌍 Global Sales",
         "🚗 Product Analysis",
         "📅 Time-Based Analysis",
         "💡 Recommendations"],
        label_visibility="collapsed"
    )

    st.markdown("""
    <hr style="border-color:#1e1e1e;margin:1.5rem 0 1rem 0">
    <div style="font-family:'DM Mono',monospace;font-size:0.62rem;color:#333;
         text-transform:uppercase;letter-spacing:1px;margin-bottom:0.8rem">
        Stack
    </div>
    """, unsafe_allow_html=True)
    for s in ["PostgreSQL", "Power BI", "Python", "Streamlit", "Plotly"]:
        st.markdown(f'<span class="stack-pill">{s}</span>', unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top:2rem;font-family:'DM Mono',monospace;font-size:0.62rem;
         color:#2a2a2a;line-height:1.8">
        Dataset: Classic Models<br>
        Records: 307 orders<br>
        Period: 2003 – 2005
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION: OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
if section == "🏠 Overview":

    st.markdown("""
    <div class="hero">
        <span class="hero-tag">Portfolio Project · SQL + BI</span>
        <h1 class="hero-title">Sales & Customer<br><span>Insights Analysis</span></h1>
        <p class="hero-sub">PostgreSQL · Power BI · Python · Streamlit</p>
        <div style="margin-top:1.2rem">
            <span class="stack-pill">🔗 PostgreSQL Queries</span>
            <span class="stack-pill">📊 Power BI Dashboard</span>
            <span class="stack-pill">🐍 Python + Streamlit</span>
            <span class="stack-pill">📁 GitHub</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # KPI Row
    st.markdown("""
    <div class="kpi-row">
        <div class="kpi-card">
            <div class="kpi-label">Total Revenue</div>
            <div class="kpi-value">$10M</div>
            <div class="kpi-note">3-year combined</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Total Orders</div>
            <div class="kpi-value">307</div>
            <div class="kpi-note">across all customers</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Avg Order Value</div>
            <div class="kpi-value">$32.7K</div>
            <div class="kpi-note">per transaction</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Avg Orders/Customer</div>
            <div class="kpi-value">3.34</div>
            <div class="kpi-note">repeat purchase rate</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Dataset overview slide
    st.markdown("""
    <div class="section-header">
        <span class="section-num">01</span>
        <h2 class="section-title">Dataset Overview</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 1])
    with col1:
        img = load_img("1.png")
        if img:
            st.image(img, use_container_width=True, caption="Raw dataset — Classic Models Sales DB")
    with col2:
        img2 = load_img("1.png")
        if img2:
            st.image(img2, use_container_width=True, caption="KPI Summary")
        st.markdown("""
        <div class="insights-wrap" style="padding:1rem 0">
            <div class="insight-heading">About this Project</div>
            <div class="insight-item"><div class="insight-dot"></div>
                <div class="insight-text">Analyzed 307 orders from a scale model car company (2003–2005)</div></div>
            <div class="insight-item"><div class="insight-dot"></div>
                <div class="insight-text">Wrote PostgreSQL queries covering aggregation, CTEs, window functions, and CASE logic</div></div>
            <div class="insight-item"><div class="insight-dot"></div>
                <div class="insight-text">Built Power BI dashboard with Star Schema and DAX measures</div></div>
            <div class="insight-item"><div class="insight-dot"></div>
                <div class="insight-text">Packaged findings into this interactive Streamlit case study</div></div>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION: GLOBAL SALES
# ══════════════════════════════════════════════════════════════════════════════
elif section == "🌍 Global Sales":

    st.markdown("""
    <div class="section-header">
        <span class="section-num">02</span>
        <h2 class="section-title">Global Sales Analysis</h2>
    </div>
    """, unsafe_allow_html=True)

    analysis_block(
        label="Geography · Revenue",
        title="Revenue by Country",
        img_file="2.png",
        sql_html="""<span class="kw">SELECT</span>
    c.country,
    <span class="fn">SUM</span>(od.quantityordered * od.priceeach) <span class="kw">AS</span> revenue
<span class="kw">FROM</span> customers c
<span class="kw">JOIN</span> orders o
    <span class="kw">ON</span> c.customernumber = o.customernumber
<span class="kw">JOIN</span> orderdetails od
    <span class="kw">ON</span> o.ordernumber = od.ordernumber
<span class="kw">GROUP BY</span> c.country
<span class="kw">ORDER BY</span> revenue <span class="kw">DESC</span>;""",
        findings=[
            "USA is the highest revenue-generating market, significantly outperforming all other countries at $3.6M",
            "Spain and France are the next strongest markets, each generating over $1M in revenue",
            "Several countries show low contribution, indicating untapped growth potential",
        ],
        implication="Focus on retention and upselling in top markets (USA, Spain, France). Increase marketing efforts in underperforming regions."
    )


# ══════════════════════════════════════════════════════════════════════════════
# SECTION: PRODUCT ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif section == "🚗 Product Analysis":

    st.markdown("""
    <div class="section-header">
        <span class="section-num">03</span>
        <h2 class="section-title">Product Analysis</h2>
    </div>
    """, unsafe_allow_html=True)

    analysis_block(
        label="Products · Revenue Share",
        title="Sales by Product Category",
        img_file="3.png",
        sql_html="""<span class="kw">SELECT</span>
    p.productline,
    <span class="fn">SUM</span>(od.quantityordered * od.priceeach) <span class="kw">AS</span> total_sales,
    <span class="fn">ROUND</span>(
        <span class="fn">SUM</span>(od.quantityordered * od.priceeach) * 100.0
        / <span class="fn">SUM</span>(<span class="fn">SUM</span>(od.quantityordered * od.priceeach))
            <span class="kw">OVER</span> (), 2
    ) <span class="kw">AS</span> pct_of_total
<span class="kw">FROM</span> products p
<span class="kw">JOIN</span> orderdetails od
    <span class="kw">ON</span> p.productcode = od.productcode
<span class="kw">GROUP BY</span> p.productline
<span class="kw">ORDER BY</span> total_sales <span class="kw">DESC</span>;""",
        findings=[
            "Classic Cars dominate sales, contributing ~39% of total revenue",
            "Vintage Cars are the second strongest category at ~19%",
            "Other categories (Trains, Ships) show relatively lower performance",
        ],
        implication="Expand inventory and marketing for high-performing product lines. Re-evaluate or reposition low-performing categories."
    )

    analysis_block(
        label="Products · Geography",
        title="Top Product by Country",
        img_file="4.png",
        sql_html="""<span class="kw">WITH</span> ranked <span class="kw">AS</span> (
  <span class="kw">SELECT</span>
    c.country,
    p.productline,
    <span class="fn">SUM</span>(od.quantityordered * od.priceeach) <span class="kw">AS</span> total_sales,
    <span class="fn">RANK</span>() <span class="kw">OVER</span> (
        <span class="kw">PARTITION BY</span> c.country
        <span class="kw">ORDER BY</span> <span class="fn">SUM</span>(od.quantityordered * od.priceeach) <span class="kw">DESC</span>
    ) <span class="kw">AS</span> rk
  <span class="kw">FROM</span> customers c
  <span class="kw">JOIN</span> orders o <span class="kw">ON</span> c.customernumber = o.customernumber
  <span class="kw">JOIN</span> orderdetails od <span class="kw">ON</span> o.ordernumber = od.ordernumber
  <span class="kw">JOIN</span> products p <span class="kw">ON</span> od.productcode = p.productcode
  <span class="kw">GROUP BY</span> c.country, p.productline
)
<span class="kw">SELECT</span> country, productline, total_sales
<span class="kw">FROM</span> ranked
<span class="kw">WHERE</span> rk = 1
<span class="kw">ORDER BY</span> total_sales <span class="kw">DESC</span>;""",
        findings=[
            "Classic Cars are the top-selling category across most countries",
            "Japan shows higher preference for Planes, indicating clear regional variation",
            "This pattern suggests product strategy should not be one-size-fits-all",
        ],
        implication="Implement region-specific product strategies. Customize offerings based on local demand patterns."
    )


# ══════════════════════════════════════════════════════════════════════════════
# SECTION: TIME-BASED ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif section == "📅 Time-Based Analysis":

    st.markdown("""
    <div class="section-header">
        <span class="section-num">04</span>
        <h2 class="section-title">Time-Based Analysis</h2>
    </div>
    """, unsafe_allow_html=True)

    analysis_block(
        label="Seasonality · Monthly",
        title="Monthly Sales Trend",
        img_file="5.png",
        sql_html="""<span class="kw">SELECT</span>
    <span class="fn">TO_CHAR</span>(o.orderdate, <span class="str">'Mon'</span>)      <span class="kw">AS</span> month_name,
    <span class="fn">EXTRACT</span>(<span class="kw">MONTH FROM</span> o.orderdate) <span class="kw">AS</span> month_num,
    <span class="fn">SUM</span>(od.quantityordered * od.priceeach) <span class="kw">AS</span> revenue
<span class="kw">FROM</span> orders o
<span class="kw">JOIN</span> orderdetails od
    <span class="kw">ON</span> o.ordernumber = od.ordernumber
<span class="kw">GROUP BY</span>
    month_name, month_num
<span class="kw">ORDER BY</span> month_num;""",
        findings=[
            "Peak sales occur in May, October, and November — likely driven by seasonal gifting",
            "June shows noticeably lower sales performance across all years",
            "November alone accounts for a disproportionate share of annual revenue",
        ],
        implication="Plan marketing campaigns around high-performing months. Investigate reasons for low sales in June and apply corrective strategies."
    )

    analysis_block(
        label="YoY · Annual",
        title="Revenue Year-over-Year",
        img_file="6.png",
        sql_html="""<span class="kw">SELECT</span>
    <span class="fn">EXTRACT</span>(<span class="kw">YEAR FROM</span> o.orderdate) <span class="kw">AS</span> year_id,
    <span class="fn">SUM</span>(od.quantityordered * od.priceeach) <span class="kw">AS</span> total_revenue,
    <span class="fn">LAG</span>(<span class="fn">SUM</span>(od.quantityordered * od.priceeach))
        <span class="kw">OVER</span> (<span class="kw">ORDER BY</span> <span class="fn">EXTRACT</span>(<span class="kw">YEAR FROM</span> o.orderdate))
                                           <span class="kw">AS</span> prev_year,
    <span class="fn">ROUND</span>(
        (<span class="fn">SUM</span>(od.quantityordered * od.priceeach)
         - <span class="fn">LAG</span>(<span class="fn">SUM</span>(od.quantityordered * od.priceeach))
             <span class="kw">OVER</span> (<span class="kw">ORDER BY</span> <span class="fn">EXTRACT</span>(<span class="kw">YEAR FROM</span> o.orderdate))
        ) * 100.0
        / <span class="fn">NULLIF</span>(<span class="fn">LAG</span>(<span class="fn">SUM</span>(od.quantityordered * od.priceeach))
            <span class="kw">OVER</span> (<span class="kw">ORDER BY</span> <span class="fn">EXTRACT</span>(<span class="kw">YEAR FROM</span> o.orderdate)), 0),
    2) <span class="kw">AS</span> yoy_growth_pct
<span class="kw">FROM</span> orders o
<span class="kw">JOIN</span> orderdetails od
    <span class="kw">ON</span> o.ordernumber = od.ordernumber
<span class="kw">GROUP BY</span> year_id
<span class="kw">ORDER BY</span> year_id;""",
        findings=[
            "Revenue declined significantly from $4.7M in 2004 to $1.8M in 2005",
            "Note: 2005 data only covers Jan–May (partial year), which explains the apparent drop",
            "2004 was the strongest year — peak revenue of $4.7M",
        ],
        implication="Requires further investigation into the cause of decline. Possible focus areas: customer retention, product relevance, and market conditions."
    )


# ══════════════════════════════════════════════════════════════════════════════
# SECTION: RECOMMENDATIONS
# ══════════════════════════════════════════════════════════════════════════════
elif section == "💡 Recommendations":

    st.markdown("""
    <div class="section-header">
        <span class="section-num">05</span>
        <h2 class="section-title">Key Business Recommendations</h2>
    </div>
    """, unsafe_allow_html=True)

    # col_img, col_rec = st.columns([1, 1.2])
    # with col_img:
    #     img = load_img("slide-11.jpg")
    #     if img:
    #         st.image(img, use_container_width=True)

    # with col_rec:
    recs = [
        ("Focus on top markets", "USA, Spain, and France drive the majority of revenue. Retention and upselling strategies should be priority for these markets."),
        ("Strengthen high-demand products", "Classic Cars (~39%) and Vintage Cars (~19%) dominate. Expand inventory and allocate more marketing budget here."),
        ("Region-specific strategies", "Japan prefers Planes over Classic Cars. Tailor product offerings and campaigns based on local demand patterns."),
        ("Improve customer retention", "High-value customers like Euro Shopping Channel (Rank 1) and Mini Gifts (Rank 2) together account for 72% of top-5 revenue. Build loyalty programs."),
        ("Investigate revenue decline", "2005 shows a sharp drop — even accounting for partial-year data. Audit operational changes, pricing, or customer churn in this period."),
        ("Capitalize on seasonal peaks", "Nov–Oct are peak months. Plan campaigns, stock up inventory, and offer promotions ahead of these windows."),
    ]
    for i, (title, text) in enumerate(recs, 1):
        st.markdown(f"""
        <div class="rec-card">
            <div class="rec-num">0{i}</div>
            <div>
                <div style="font-weight:700;color:#f0ece4;font-size:0.9rem;
                        margin-bottom:0.2rem">{title}</div>
                <div class="rec-text">{text}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-text">Shivang Sharma · Data Analyst Portfolio · 2025</div>
    <div class="footer-text">PostgreSQL · Power BI · Python · Streamlit</div>
</div>
""", unsafe_allow_html=True)
