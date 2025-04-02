-- DB 설계 -> 데이터 -> R
-- 요식업 프랜차이즈 관리
-- 홍길동씨, 19990101생, 수원 거주, 
-- 김밥천국, 종로점, 10테이블
-- 야채김밥, 4000, 식사류

-- 테이블을 하나로 -> 중복 저장됨
-- -> 용량 낭비
---------------------------------------------
-- DB Design : DB 설계
-- 1) 주제별로 테이블 나누고 : 이래야 중복이 생기지 않음
-- 		=> 사장 / 매장 / 메뉴 테이블 나누기
-- 2) 기본적인거 하고 (자료형, PK, ...)
-- 3) 각 테이블간이 관계 체크
--		-> m:n : 따로 테이블 하나 추가
--		-> 1:n -> n쪽에 테이블에 1의 PK필드
---------------------------------------------
-- DB
--		RDBMS 계열
--		NoSQL 계열
---------------------------------------------
-- RDBMS (Relational Database Management System) : '관계형' 데이터베이스 관리 시스템
--		일반적으로 DB 라고 하면, 이걸 말함.
--		테이블을 나눠서 디자인 함.
--		테이블 간의 관계를 중심으로, 풀어나가는
---------------------------------------------
-- NoSQL 
--	SQL을 쓰지 않고, 그 DB의 자체 문법으로 사용


-- 사장 테이블
DROP TABLE CEO CASCADE CONSTRAINT purge;
CREATE TABLE CEO(
	c_no NUMBER(3) PRIMARY KEY,
	c_name varchar2(10 char) NOT NULL,
	c_birth DATE NOT NULL,
	c_addr varchar2(10 char) NOT NULL
);

-- 매장 테이블
DROP TABLE Restaurant CASCADE CONSTRAINT purge;
CREATE TABLE Restaurant(
	r_no NUMBER(2) PRIMARY KEY,
	r_name varchar2(10 char) NOT NULL,
	r_locate varchar2(10 char) NOT NULL,
	r_table NUMBER(2) NOT NULL
);

-- 메뉴 테이블
CREATE TABLE Menu(
	m_no NUMBER(2) PRIMARY KEY,
	m_name varchar2(10 char) NOT NULL,
	m_price NUMBER(6) NOT NULL,
	m_cate varchar2(10 char) NOT NULL,
	m_r_no NUMBER(2) NOT NULL
);

-- 운영 테이블
CREATE TABLE Operate(
	o_no NUMBER(2) PRIMARY KEY,
	o_c_no NUMBER(2) NOT NULL,
	o_r_no NUMBER(2) NOT NULL
);

----- 시퀀스 -----
CREATE SEQUENCE CEO_SEQ;
CREATE SEQUENCE Restaurant_SEQ;
DROP SEQUENCE Restaurant_SEQ;
CREATE SEQUENCE Menu_SEQ;
CREATE SEQUENCE Operate_SEQ;

----- 사장 -----
INSERT INTO CEO VALUES(CEO_SEQ.nextval, '홍길동', to_date('19990101', 'YYYYMMDD'), '수원');
INSERT INTO CEO VALUES(CEO_SEQ.nextval, '김길동', to_date('20000101', 'YYYYMMDD'), '인천');
INSERT INTO CEO VALUES(CEO_SEQ.nextval, '박철수', to_date('20020202', 'YYYYMMDD'), '안산');
INSERT INTO CEO VALUES(CEO_SEQ.nextval, '이길동', to_date('20010606', 'YYYYMMDD'), '서울');
INSERT INTO CEO VALUES(CEO_SEQ.nextval, '최길동', to_date('19950808', 'YYYYMMDD'), '부산');
SELECT * FROM CEO;

----- 매장 -----
INSERT INTO Restaurant VALUES(Restaurant_SEQ.nextval, '김밥천국', '종로', 10);
INSERT INTO Restaurant VALUES(Restaurant_SEQ.nextval, '우동천국', '종각', 20);
INSERT INTO Restaurant VALUES(Restaurant_SEQ.nextval, '하이디라오', '홍대', 30);
INSERT INTO Restaurant VALUES(Restaurant_SEQ.nextval, '등촌갈국수', '강남', 20);
INSERT INTO Restaurant VALUES(Restaurant_SEQ.nextval, '에슐리', '을지로', 10);
INSERT INTO Restaurant VALUES(Restaurant_SEQ.nextval, '김밥천국', '목동', 30);
SELECT * FROM Restaurant;

----- 메뉴 -----
INSERT INTO Menu VALUES(Menu_SEQ.nextval, '야채김밥', 2000, '식사', 1);
INSERT INTO Menu VALUES(Menu_SEQ.nextval, '김치김밥', 2500, '식사', 1);
INSERT INTO Menu VALUES(Menu_SEQ.nextval, '치즈김밥', 3000, '식사', 6);
INSERT INTO Menu VALUES(Menu_SEQ.nextval, '김치라면', 3000, '식사', 6);
INSERT INTO Menu VALUES(Menu_SEQ.nextval, '우육면', 9000, '식사', 3);
INSERT INTO Menu VALUES(Menu_SEQ.nextval, '샤브샤브', 15000, '식사', 4);
INSERT INTO Menu VALUES(Menu_SEQ.nextval, '돈까스김밥', 4000, '식사', 1);
INSERT INTO Menu VALUES(Menu_SEQ.nextval, '불고기김밥', 4500, '식사', 6);
INSERT INTO Menu VALUES(Menu_SEQ.nextval, '소고기김밥', 5000, '식사', 5);
INSERT INTO Menu VALUES(Menu_SEQ.nextval, '스페셜정식', 20000, '식사', 1);
SELECT * FROM Menu;

----- 운영 -----
INSERT INTO Operate VALUES(Operate_SEQ.nextval, 1, 6);
INSERT INTO Operate VALUES(Operate_SEQ.nextval, 2, 1);
INSERT INTO Operate VALUES(Operate_SEQ.nextval, 5, 3);
SELECT * FROM Operate;


---------------------------------------------

-- 프랜차이즈 전체 메뉴 정보
SELECT * FROM Menu;

-- 프랜차이즈 전체 사장 정보
SELECT * FROM CEO;

-- 테이블이 20개가 넘는 매장
-- 매장명, 지점명, 테이블 수
SELECT r_name, r_locate, r_table FROM Restaurant WHERE r_table > 20;

-- 프랜차이즈 전체 메뉴 평균가
SELECT AVG(m_price) FROM Menu;

-- 제일 비싼 메뉴
-- 이름 가격
SELECT m_name, m_price FROM Menu WHERE m_price = (SELECT MAX(m_price) FROM Menu);

-- 평균보다 싼 메뉴
-- 이름, 가격
SELECT m_name, m_price FROM Menu WHERE m_price < (SELECT AVG(m_price) FROM Menu);


-- 서브 쿼리
--		WHERE 절에 통계함수 못쓰니까..
--		테이블 여러개 관계의 데이터 검색

-- 김밥천국 종로점의 
-- 메뉴명, 가격
SELECT m_name, m_price FROM Menu 
WHERE m_r_no = (SELECT r_no FROM Restaurant WHERE r_name = '김밥천국' AND r_locate = '종로');


-- 홍길동, 19990101이 운영하는 매장
-- 이름, 지점명
SELECT r_name, r_locate FROM Restaurant WHERE r_no IN (
	SELECT o_r_no FROM Operate WHERE o_c_no IN (
		SELECT c_no FROM CEO WHERE c_name = '홍길동' AND c_birth = to_date('19990101', 'YYYYMMDD')
	)
);

-- 김길동, 20000101이 운영하는 매장
-- 메뉴명, 가격
SELECT m_name, m_price FROM MENU WHERE m_r_no IN (
	SELECT r_no FROM Restaurant WHERE r_no = (
		SELECT o_r_no FROM Operate WHERE o_c_no = (
			SELECT c_no FROM CEO 
			WHERE c_name = '김길동' AND c_birth = to_date('20000101', 'YYYYMMDD')
		)
	)
);


-- 최고가 메뉴를 파는 사장님의
-- 이름, 생일
SELECT c_name, c_birth FROM CEO WHERE c_no IN (
	SELECT o_c_no FROM Operate WHERE o_r_no IN (
		SELECT m_r_no FROM MENU WHERE m_price = (
			SELECT MAX(m_price) FROM MENU)
	)
);




--김밥 시리즈
-- 메뉴명, 가격, 매장명, 지점명
-- 조인 JOIN
-- 모든 경우의 수 별로 다 연결해서 붙여버림
--		DB서버의 HDD에 테이블 2개 각각 데이터가 10TB, 10TB
--		JOIN = 모든 경우의 수 별로 다 붙이면 : ?
--		변수에 저장 -> RAM에 저장해놓고
--		맞는 것만 필터링 함 -> IF => 매우 비효율적
SELECT * 
FROM Restaurant, Menu;

-- 맞는것만 필터링
SELECT * 
FROM Restaurant r, Menu m
WHERE r.r_no = m.m_r_no
AND m_name LIKE '%김밥';

-- 최연장자 사장님네의
-- 매장명, 지점명, 사장이름, 생일
-- 필드명이 중복될 때,

SELECT r_name, r_locate, c_name, c_birth
FROM CEO c, Operate o, Restaurant r
WHERE c.c_no = o.o_c_no 
	AND o_r_no = r.r_no
	AND	c_birth = (SELECT MIN(c_birth) FROM CEO);

-- 최고가 메뉴를 파는 사장님
-- 이름, 생일 
SELECT DISTINCT c_name, c_birth
FROM CEO c, Operate o, Restaurant r, Menu m
WHERE c.c_no  = o.o_c_no
	AND m.m_r_no = o.o_r_no
	AND m_price = (
		SELECT MAX(m_price) FROM Menu
	);


-- 식사 카테고리 파는 사장님 이름
-- 가능 하다면 서브 쿼리를 사용하자.
SELECT c_name FROM CEO WHERE c_no IN (
	SELECT o_c_no FROM Operate WHERE o_r_no IN (
		SELECT m_r_no FROM Menu WHERE m_cate = '식사'
	)
);


-- 식사 카테고리 파는 사장님 이름, 매장명, 지점명
-- -> CEO, Restaurant 에서 꺼내야됨
-- -> join 써서...

SELECT DISTINCT c_name, r_name, r_locate
FROM CEO c, Restaurant R, Menu m, Operate o
WHERE c.c_no  = o.o_c_no
	AND r.r_no = o.o_r_no
	AND m.m_r_no = o.o_r_no
	AND m.m_cate = '식사';

-- WHERE 조건식
-- ORDER BY 필드명, 필드명, ... (조건)

-- 매장명, 지점명, 메뉴명, 가격
-- 을 메뉴명 가나다 순 -> 가격 싼 수
SELECT r_name, r_locate, m_name, m_price
FROM Restaurant R, Menu m
WHERE r.r_no = m.m_r_no
ORDER BY m_name, m_price;


-- 사장이름, 생일, 매장명, 지점명
-- 사장님 나이 어린 순
SELECT * 
FROM CEO c, Restaurant r, Operate o
WHERE o.o_c_no = c.c_no
AND o.o_r_no = r.r_no



