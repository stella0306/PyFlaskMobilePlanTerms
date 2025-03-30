from dataclasses import dataclass

# 요청 객체
@dataclass
class MobilePlanTermsRequestDto:
    id: int # 데이터 고유 ID
    name: str # 데이터 이름
    description: str # 데이터 설명