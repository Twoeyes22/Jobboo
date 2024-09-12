from typing import Optional
import logging
from fastapi import Depends, Query, Request, APIRouter, Form, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from fastapi.templating import Jinja2Templates
from models import Team
from src.main.goo.repository.TeamRepository import TeamRepository
from src.main.goo.model.UploadFileDTO import UploadFileDTO, FileType

# 로거 설정
logging.basicConfig(level=logging.INFO)

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# 데이터베이스 의존성을 주입하는 함수
async def get_team_repository(db: AsyncSession = Depends(get_db)) -> TeamRepository:
    return TeamRepository(db)

@router.get("/team/create", response_class=HTMLResponse, name="create_team")
async def create_team_form(request: Request):
    return templates.TemplateResponse("team/create_team.html", {"request": request})

@router.post("/team/create", name="create_team")
async def create_team(
    t_name: str = Form(...),
    t_intro: Optional[str] = Form(None),
    t_descript: Optional[str] = Form(None),
    t_git: Optional[str] = Form(None),
    t_logo: Optional[UploadFile] = File(None),
    repo: TeamRepository = Depends(get_team_repository)
):
    # 팀 이름 중복 확인
    existing_team = await repo.get_team_by_name(t_name)
    if existing_team:
        logging.error("팀 이름 중복 오류: %s", t_name)
        raise HTTPException(status_code=400, detail="이미 존재하는 팀 이름입니다.")

    # 팀 생성 요청 로그
    logging.info("팀 생성 요청: %s, %s, %s, %s, %s", t_name, t_intro, t_descript, t_git, t_logo.filename if t_logo else "No Logo")

    team = Team(
        t_name=t_name,
        t_intro=t_intro,
        t_descript=t_descript,
        t_git=t_git,
        t_logo=t_logo.filename if t_logo else None
    )

    try:
        await repo.create_team(team)
        return {"message": "팀 생성이 완료되었습니다."}
    except Exception as e:
        logging.error("팀 생성 중 오류 발생: %s", str(e))
        raise HTTPException(status_code=500, detail="팀 생성 중 오류 발생")

    
@router.get("/team/check-name", name="check_team_name")
async def check_team_name(name: str = Query(..., description="The name to check for uniqueness"), repo: TeamRepository = Depends(get_team_repository)):
    existing_team = await repo.get_team_by_name(name)
    return {"exists": bool(existing_team)}
    

# @router.post("/upload")
# async def upload_file(file: UploadFile):
#     try:
#         file_dto = await UploadFileDTO.create_upload_file_dto(UPLOAD_DIR, file, FileType.IMAGE)
#         return {"message": "파일 업로드 완료", "data": file_dto}
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="파일 업로드 중 오류 발생")
