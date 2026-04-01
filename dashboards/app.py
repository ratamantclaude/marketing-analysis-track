"""Marketing Analysis Dashboard - Streamlit App"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

st.set_page_config(
    page_title="Marketing Analysis Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Marketing Analysis Dashboard")
st.caption("วิเคราะห์การตลาดบน Platform Online")


# --- สร้าง Demo Data ---
@st.cache_data
def generate_demo_data():
    dates = pd.date_range(end=datetime.now(), periods=30, freq="D")
    platforms = ["Facebook Ads", "Google Ads", "TikTok Ads", "LINE OA"]
    rows = []
    for date in dates:
        for platform in platforms:
            base = {"Facebook Ads": 1.0, "Google Ads": 1.2, "TikTok Ads": 0.8, "LINE OA": 0.6}
            scale = base[platform]
            impressions = int(random.gauss(10000, 2000) * scale)
            clicks = int(impressions * random.uniform(0.02, 0.06))
            conversions = int(clicks * random.uniform(0.03, 0.10))
            spend = round(clicks * random.uniform(5, 15), 2)
            revenue = round(conversions * random.uniform(200, 800), 2)
            rows.append({
                "date": date,
                "platform": platform,
                "impressions": max(impressions, 0),
                "clicks": max(clicks, 0),
                "conversions": max(conversions, 0),
                "spend": spend,
                "revenue": revenue,
            })
    return pd.DataFrame(rows)


df = generate_demo_data()

# --- Sidebar Filters ---
st.sidebar.header("ตัวกรอง")
selected_platforms = st.sidebar.multiselect(
    "เลือก Platform",
    options=df["platform"].unique(),
    default=df["platform"].unique(),
)
date_range = st.sidebar.date_input(
    "ช่วงวันที่",
    value=(df["date"].min(), df["date"].max()),
)

if len(date_range) == 2:
    mask = (
        df["platform"].isin(selected_platforms)
        & (df["date"] >= pd.Timestamp(date_range[0]))
        & (df["date"] <= pd.Timestamp(date_range[1]))
    )
    filtered = df[mask]
else:
    filtered = df[df["platform"].isin(selected_platforms)]

# --- KPI Cards ---
st.subheader("ภาพรวม")
total = filtered.agg({
    "impressions": "sum",
    "clicks": "sum",
    "conversions": "sum",
    "spend": "sum",
    "revenue": "sum",
})

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Impressions", f"{total['impressions']:,.0f}")
col2.metric("Clicks", f"{total['clicks']:,.0f}")
col3.metric("Conversions", f"{total['conversions']:,.0f}")
col4.metric("Spend (THB)", f"฿{total['spend']:,.0f}")
col5.metric("Revenue (THB)", f"฿{total['revenue']:,.0f}")

ctr = (total["clicks"] / total["impressions"] * 100) if total["impressions"] else 0
cpc = (total["spend"] / total["clicks"]) if total["clicks"] else 0
roas = (total["revenue"] / total["spend"]) if total["spend"] else 0

col6, col7, col8 = st.columns(3)
col6.metric("CTR", f"{ctr:.2f}%")
col7.metric("CPC", f"฿{cpc:.2f}")
col8.metric("ROAS", f"{roas:.2f}x")

st.divider()

# --- Charts ---
left, right = st.columns(2)

with left:
    st.subheader("Spend & Revenue ตาม Platform")
    platform_summary = filtered.groupby("platform").agg({"spend": "sum", "revenue": "sum"}).reset_index()
    fig1 = px.bar(
        platform_summary,
        x="platform",
        y=["spend", "revenue"],
        barmode="group",
        labels={"value": "THB", "variable": ""},
        color_discrete_map={"spend": "#ef553b", "revenue": "#636efa"},
    )
    st.plotly_chart(fig1, use_container_width=True)

with right:
    st.subheader("สัดส่วน Spend ตาม Platform")
    fig2 = px.pie(
        platform_summary,
        values="spend",
        names="platform",
    )
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("แนวโน้มรายวัน")
daily = filtered.groupby(["date", "platform"]).agg({"clicks": "sum", "conversions": "sum", "spend": "sum"}).reset_index()

tab1, tab2, tab3 = st.tabs(["Clicks", "Conversions", "Spend"])

with tab1:
    fig3 = px.line(daily, x="date", y="clicks", color="platform", markers=True)
    st.plotly_chart(fig3, use_container_width=True)

with tab2:
    fig4 = px.line(daily, x="date", y="conversions", color="platform", markers=True)
    st.plotly_chart(fig4, use_container_width=True)

with tab3:
    fig5 = px.line(daily, x="date", y="spend", color="platform", markers=True)
    st.plotly_chart(fig5, use_container_width=True)

# --- Platform Comparison Table ---
st.subheader("เปรียบเทียบ Platform")
comparison = filtered.groupby("platform").agg({
    "impressions": "sum",
    "clicks": "sum",
    "conversions": "sum",
    "spend": "sum",
    "revenue": "sum",
}).reset_index()
comparison["CTR (%)"] = (comparison["clicks"] / comparison["impressions"] * 100).round(2)
comparison["CPC (฿)"] = (comparison["spend"] / comparison["clicks"]).round(2)
comparison["ROAS"] = (comparison["revenue"] / comparison["spend"]).round(2)
comparison["Conv Rate (%)"] = (comparison["conversions"] / comparison["clicks"] * 100).round(2)

st.dataframe(
    comparison[["platform", "impressions", "clicks", "conversions", "spend", "revenue", "CTR (%)", "CPC (฿)", "ROAS", "Conv Rate (%)"]],
    use_container_width=True,
    hide_index=True,
)

st.divider()
st.caption("📌 ข้อมูลเป็น Demo Data สำหรับทดสอบ — เชื่อมต่อ API จริงได้ผ่าน configs/config.yaml")
