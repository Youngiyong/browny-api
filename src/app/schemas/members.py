from datetime import datetime
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class MemberBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    email: Optional[str]
    sex: Optional[str]
    password: Optional[str]
    phone: Optional[str]
    birthday: Optional[str]
    join_type: Optional[str]
    join_token: Optional[str]
    grade: Optional[str]
    last_login_date: Optional[datetime]
    pw_chage_date: Optional[datetime]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class MemberProfile(BaseModel):
    id: Optional[int]
    member_id: Optional[int]
    name: Optional[str]
    content: Optional[str]
    image: Optional[str]
    facebook: Optional[str]
    instagram: Optional[str]
    github: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class MemberFollow(BaseModel):
    id: Optional[int]
    member_id: Optional[int]
    follow_id: Optional[int]
    memo: Optional[str]
    created_at: Optional[datetime]


class MemberCreate(MemberBase):
    name: Optional[str]
    email: Optional[str]
    sex: Optional[str]
    password: Optional[str]
    phone: Optional[str]
    birthday: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "윤기용",
                "email": "youn9354@naver.com",
                "sex": "M",
                "password": "kim123132132@!#@!",
                "phone": "01092069357",
                "birthday": "1997-05-03",
            }
        }


class MemberCreateResponse(MemberBase):
    id: Optional[int]
    name: Optional[str]
    email: Optional[str]
    sex: Optional[str]
    password: Optional[str]
    phone: Optional[str]
    birthday: Optional[str]
    join_type: Optional[str]
    join_token: Optional[str]
    grade: Optional[str]
    last_login_date: Optional[datetime]
    pw_chage_date: Optional[datetime]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class MemberFollowBase(BaseModel):
    pass


class MemberProfileBase(BaseModel):
    pass


class Member(MemberBase):
    id = int
    member_follows: List[MemberFollow] = []
    member_profiles: List[MemberProfile] = []

    class Config:
        orm_mode = True


class MemberFollowBase(BaseModel):
    id: Optional[int]
    member_id: Optional[int]
    follow_id: Optional[int]
    memo: Optional[str]
    created_at: Optional[datetime]


class MemberFollowCreate(MemberFollowBase):
    member_id: Optional[int]
    follow_id: Optional[int]
    memo: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "member_id": "501021",
                "follow_id": "105901",
                "memo": "memo exmaple"
            }
        }

class MemberFollow(MemberFollowBase):
    id: int

    class Config:
        orm_mode = True


class MemberProfileBase(BaseModel):
    id: Optional[int]
    member_id: Optional[int]
    name: Optional[str]
    image: Optional[str]
    facebook: Optional[str]
    instagram: Optional[str]
    github: Optional[str]
    content: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class MemberProfile(MemberProfileBase):
    id: int

    class Config:
        orm_mode = True


class MemberProfileCreate(MemberProfileBase):
    pass


class MemberProfileUpdate(MemberProfileBase):
    name: Optional[str]
    image: Optional[str]
    facebook: Optional[str]
    instagram: Optional[str]
    github: Optional[str]
    content: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "윤기용",
                "image": "members/21021021012021",
                "facebook": "https://www.facebook.com/youn9354",
                "instagram": "https://www.instagram.com/dev_giyong",
                "github": "https://github.com/Youngiyong",
                "content": "content example"
            }
        }


class MemberFollowUpdate(MemberFollowBase):
    pass

class MemberFollowResponse(MemberFollowBase):
    class Config:
        orm_mode = True


class MemberResponse(MemberBase):
    class Config:
        orm_mode = True
