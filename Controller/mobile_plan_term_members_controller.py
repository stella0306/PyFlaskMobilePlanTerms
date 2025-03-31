from flask import Blueprint, request, Response
from Service.Impl.mobile_plan_term_members_service_impl import MobilePlanTermMembersServiceImpl
from Dto.Response.mobile_plan_term_members_response_dto import MobilePlanTermMembersResponseDto
from Dto.Response.mobile_plan_term_members_role_response import MobilePlanTermMembersRoleResponseDto
from Dto.Request.mobile_plan_term_members_request_dto import MobilePlanTermMembersRequestDto
from util.json_utils import dumps_json

# 블루프린트 객체 생성
mobile_plan_term_members_bp = Blueprint(
    name="mobile_plan_term_members", 
    import_name=__name__
    )

# 서비스 객체 생성
mobile_plan_term_members_service = MobilePlanTermMembersServiceImpl()

# 사용자 계정 생성
@mobile_plan_term_members_bp.route("/account/create", methods=["POST"])
def account_create_mobile_plan_term_members():
    """
    Swagger UI
    설명란
    """

    # 데이터 가져오기
    data = request.get_json()

    # API_KEY 가져오기
    api_key = request.headers.get("X-API-KEY")

    mobile_plan_term_members = mobile_plan_term_members_service.account_create_mobile_plan_term_members(
        mobile_plan_term_members_request_dto=MobilePlanTermMembersRequestDto(
            id=None, 
            username=data.get("username"), 
            password=data.get("password"),
            api_key=api_key
            )
    )

    return Response(
        response=dumps_json(mobile_plan_term_members if mobile_plan_term_members else {}),
        mimetype="application/json",
        status=200
    )

# 사용자 계정 삭제
@mobile_plan_term_members_bp.route("/account/delete", methods=["DELETE"])
def account_delete_mobile_plan_term_members():
    return "준비중 입니다."

# 사용자 계정 로그인
@mobile_plan_term_members_bp.route("/account/login", methods=["POST"])
def account_login_mobile_plan_term_members():
    return "준비중 입니다."