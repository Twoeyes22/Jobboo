## 프로젝트 소개

FAST API 사용해 팀원의 이력서를 한 눈에 보는 웹 페이지 


## 프로젝트 구조
```
Jobboo/
│  
├── app/
│   └── main.py
│  
├── Dockerfile
├── README.md
├── config.json
├── docker-compose.yml
└── requirements.txt
```
## 환경설정

requirements.txt
```
fastapi==0.100.0
uvicorn==0.22.0
jinja2==3.1.2
```

Service Port
```
Local port : 8080
Container port : 8080
```

## 서비스 동작

```
sudo docker-compose up -d
```

## 브랜치 컨벤션

`HEADER/{내용}` 

e.g. `feature/login`

|HEADER|설명|
|:--:|:--:|
|main|기준이 되는 브랜치|
|develop|개발 브랜치. feature 브랜치에서 작업한 기능이 merge되는 브랜치|
|feature|기능 단위로 개발하는 브랜치. 기능 개발이 완료되면 develop 브랜치에 merge|
|release|배포 전 QA(품질 보증)를 위한 브랜치. QA 완료 후 main에 merge|
|hotfix|main 브랜치로 배포 후 버그가 생겼을 때 긴급 수정하는 브랜치|

## 커밋 컨벤션

`HEADER: {내용}` 

e.g. `featre: 로그인 기능 구현`

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
