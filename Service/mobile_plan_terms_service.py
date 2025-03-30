from abc import ABC, abstractmethod
from Dto.Request.mobile_plan_terms_request_dto import MobilePlanTermsRequestDto

# 비즈니스 추상 클래스
class MobilePlanTermsService(ABC):
    # 모든 데이터 가져오기
    @abstractmethod
    def get_all_mobile_plans_terms(self):
        pass
    
    # 이름으로 특정 데이터 가져오기
    @abstractmethod
    def get_mobile_plan_terms_by_name(self, mobile_plan_terms_request_dto: MobilePlanTermsRequestDto):
        pass

    # ID으로 특정 데이터 가져오기
    @abstractmethod
    def get_mobile_plan_terms_by_id(self, mobile_plan_terms_request_dto: MobilePlanTermsRequestDto):
        pass

    # 데이터 생성
    @abstractmethod
    def create_mobile_plan_terms(self, mobile_plan_terms_request_dto: MobilePlanTermsRequestDto):
        pass

    # 데이터 삭제
    @abstractmethod
    def delete_mobile_plan_terms(self, mobile_plan_terms_request_dto: MobilePlanTermsRequestDto):
        pass