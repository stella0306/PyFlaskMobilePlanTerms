from dataclasses import dataclass

# 응답 객체
@dataclass
class MobilePlanTermMembersResponseDto:
    id: int # 계정 고유 ID
    username: str # 계정 ID 
    password: str # 계정 비밀번호
    api_key: str # 데이터 생성/삭제 api key
    role: str # 권한 api_key 여부에 따라 default, admin으로 나눠 짐