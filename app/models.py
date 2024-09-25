from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# ORM 모델 자체는 비동기적 특성이 없으므로 변경 불필요
class Team(Base):
    __tablename__ = 'team'

    t_id = Column(Integer, primary_key=True, autoincrement=True)
    t_name = Column(String(255), unique=True, nullable=False)
    t_intro = Column(Text)
    t_descript = Column(Text)
    t_logo = Column(String(255))
    t_git = Column(String(255))

    users = relationship("User", back_populates="team")

class User(Base):
    __tablename__ = 'user'

    u_id = Column(Integer, primary_key=True, autoincrement=True)
    t_id = Column(Integer, ForeignKey('team.t_id'))
    u_name = Column(String(255), nullable=False)
    u_nickname = Column(String(255), nullable=False)
    u_email = Column(String(255), unique=True)
    u_git = Column(String(255))
    u_html = Column(Text)
    u_css = Column(Text)
    u_image = Column(String(255))
    team = relationship("Team", back_populates="users")
    






