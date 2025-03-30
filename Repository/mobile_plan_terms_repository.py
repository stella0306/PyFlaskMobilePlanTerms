from Entity.mobile_plan_terms_entity import MobilePlanTermsEntity
from config.database import db

# DB 통신 객체
class MobilePlanTermsRepository:
    # 모든 데이터 반환
    @staticmethod
    def find_all():
        return MobilePlanTermsEntity.query.all()
    
    # 이름으로 특정된 데이터 반환
    @staticmethod
    def find_by_name(mobile_plan_terms_entity: MobilePlanTermsEntity):
        return MobilePlanTermsEntity.query.filter_by(name=mobile_plan_terms_entity.name).first()

    # ID으로 특정된 데이터 반환
    @staticmethod
    def find_by_id(mobile_plan_terms_entity: MobilePlanTermsEntity):
        return MobilePlanTermsEntity.query.filter_by(id=mobile_plan_terms_entity.id).first()

    # 데이터 저장
    @staticmethod
    def save(mobile_plan_terms_entity: MobilePlanTermsEntity):
        db.session.add(mobile_plan_terms_entity)
        db.session.commit()

    # 데이터 삭제
    @staticmethod
    def delete(mobile_plan_terms_entity: MobilePlanTermsEntity):
        db.session.delete(mobile_plan_terms_entity)
        db.session.commit()