from dataclasses import dataclass
from config.database import db


# 데이터베이스 Entity
@dataclass
class MobilePlanTermsEntity(db.Model):
    __tablename__ = "mobile_plans" # 테이블 이름

    # 데이터 고유 ID 변수, 정수형 인덱스 자동 증가
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 데이터 이름 변수, 문자열 길이를 100으로 제한, Null을 허용하지 않음
    name = db.Column(db.String(100), nullable=False)

    # 데이터 설명 변수, 문자열 길이를 200으로 제한, Null을 허용하지 않음.
    description = db.Column(db.String(200), nullable=False)
