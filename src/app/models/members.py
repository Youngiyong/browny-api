
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func, Text
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class Members(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50), nullable=False)
    email = Column(String(length=50), nullable=False)
    sex = Column(String(length=1), nullable=True)
    password = Column(String(length=100), nullable=True)
    phone = Column(String(length=100), nullable=False)
    birthday = Column(String(length=10), nullable=False)
    grade = Column(String(length=10), nullable=True, default="user")
    join_type = Column(String(length=30), nullable=True)
    join_token = Column(String(length=255), nullable=True)
    pw_chage_date = Column(DateTime, nullable=True, default=func.utc_timestamp())
    last_login_date = Column(DateTime, nullable=True, default=func.utc_timestamp())
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    # member_follows = relationship("MemberFollows", back_populates="members")
    # member_profiles = relationship("MemberProfiles", back_populates="members")


class MemberFollows(Base):
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("members.id"))
    follow_id = Column(Integer, nullable=False)
    memo = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    # members = relationship("Members", back_populates="member_follows")
    __tablename__ = "member_follows"


class MemberProfiles(Base):
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("members.id"))
    name = Column(String(length=30), nullable=True)
    image = Column(String(length=100), nullable=True)
    content = Column(Text, nullable=True)
    facebook = Column(String(length=100), nullable=True)
    instagram = Column(String(length=100), nullable=True)
    github = Column(String(length=100), nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    # members = relationship("Members", back_populates="member_profiles")
    __tablename__ = "member_profiles"
