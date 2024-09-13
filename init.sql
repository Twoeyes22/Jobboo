-- 문자 인코딩 설정
SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;
SET collation_connection = utf8mb4_unicode_ci;

-- 데이터베이스 생성 (이미 존재하지 않는 경우)
CREATE DATABASE IF NOT EXISTS jobboo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE jobboo;

-- 사용자 생성 및 권한 부여
CREATE USER IF NOT EXISTS 'jobboo'@'%' IDENTIFIED BY 'jobboo';
GRANT ALL PRIVILEGES ON jobboo.* TO 'jobboo'@'%';
FLUSH PRIVILEGES;

-- team 테이블 생성 (이미 존재하지 않는 경우)
CREATE TABLE IF NOT EXISTS team (
    t_id INT AUTO_INCREMENT PRIMARY KEY,
    t_name VARCHAR(255) NOT NULL,
    t_intro TEXT,
    t_descript TEXT,
    t_logo VARCHAR(255),
    t_git VARCHAR(255)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- user 테이블 생성 (이미 존재하지 않는 경우)
CREATE TABLE IF NOT EXISTS user (
    u_id INT AUTO_INCREMENT PRIMARY KEY,
    t_id INT,
    u_name VARCHAR(255) NOT NULL,
    u_nickname VARCHAR(255),
    u_email VARCHAR(255),
    u_git VARCHAR(255),
    u_html TEXT,
    u_css TEXT,
    u_image VARCHAR(255),
    FOREIGN KEY (t_id) REFERENCES team(t_id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- team 테이블 데이터 삽입
INSERT INTO team (t_name, t_intro, t_descript, t_logo, t_git) VALUES
('Jobboo', 'DevOps의 숙명!!!', '클라우드 엔지니어 혹은 DevOps를 꿈꾸는 머찐 팀입니다.', '/images/team_logo/jobboo_logo.png', 'https://github.com/Kakao-X-Goorm-DEEP-DIVE-course/Jobboo'),
('연매출2조', '클라우드 전문가 그룹', 'AWS, Azure, GCP 전문가들이 모였습니다.', '/images/team_logo/2BillionForYear.png', 'https://github.com/Kakao-X-Goorm-DEEP-DIVE-course/guestbook'),
('사라진 그들', 'AI 혁신가들', '인공지능과 머신러닝을 연구하는 팀입니다.', '/images/team_logo/jobboo_logo.png', 'https://github.com/aiinnovators'),
('캐치구름', '웹 개발의 마법사들', '최신 웹 기술을 연구하고 적용하는 팀입니다.', '/images/team_logo/catchcloud.png', 'https://github.com/Kakao-X-Goorm-DEEP-DIVE-course/Catch-Goorm');

-- user 테이블 데이터 삽입
INSERT INTO user (t_id, u_name, u_nickname, u_email, u_git, u_html, u_css, u_image) VALUES
(1, 'minwoo','DevOps_Master', 'devops@jobboo.com', 'https://github.com/Twoeyes22', 'resume_html/minwoo.html', 'css/resume_css/minwoo.css', 'images/user_photos/minwoo.png'),
(1, 'seoyeon','CloudGuru', 'cloud@masters.com', 'https://github.com/cloud_guru', 'resume_html/minwoo.html', '/css/cloud_guru.css', '/images/cloud_guru.jpg'),
(1, 'honggoo','AI_Researcher', 'ai@innovators.com', 'https://github.com/ai_researcher', 'resume_html/minwoo.html', '/css/ai_researcher.css', '/images/ai_researcher.jpg'),
(1, 'kwangjin','FrontendNinja', 'kwangjin@webwizards.com', 'https://github.com/frontend_ninja', 'resume_html/kwangjin.html', '/css/frontend_ninja.css', '/images/frontend_ninja.jpg'),
(1, 'boyeong','FrontendNinja', 'boyeong@webwizards.com', 'https://github.com/frontend_ninja', 'resume_html/nabo2000@naver.com.html', '/css/frontend_ninja.css', 'images/user_photos/nabo2000@naver.com.jpeg'),
(1, 'hongzip','FrontendNinja', 'hongzip@webwizards.com', 'https://github.com/frontend_ninja', '/html/frontend_ninja.html', '/css/frontend_ninja.css', '/images/frontend_ninja.jpg'),
(2, 'hyeonjin','Backend Engineer', 'overlaylowedir@gmail.com', 'https://github.com/badasskim', 'resume_html/badasskim.html', 'css/ai_researcher.css', 'images/user_photos/badasskim.png'),
(3, 'Dig','FrontendNinja', 'bbkwangjin@webwizards.com', 'https://github.com/frontend_ninja', '/html/frontend_ninja.html', '/css/frontend_ninja.css', '/images/frontend_ninja.jpg'),
(4, 'born','FrontendNinja', 'ddboyeong@webwizards.com', 'https://github.com/frontend_ninja', '/html/frontend_ninja.html', '/css/frontend_ninja.css', '/images/frontend_ninja.jpg'),
(4, 'zip','FrontendNinja', 'eehongzip@webwizards.com', 'https://github.com/frontend_ninja', '/html/frontend_ninja.html', '/css/frontend_ninja.css', '/images/frontend_ninja.jpg');
