from fastapi import APIRouter, Request, Form, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
# 라우터 객체 생성
router = APIRouter()

# Jinja2 템플릿 엔진 설정
templates = Jinja2Templates(directory="templates")

# 팀원 정보를 담은 리스트, DB를 사용해보자!
team_members = [
    {"name": "Seoyeon", "image": "Seoyeon.jpg", "resume": "Seoyeon.html"},
    {"name": "Minwoo", "image": "minwoo.png", "resume": "minwoo.html"},
    {"name": "Hongjip", "image": "Hongjip.jpg", "resume": "Hongjip.html"},
    {"name": "Gwangjin", "image": "Gwangjin.jpg", "resume": "Gwangjin.html"},
    {"name": "Boyeong", "image": "Boyeong.jpg", "resume": "Boyeong.html"},
    {"name": "Jiman", "image": "Jiman.jpg", "resume": "Jiman.html"},
    {"name": "Goo", "image": "Goo.jpg", "resume": "Goo.html"}
]

# 홈페이지 라우트
@router.get("/")
async def home(request: Request):
    # index.html 템플릿을 렌더링하고, 팀원 정보를 전달
    return templates.TemplateResponse("index.html", {"request": request, "team_members": team_members})

# 개별 이력서 페이지 라우트
@router.get("/resume/{member_name}")
async def resume(request: Request, member_name: str):
    # 해당 팀원의 이력서 HTML 파일을 렌더링
    return templates.TemplateResponse(f"resume/{member_name}.html", {"request": request})

## 다른 사람 메인페이지도 추가해보자.

##유저 생성 페이지
# 유저 생성 페이지 라우트
@router.get("/user/create")
async def create_user_page(request: Request):
    # create_user.html 템플릿을 렌더링
    return templates.TemplateResponse("create_user.html", {"request": request})


@router.post("/user/create")
async def create_user(
    request: Request,
    u_name: str = Form(...),
    u_nickname: str = Form(...),
    u_email: str = Form(None),
    u_git: str = Form(None),
    u_html: UploadFile = Form(None),
    u_css: UploadFile = Form(None),
    photo: UploadFile = Form(None),
    t_id: int = Form(...)
):
    # 여기에서 받은 데이터를 처리하고 DB에 저장하는 등의 작업을 수행할 수 있습니다.
    # 예를 들어, 파일을 저장하는 작업을 추가할 수 있습니다.

    # 예시로 파일을 저장하는 코드
    if u_html:
        # 파일 이름이 실제로 있는지 확인한 후, 경로를 포함한 파일명을 사용
        file_path_html = f'templates/resume/{u_html.filename}'
        if not u_html.filename:  # 파일 이름이 없는 경우 처리
            return {"error": "HTML 파일이 지정되지 않았습니다."}
        with open(file_path_html, 'wb') as f:
            f.write(await u_html.read())
    
    if u_css:
        file_path_css = f'static/css/resume_css/{u_css.filename}'
        if not u_css.filename:  # 파일 이름이 없는 경우 처리
            return {"error": "CSS 파일이 지정되지 않았습니다."}
        with open(file_path_css, 'wb') as f:
            f.write(await u_css.read())
    
    if photo:
        file_path_photo = f'static/images/user_photos/{photo.filename}'
        if not photo.filename:  # 파일 이름이 없는 경우 처리
            return {"error": "사진 파일이 지정되지 않았습니다."}
        with open(file_path_photo, 'wb') as f:
            f.write(await photo.read())

    # DB에 유저 정보 저장 로직 추가
    # 예를 들어, 새로운 유저 정보를 데이터베이스에 삽입하는 코드를 여기에 작성합니다.

    # 처리가 끝나면 홈으로 리다이렉트
    return RedirectResponse(url="/", status_code=303)
