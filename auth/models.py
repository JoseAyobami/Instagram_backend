from sqlalchemy import Column, Date, DateTime, Integer, String, Enum, ForeignKey
from datetime import datetime, timezone

from ..database import Base
from .enums import Gender
class User(Base):
    __tablename__ = "users"

    # basics details
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    name = Column(String)
    hashed_password = Column(String, nullable=False)
    created_ht = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


    # profile
    dob = Column(Date)
    gender = Column(Enum(Gender))
    profile_pic = Column(String)  # Link stored to our dp
    bio = Column(String)
    location = Column(String)

    