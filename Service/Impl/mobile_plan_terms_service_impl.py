from Service.mobile_plan_terms_service import MobilePlanTermsService
from Dto.Request.mobile_plan_terms_request_dto import MobilePlanTermsRequestDto
from Dto.Response.mobile_plan_terms_response_dto import MobilePlanTermsResponseDto
from Repository.mobile_plan_terms_repository import MobilePlanTermsRepository
from Entity.mobile_plan_terms_entity import MobilePlanTermsEntity
from dataclasses import asdict

# MobilePlanTermsService 추상 클래스의 실제 기능 구현
class MobilePlanTermsServiceImpl(MobilePlanTermsService):
    def __init__(self):
        # DB 통신 객체 생성
        self.mobile_plan_terms_respository = MobilePlanTermsRepository()


    # 모든 데이터 가져오기
    def get_all_mobile_plans_terms(self):
        mobile_plan_terms_respository = self.mobile_plan_terms_respository.find_all()

        # 데이터가 없을 때
        if mobile_plan_terms_respository:
            return [
            asdict(
                MobilePlanTermsResponseDto(
                    id=mpt.id,
                    name=mpt.name, 
                    description=mpt.description
                    )
                )

                    for mpt in mobile_plan_terms_respository
                ]

        else:
            return {"message": "데이터가 없습니다."}
    

    # 이름으로 특정 데이터 가져오기
    def get_mobile_plan_terms_by_name(self, mobile_plan_terms_request_dto: MobilePlanTermsRequestDto):
        mobile_plan_terms_respository = self.mobile_plan_terms_respository.find_by_name(
            mobile_plan_terms_entity = MobilePlanTermsEntity(
                **asdict(mobile_plan_terms_request_dto)
                )
            )
        
        if not mobile_plan_terms_respository:
            return {"message": "이름으로 데이터를 찾을 수 없습니다."}
        
        return asdict(
            MobilePlanTermsResponseDto(
                id=mobile_plan_terms_respository.id,
                name=mobile_plan_terms_respository.name,
                description=mobile_plan_terms_respository.description
            )
        )


    # ID으로 특정 데이터 가져오기
    def get_mobile_plan_terms_by_id(self, mobile_plan_terms_request_dto: MobilePlanTermsRequestDto):
        mobile_plan_terms_respository = self.mobile_plan_terms_respository.find_by_id(
            mobile_plan_terms_entity = MobilePlanTermsEntity(
                **asdict(mobile_plan_terms_request_dto)
                )
            )
        
        if not mobile_plan_terms_respository:
            return {"message": "ID으로 데이터를 찾을 수 없습니다."}
        
        return asdict(
            MobilePlanTermsResponseDto(
                id=mobile_plan_terms_respository.id,
                name=mobile_plan_terms_respository.name,
                description=mobile_plan_terms_respository.description
                )
        )


    # 데이터 생성
    def create_mobile_plan_terms(self, mobile_plan_terms_request_dto: MobilePlanTermsRequestDto):
        mobile_plan_terms_respository = self.mobile_plan_terms_respository.find_by_name(
            mobile_plan_terms_entity = MobilePlanTermsEntity(
                **asdict(mobile_plan_terms_request_dto)
                )
            )
        
        if mobile_plan_terms_respository:
            return {"message": "이미 존재하는 데이터입니다."}
        
        mobile_plan_terms_entity = MobilePlanTermsEntity(
            name=mobile_plan_terms_request_dto.name,
            description=mobile_plan_terms_request_dto.description
        )
        self.mobile_plan_terms_respository.save(mobile_plan_terms_entity=mobile_plan_terms_entity)

        return asdict(
            MobilePlanTermsResponseDto(
                id=mobile_plan_terms_entity.id,
                name=mobile_plan_terms_entity.name,
                description=mobile_plan_terms_entity.description
                )
        )
    

    # 데이터 삭제
    def delete_mobile_plan_terms(self, mobile_plan_terms_request_dto: MobilePlanTermsRequestDto):
        mobile_plan_terms_respository = self.mobile_plan_terms_respository.find_by_id(
            mobile_plan_terms_entity = MobilePlanTermsEntity(
                **asdict(mobile_plan_terms_request_dto)
                )
            )
        
        if not mobile_plan_terms_respository:
            return {"message": "데이터를 찾을 수 없습니다."}

        self.mobile_plan_terms_respository.delete(
            mobile_plan_terms_entity=mobile_plan_terms_respository
            )

        return {"message": "데이터가 삭제 됐습니다."}