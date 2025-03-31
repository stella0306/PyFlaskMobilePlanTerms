from dataclasses import dataclass
from config.database import db


# 데이터베이스 Entity
@dataclass
class MobilePlanTermMembersEntity(db.Model):
    __tablename__ = "mobile_plan_members" # 테이블 이름

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 고유 ID
    username: str = db.Column(db.String(100), nullable=False)  # 필수
    password: str = db.Column(db.String(200), nullable=False)  # 필수
    api_key: str = db.Column(db.String(200), nullable=True)  # 선택적
    role: str = db.Column(db.String(200), nullable=False)  # 필수