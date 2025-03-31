from Entity.mobile_plan_term_members_entity import MobilePlanTermMembersEntity
from config.database import db

# DB 통신 객체
class MobilePlanTermMembersRepository:
    # 모든 데이터 반환
    @staticmethod
    def find_all():
        return MobilePlanTermMembersEntity.query.all()
    
    # 이름으로 특정된 데이터 반환
    @staticmethod
    def find_by_name(mobile_plan_term_members_entity: MobilePlanTermMembersEntity):
        return MobilePlanTermMembersEntity.query.filter_by(username=mobile_plan_term_members_entity.username).first()

    # ID으로 특정된 데이터 반환
    @staticmethod
    def find_by_id(mobile_plan_term_members_entity: MobilePlanTermMembersEntity):
        return MobilePlanTermMembersEntity.query.filter_by(id=mobile_plan_term_members_entity.id).first()

    # API_KEY으로 특정된 데이터 반환
    @staticmethod
    def find_by_api_key(mobile_plan_term_members_entity: MobilePlanTermMembersEntity):
        return MobilePlanTermMembersEntity.query.filter_by(api_key=mobile_plan_term_members_entity.api_key).first()

    # 데이터 저장
    @staticmethod
    def save(mobile_plan_term_members_entity: MobilePlanTermMembersEntity):
        db.session.add(mobile_plan_term_members_entity)
        db.session.commit()

    # 데이터 삭제
    @staticmethod
    def delete(mobile_plan_term_members_entity: MobilePlanTermMembersEntity):
        db.session.delete(mobile_plan_term_members_entity)
        db.session.commit()