
from sqlalchemy import MetaData, Column, Integer, String, LargeBinary, ForeignKey, DateTime, func, UniqueConstraint
from sqlalchemy.orm import relationship
from .database import Base

metadata = MetaData()


class User(Base):
    __tablename__ = 'User'
    metadata,
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    passwords = relationship("Password", back_populates="owner")

class Password(Base):
    __tablename__ = 'Password'
    metadata,
    password_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    service_name = Column(String(255), nullable=False)
    encrypted_service_password = Column(LargeBinary, nullable=False)
    salt = Column(LargeBinary, nullable=False)
    iv = Column(LargeBinary, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    owner = relationship("User", back_populates="passwords")

    __table_args__ = (
        UniqueConstraint('user_id', 'service_name', name='uix_user_service'),
    )
