"""Marketing Analysis Track - Main Entry Point"""

import yaml
from pathlib import Path
from analyzers.campaign import CampaignAnalyzer
from analyzers.audience import AudienceAnalyzer
from analyzers.content import ContentAnalyzer
from reports.generator import ReportGenerator


def load_config(config_path: str = "configs/config.yaml") -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    config = load_config()
    print("=" * 50)
    print("  Marketing Analysis Track")
    print("  วิเคราะห์การตลาดบน Platform Online")
    print("=" * 50)

    # วิเคราะห์แคมเปญ
    campaign = CampaignAnalyzer(config)
    campaign_results = campaign.analyze()

    # วิเคราะห์กลุ่มเป้าหมาย
    audience = AudienceAnalyzer(config)
    audience_results = audience.analyze()

    # วิเคราะห์คอนเทนต์
    content = ContentAnalyzer(config)
    content_results = content.analyze()

    # สร้างรายงาน
    report = ReportGenerator(config)
    report.generate(
        campaign=campaign_results,
        audience=audience_results,
        content=content_results,
    )

    print("\nสร้างรายงานเสร็จสิ้น!")


if __name__ == "__main__":
    main()
