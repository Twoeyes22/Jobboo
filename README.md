## 프로젝트 소개

FAST API 사용해 팀원의 이력서를 한 눈에 보는 웹 페이지 


## 프로젝트 구조
```
Jobboo/
├── Dockerfile
├── README.md
├── app
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routers
│   │   └── pages.py
│   ├── static
│   │   ├── css
│   │   │   ├── main.css
│   │   │   ├── resume_css
│   │   │   │   └── 이력서 CSS 파일들
│   │   │   └── user_create.css
│   │   ├── images
│   │   │   ├── resume_images
│   │   │   │   └── 이력서에서 참조하는 개인 이미지들
│   │   │   ├── team_logo
│   │   │   │   ├── 2BillionForYear.png
│   │   │   │   ├── catchcloud.png
│   │   │   │   └── jobboo_logo.png
│   │   │   └── user_photos
│   │   │       └── main page 유저 별 이미지들
│   │   ├── js
│   │   │   ├── main.js
│   │   │   └── resume_js
│   │   │       └── 이력서 js 파일들
│   │   └── resume_html
│   │       └── 이력서 html 파일들
│   └── templates
│       ├── 404.html
│       ├── base.html
│       ├── create_user.html
│       └── index.html
├── config
├── docker-compose.yaml
├── init.sql
└── requirements.txt
```
## 환경설정

requirements.txt
```
fastapi==0.100.0  # 대장
uvicorn==0.22.0  # 빌드 툴
jinja2==3.1.2   # 템플릿
sqlalchemy==1.4.40 # ORM
#pymysql==1.0.2   # mysql 드라이버
pytest==8.3.2     # 테스트 도구
pydantic==1.10.9  # Json 변환 직렬화 역직렬화
httpx==0.24.1
python-dotenv     # 코드에 env 변수 필요할때
python-multipart # 파일 업로드 할때 필요한
aiofiles # 파일 입출력 비동기 가능하게


alembic # SQLAlchemy를 위한 데이터베이스 마이그레이션 도구로, 스키마 변경을 버전 관리
aiomysql # 비동기 MySQL 데이터베이스 지원을 제공하는 라이브러리

sqlalchemy[asyncio] # SQLAlchemy의 비동기 지원 모듈로, 비동기 I/O를 사용하여 데이터베이스 작업을 수행
cryptography==40.0.1 # 암호화와 관련된 보안 작업을 수행할 수 있는 라이브러리%
```

Service Port
```
<WEB>
Local Port : 8080
Container Port : 8080

<DB>
Local Port : 3306
Container Port : 3306
```

## 서비스 동작

```
sudo docker-compose up -d
```

## 브랜치 컨벤션

`HEADER/{내용}` 

e.g. `main`, `develop`, `feature/login`

|HEADER|설명|
|:--:|:--:|
|main|기준이 되는 브랜치|
|develop|개발 브랜치. feature 브랜치에서 작업한 기능이 merge되는 브랜치|
|feature|기능 단위로 개발하는 브랜치. 기능 개발이 완료되면 develop 브랜치에 merge|
|release|배포 전 QA(품질 보증)를 위한 브랜치. QA 완료 후 main에 merge|
|hotfix|main 브랜치로 배포 후 버그가 생겼을 때 긴급 수정하는 브랜치|

## 커밋 컨벤션

`HEADER: {내용}` 

e.g. `feat: 로그인 기능 구현`

|HEADER|설명|
|:--:|:--:|
|feat|새로운 기능 구현|
|refactor|내부 로직은 변경하지 않고 기존 코드 리팩토링|
|fix|버그, 오류, 충돌 해결|
|add|feat 이외의 부수적인 코드 추가, 라이브러리 추가 작업|
|update|기능 수정|
|chore|잡일. 버전 코드 수정, 패키지 구조 변경, 파일 이동, 가독성이나 변수명 수정|

## 멤버

|<img width=150 src="https://avatars.githubusercontent.com/u/125520029?v=4" />|<img width=150 src="https://avatars.githubusercontent.com/u/141303941?v=4" />|<img width=150 src="https://avatars.githubusercontent.com/u/162412972?v=4" />|
|:----:|:----:|:----:|
| [박서연](https://github.com/seoyeon0201) | [양민우](https://github.com/Twoeyes22) | [김홍집](https://github.com/redhouse33) |

|<img width=150 src="https://avatars.githubusercontent.com/u/125520029?v=4" />|<img width=150 src="https://avatars.githubusercontent.com/u/125520029?v=4" />|<img width=150 src="https://avatars.githubusercontent.com/u/125520029?v=4" />|<img width=150 src="https://avatars.githubusercontent.com/u/166140353?v=4" />|
|:----:|:----:|:----:|:----:|
| [최광진]() | [나보영]() | [박지만]() | [홍구](https://github.com/rednine9777) |
