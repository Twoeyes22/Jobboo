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
    upload_file = relationship("UploadFile", back_populates="team", uselist=False)

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
    
    upload_file = relationship("UploadFile", back_populates="user", uselist=False)


# 주요 변경사항: 없음
# ORM 모델 정의는 동기/비동기와 관계없이 동일



# Todo: 업로드 파일 미구현
# class UploadFile(Base):
#     __tablename__ = 'upload_file'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     upload_folder = Column(String(255))
#     upload_path = Column(String(255))
#     client_file_name = Column(String(255))
#     ext_file_name = Column(String(50))
#     file_type = Column(String(50))
#     server_file_name = Column(String(255))
#     full_path = Column(String(255))

#     # 팀 또는 유저와의 1:1 관계
#     team_id = Column(Integer, ForeignKey('team.t_id', ondelete="SET NULL"), unique=True, nullable=True)
#     user_id = Column(Integer, ForeignKey('user.u_id', ondelete="SET NULL"), unique=True, nullable=True)

#     # 양방향 관계 설정
#     team = relationship("Team", back_populates="upload_file")
#     user = relationship("User", back_populates="upload_file")


