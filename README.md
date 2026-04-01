# Marketing Analysis Track

ระบบวิเคราะห์การตลาดบน Platform Online

## โครงสร้างโปรเจกต์

```
marketing-analysis-track/
├── data/
│   ├── raw/              # ข้อมูลดิบจาก platforms
│   └── processed/        # ข้อมูลที่ผ่านการ clean แล้ว
├── notebooks/            # Jupyter notebooks สำหรับ EDA
├── src/
│   ├── collectors/       # เก็บข้อมูลจาก platforms (Facebook, Google, TikTok, etc.)
│   ├── analyzers/        # วิเคราะห์ข้อมูลการตลาด
│   └── reports/          # สร้างรายงานอัตโนมัติ
├── dashboards/           # Dashboard templates
└── configs/              # ไฟล์ config สำหรับแต่ละ platform
```

## ฟีเจอร์หลัก

- **Data Collection** - ดึงข้อมูลจาก Facebook Ads, Google Ads, TikTok Ads, LINE OA
- **Campaign Analysis** - วิเคราะห์ประสิทธิภาพแคมเปญ (CTR, CPC, ROAS, Conversion Rate)
- **Audience Insights** - วิเคราะห์กลุ่มเป้าหมาย, Demographics, Behavior
- **Content Performance** - วิเคราะห์ประสิทธิภาพคอนเทนต์แต่ละประเภท
- **Competitor Analysis** - เปรียบเทียบกับคู่แข่ง
- **Automated Reports** - สร้างรายงานสรุปอัตโนมัติ

## Platforms ที่รองรับ

| Platform | Data Collection | Analysis | Dashboard |
|----------|:-:|:-:|:-:|
| Facebook Ads | ✅ | ✅ | ✅ |
| Google Ads | ✅ | ✅ | ✅ |
| TikTok Ads | ✅ | ✅ | ✅ |
| LINE OA | ✅ | ✅ | ✅ |
| Shopee | ✅ | ✅ | ⬜ |
| Lazada | ✅ | ✅ | ⬜ |

## เริ่มต้นใช้งาน

```bash
pip install -r requirements.txt
cp configs/config.example.yaml configs/config.yaml
# แก้ไข config.yaml ใส่ API keys ของแต่ละ platform
python src/main.py
```

## Tech Stack

- **Python 3.10+**
- **Pandas / Polars** - Data processing
- **Plotly / Streamlit** - Visualization & Dashboard
- **SQLite / PostgreSQL** - Data storage
