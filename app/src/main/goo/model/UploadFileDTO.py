import os
import uuid
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import aiofiles


class FileType(str):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"

# Python의 DTO 클래스
class UploadFileDTO(BaseModel):
    upload_folder: Optional[str] = None
    upload_path: Optional[str] = None
    client_file_name: Optional[str] = None
    ext_file_name: Optional[str] = None
    file_type: Optional[FileType] = None
    server_file_name: Optional[str] = None
    full_path: Optional[str] = None
    
    # 유저 또는 팀과 연결을 위한 필드 추가
    team_id: Optional[int] = None
    user_id: Optional[int] = None

    # 엔티티에서 DTO로 변환
    @classmethod
    def entity_to_dto(cls, upload_file):
        return cls(
            upload_folder=upload_file.upload_folder,
            upload_path=upload_file.upload_path,
            client_file_name=upload_file.client_file_name,
            ext_file_name=upload_file.ext_file_name,
            file_type=upload_file.file_type,
            server_file_name=upload_file.server_file_name,
            full_path=upload_file.full_path,
            team_id=upload_file.team_id,
            user_id=upload_file.user_id
        )

    # DTO를 생성하고 파일을 저장하는 로직
    @classmethod
    async def create_upload_file_dto(cls, upload_folder: str, file, file_type: FileType, team_id: Optional[int] = None, user_id: Optional[int] = None):
        # 추가 디렉터리 생성
        upload_path = cls.make_sub_folders()

        # 원본 파일명 및 확장자 추출
        client_file_name = file.filename
        ext_file_name = cls.make_ext_file_name(client_file_name)
        file_type_enum = cls.make_file_ext_type(ext_file_name)

        # 파일 확장자 타입 검증
        if file_type_enum != file_type:
            raise ValueError("지원되지 않는 파일 타입입니다.")

        # 서버에 저장할 파일 이름 생성 (UUID)
        server_file_name = cls.make_server_file_name(ext_file_name)

        # 전체 경로 생성
        full_path = os.path.join(upload_folder, upload_path, server_file_name)

        # 파일 저장
        if not os.path.exists(os.path.join(upload_folder, upload_path)):
            os.makedirs(os.path.join(upload_folder, upload_path))

        # 파일 저장 (비동기 방식)
        async with aiofiles.open(full_path, "wb") as out_file:
            content = await file.read()
            await out_file.write(content)

        # DTO 반환
        return cls(
            upload_folder=upload_folder,
            upload_path=upload_path,
            client_file_name=client_file_name,
            ext_file_name=ext_file_name,
            file_type=file_type_enum,
            server_file_name=server_file_name,
            full_path=full_path,
            team_id=team_id,
            user_id=user_id
        )

    # 추가 디렉토리 경로 생성 (날짜 기준)
    @staticmethod
    def make_sub_folders():
        return datetime.now().strftime("%Y/%m/%d").replace("/", os.sep)

    # 파일 확장자 추출
    @staticmethod
    def make_ext_file_name(original_filename: str) -> str:
        return original_filename.split(".")[-1].lower()

    # 파일 확장자에 따른 파일 타입 결정
    @staticmethod
    def make_file_ext_type(ext_file_name: str) -> FileType:
        if ext_file_name in ["jpg", "jpeg", "png", "gif"]:
            return FileType.IMAGE
        elif ext_file_name in ["mp4", "avi", "mkv"]:
            return FileType.VIDEO
        else:
            raise ValueError(f"지원되지 않는 파일 확장자: {ext_file_name}")

    # UUID 기반 파일 이름 생성
    @staticmethod
    def make_server_file_name(ext_file_name: str) -> str:
        return f"{uuid.uuid4()}.{ext_file_name}"
