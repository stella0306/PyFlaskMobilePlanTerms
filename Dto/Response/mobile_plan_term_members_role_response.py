from dataclasses import dataclass

# 응답 객체
@dataclass
class MobilePlanTermMembersRoleResponseDto:
    is_access: bool # 불리언 타입으로 접근
    role: str # 권한