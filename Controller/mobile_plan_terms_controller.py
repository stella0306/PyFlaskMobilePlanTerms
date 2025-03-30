from flask import Blueprint, request, Response
from Service.Impl.mobile_plan_terms_service_impl import MobilePlanTermsServiceImpl
from Dto.Response.mobile_plan_terms_response_dto import MobilePlanTermsResponseDto
from Dto.Request.mobile_plan_terms_request_dto import MobilePlanTermsRequestDto
from util.json_utils import dumps_json

# 블루프린트 객체 생성
mobile_plan_terms_bp = Blueprint(
    name="mobile_plan_terms", 
    import_name=__name__
    )

# 서비스 객체 생성
mobile_plan_terms_service = MobilePlanTermsServiceImpl()

# 모든 데이터 가져오기
@mobile_plan_terms_bp.route("/search_all", methods=["GET"])
def get_all_mobile_plans_terms():
    mobile_plan_terms = mobile_plan_terms_service.get_all_mobile_plans_terms()

    mobile_plan_terms_dict = [mbt for mbt in mobile_plan_terms] if isinstance(mobile_plan_terms, list) else mobile_plan_terms

    return Response(
        response=dumps_json(mobile_plan_terms_dict if mobile_plan_terms_dict else {}),
        mimetype="application/json",
        status=200
    )

# 이름으로 특정 데이터 가져오기
@mobile_plan_terms_bp.route("/search_by_name/<string:name>", methods=["GET"])
def get_mobile_plan_terms_by_name(name:str):
    mobile_plan_terms = mobile_plan_terms_service.get_mobile_plan_terms_by_name(
        mobile_plan_terms_request_dto=MobilePlanTermsRequestDto(
            id=None, 
            name=name, 
            description=None
            )
    )

    return Response(
        response=dumps_json(mobile_plan_terms if mobile_plan_terms else {}),
        mimetype="application/json",
        status=200
    )

# 이름으로 특정 데이터 가져오기
@mobile_plan_terms_bp.route("/search_by_id/<int:id>", methods=["GET"])
def get_mobile_plan_terms_by_id(id:int):
    mobile_plan_terms = mobile_plan_terms_service.get_mobile_plan_terms_by_id(
        mobile_plan_terms_request_dto=MobilePlanTermsRequestDto(
            id=id, 
            name=None, 
            description=None
            )
    )

    return Response(
        response=dumps_json(mobile_plan_terms if mobile_plan_terms else {}),
        mimetype="application/json",
        status=200
    )


# 데이터 생성
@mobile_plan_terms_bp.route("/create", methods=["POST"])
def create_mobile_plan_terms():
    # 데이터 가져오기
    data = request.get_json()

    mobile_plan_terms = mobile_plan_terms_service.create_mobile_plan_terms(
        mobile_plan_terms_request_dto=MobilePlanTermsRequestDto(
            id=None, 
            name=data.get("name"), 
            description=data.get("description")
            )
    )

    return Response(
        response=dumps_json(mobile_plan_terms if mobile_plan_terms else {}),
        mimetype="application/json",
        status=200
    )


# 데이터 식제
@mobile_plan_terms_bp.route("/delete", methods=["DELETE"])
def delete_mobile_plan_terms():
    # 데이터 가져오기
    data = request.get_json()

    mobile_plan_terms = mobile_plan_terms_service.delete_mobile_plan_terms(
        mobile_plan_terms_request_dto=MobilePlanTermsRequestDto(
            id=data.get("id"), 
            name=None, 
            description=None
            )
    )

    return Response(
        response=dumps_json(mobile_plan_terms if mobile_plan_terms else {}),
        mimetype="application/json",
        status=200
    )