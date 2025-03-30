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
    """
    모든 모바일 요금제 용어 데이터 조회 API
    ---
    tags:
      - Mobile Plan Terms
    responses:
      200:
        description: 모든 모바일 요금제 용어 데이터 목록
    """

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
    """
    이름으로 특정 모바일 요금제 용어 데이터 조회 API
    ---
    tags:
      - Mobile Plan Terms
    parameters:
      - name: name
        in: path
        type: string
        required: true
        description: 조회할 모바일 요금제 용어 이름
    responses:
      200:
        description: 조회된 모바일 요금제 용어 정보
    """
    
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

# ID으로 특정 데이터 가져오기
@mobile_plan_terms_bp.route("/search_by_id/<int:id>", methods=["GET"])
def get_mobile_plan_terms_by_id(id:int):
    """
    ID으로 특정 모바일 요금제 용어 데이터 조회 API
    ---
    tags:
      - Mobile Plan Terms
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: 조회할 모바일 요금제 용어 ID
    responses:
      200:
        description: 조회된 모바일 요금제 용어 정보
    """

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
    """
    모바일 요금제 용어 정보 생성 API
    ---
    tags:
      - Mobile Plan Terms
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            name:
              type: string
              description: 용어 이름
              required: true
            description:
              type: string
              description: 용어 설명
              required: true
    responses:
      200:
        description: 생성된 모바일 요금제 용어 정보
        schema:
          type: object
          properties:
            id:
              type: integer
              description: 생성된 용어 ID
            name:
              type: string
              description: 생성된 용어 이름
            description:
              type: string
              description: 생성된 용어 설명
    """

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
    """
    모바일 요금제 용어 정보 삭제 API
    ---
    tags:
      - Mobile Plan Terms
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            id:
              type: integer
              description: 용어 ID
              required: true
    responses:
      200:
        description: 삭제된 모바일 요금제 용어 정보
        schema:
          type: object
          properties:
            message:
              type: string
              description: 삭제 여부
    """
    
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