from abc import ABC, abstractmethod
from Dto.Request.mobile_plan_term_members_request_dto import MobilePlanTermMembersRequestDto

# 비즈니스 추상 클래스
class MobilePlanTermMembersService(ABC):
    # 모바일 요금제 용어 접근 사용자 계정 생성
    @abstractmethod
    def account_create_mobile_plan_term_members(mobile_plan_term_members_request_dto: MobilePlanTermMembersRequestDto):
        pass

    # 모바일 요금제 용어 접근 사용자 계정 삭제
    @abstractmethod
    def account_delete_mobile_plan_term_members(mobile_plan_term_members_request_dto: MobilePlanTermMembersRequestDto):
        pass

    # 모바일 요금제 용어 접근 사용자 계정 로그인
    @abstractmethod
    def account_login_mobile_plan_term_members(mobile_plan_term_members_request_dto: MobilePlanTermMembersRequestDto):
        pass