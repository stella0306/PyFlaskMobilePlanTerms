from Service.mobile_plan_term_members_service import MobilePlanTermMembersService
from Dto.Request.mobile_plan_term_members_request_dto import MobilePlanTermMembersRequestDto
from Dto.Response.mobile_plan_term_members_response_dto import MobilePlanTermMembersResponseDto
from Repository.mobile_plan_term_members_repository import MobilePlanTermMembersRepository
from Entity.mobile_plan_term_members_entity import MobilePlanTermMembersEntity
from config.database import ADMIN_API_KEY
from dataclasses import asdict
from enum import Enum

# 사용자 권한
class MobilePlanTermMembersRole(Enum):
    DEFAULT = "default"  # 기본
    ADMIN = "admin"  # 관리자


# MobilePlanTermMembersService 추상 클래스의 실제 기능 구현
class MobilePlanTermMembersServiceImpl(MobilePlanTermMembersService):
    def __init__(self):
        # DB 통신 객체 생성
        self.mobile_plan_term_members_respository = MobilePlanTermMembersRepository()

    # 모바일 요금제 용어 접근 사용자 계정 생성
    def account_create_mobile_plan_term_members(self, mobile_plan_term_members_request_dto: MobilePlanTermMembersRequestDto):
        mobile_plan_term_members_respository = self.mobile_plan_term_members_respository.find_by_name(
            mobile_plan_term_members_entity = MobilePlanTermMembersEntity(
                **asdict(mobile_plan_term_members_request_dto)
                )
            )
        
        if mobile_plan_term_members_respository:
            return {"message": f"이미 존재하는 사용자({mobile_plan_term_members_request_dto.username}) 입니다."}
        
        # 사용자 권한 정의
        # 후에 token의 관한 여러 예외처리를 적용할 것.
        role = MobilePlanTermMembersRole.ADMIN.value if mobile_plan_term_members_request_dto.api_key == ADMIN_API_KEY else MobilePlanTermMembersRole.DEFAULT.value

        mobile_plan_term_members_entity = MobilePlanTermMembersEntity(
            username=mobile_plan_term_members_request_dto.username,
            password=mobile_plan_term_members_request_dto.password,
            api_key=mobile_plan_term_members_request_dto.api_key,
            role=role
        )
        self.mobile_plan_term_members_respository.save(mobile_plan_term_members_entity=mobile_plan_term_members_entity)

        return asdict(
            MobilePlanTermMembersResponseDto(
                id=mobile_plan_term_members_entity.id,
                username=mobile_plan_term_members_entity.username,
                password=mobile_plan_term_members_entity.password,
                api_key=mobile_plan_term_members_entity.api_key,
                role=role
                )
        )

    # 모바일 요금제 용어 접근 사용자 계정 삭제
    def account_delete_mobile_plan_term_members(self, mobile_plan_term_members_request_dto: MobilePlanTermMembersRequestDto):
        pass

    # 모바일 요금제 용어 접근 사용자 계정 로그인
    def account_login_mobile_plan_term_members(self, mobile_plan_term_members_request_dto: MobilePlanTermMembersRequestDto):
        pass
    