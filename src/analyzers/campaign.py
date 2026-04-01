"""Campaign Performance Analyzer - วิเคราะห์ประสิทธิภาพแคมเปญ"""

import pandas as pd
from dataclasses import dataclass


@dataclass
class CampaignMetrics:
    impressions: int
    clicks: int
    conversions: int
    spend: float
    revenue: float

    @property
    def ctr(self) -> float:
        return (self.clicks / self.impressions * 100) if self.impressions else 0

    @property
    def cpc(self) -> float:
        return (self.spend / self.clicks) if self.clicks else 0

    @property
    def cpa(self) -> float:
        return (self.spend / self.conversions) if self.conversions else 0

    @property
    def roas(self) -> float:
        return (self.revenue / self.spend) if self.spend else 0

    @property
    def conversion_rate(self) -> float:
        return (self.conversions / self.clicks * 100) if self.clicks else 0


class CampaignAnalyzer:
    def __init__(self, config: dict):
        self.config = config
        self.platforms = config.get("platforms", {})

    def analyze(self) -> dict:
        results = {}
        for platform in self.platforms:
            print(f"  วิเคราะห์แคมเปญจาก {platform}...")
            results[platform] = self._analyze_platform(platform)
        return results

    def _analyze_platform(self, platform: str) -> dict:
        # TODO: เชื่อมต่อ API จริงของแต่ละ platform
        return {
            "platform": platform,
            "campaigns": [],
            "summary": {},
        }

    def compare_platforms(self, results: dict) -> pd.DataFrame:
        rows = []
        for platform, data in results.items():
            if "summary" in data:
                rows.append({"platform": platform, **data["summary"]})
        return pd.DataFrame(rows)
