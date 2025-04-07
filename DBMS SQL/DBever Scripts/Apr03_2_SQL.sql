-- CREATE USER ->> DBA

-- CREATE TABLE 
-- DROP TABLE
-- CREATE SEQUENCE ->> DBA지만 개발자도 함.

-- 데이터를 CRUD 하자
-- INCERT : C
-- SELECT : R 
-- UPDATE : U
-- DELETE : D
---------------------------------------------
-- [ UPDATE ]
-- UPDATE 테이블 명 
-- SET 필드명=값, 필드명=값, ...
-- WHERE 조건식 (안쓰면 해당 필드명 값이 다 바뀜)

-- 야채김밥의 가격을 3000원으로 수정
SELECT * FROM MENU;

UPDATE MENU 
SET M_PRICE = 13000 
WHERE M_NAME = '야채김밥';


-- 김밥천국 종로점의 메뉴들의 값을 500원 이하.

SELECT * FROM RESTAURANT, MENU, CEO;

SELECT R_NO FROM RESTAURANT
WHERE R_NAME = '김밥천국' AND R_LOCATE = '종로';

UPDATE MENU 
SET M_PRICE = M_PRICE - 300
WHERE M_R_NO = (
	SELECT R_NO FROM RESTAURANT
	WHERE R_NAME = '김밥천국' AND R_LOCATE = '종로'
);

-- 홍씨 사장님네 메뉴 10% 인상

UPDATE MENU
SET M_PRICE = M_PRICE * 1.1, M_NAME = 'asd'
WHERE M_R_NO IN (
	SELECT O_R_NO FROM OPERATE o, CEO c 
	WHERE o.O_C_NO = c.C_NO
	AND C_NAME LIKE '홍%'
);


SELECT * FROM MENU;

---------------------------------------------

-- [ DELETE ]
-- DELETE FROM 테이블명
-- WHERE 조건식 (뭘 지울 건지)

DELETE FROM MENU 
WHERE M_PRICE = (
	SELECT MAX(M_PRICE) FROM MENU
);

SELECT * FROM MENU ORDER BY M_PRICE DESC;



-- 김밥천국 종로점 폐업
-- (김밥천국 종로점)하고 연결되어있던 메뉴 테이블의 데이터는??
DELETE FROM RESTAURANT
WHERE R_NAME = '김밥천국' AND R_LOCATE = '종로';

SELECT * FROM RESTAURANT;


---------------------------------------------
CREATE TABLE MEMBER (
	M_ID VARCHAR2(10 CHAR) PRIMARY KEY,
	M_PW VARCHAR2(10 CHAR) NOT NULL
);

DROP TABLE BBS CASCADE CONSTRAINT purge;

-- 제약 조건 : CONSTRAINT
-- CREATE TABLE 테이블명 (
-- 		...,
--		CONSTRAINT 제약조건명
--			FOREIGN KEY 필드명A REFERENCES 테이블명(필드명B) ==> 필드명A을 테이블명(필드명B)를 참조하는 외래키로 지정 
--			ON DELETE CASCADE
--			
-- );

CREATE TABLE BBS(
	B_TXT VARCHAR2(10 CHAR) PRIMARY KEY,
	B_M_ID VARCHAR2(10 CHAR) NOT NULL,
	CONSTRAINT BBS_WRITER -- 제액 조건 정의
		-- B_M_ID는 MEMBER 테이블의 M_ID를 참조. 
		-- 즉, B_M_ID에 들어올 수 있는 값은 MEMBER 테이블의 M_ID에 존재하는 값이어야함. 
		-- (없는 값이면 무결성 제약조건으로 인해 오류 발생)
		FOREIGN KEY(B_M_ID) REFERENCES MEMBER(M_ID) 
		ON DELETE CASCADE  -- 참조한 M_ID가 삭제 시, 자동 삭제
);

INSERT INTO MEMBER VALUES('Hwan', 1);
INSERT INTO BBS VALUES('ASDㅋASD', 'Hwan');
INSERT INTO BBS VALUES('ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ', 'HwanA');
SELECT * FROM MEMBER;
SELECT * FROM BBS;


DELETE FROM MEMBER WHERE M_ID = 'Hwan';



---------------------------------------------

-- 파이썬 연결 테이블
CREATE TABLE PRODUCT(
	P_NAME VARCHAR2(10 CHAR) PRIMARY KEY,
	P_PRICE NUMBER(10) NOT NULL
);

INSERT INTO PRODUCT VALUES('마우스', 15000);
INSERT INTO PRODUCT VALUES('키보드', 30000);
INSERT INTO PRODUCT VALUES('USB', 8000);
INSERT INTO PRODUCT VALUES('헤드셋', 45000);
INSERT INTO PRODUCT VALUES('웹캠', 70000);
INSERT INTO PRODUCT VALUES('스피커', 50000);
INSERT INTO PRODUCT VALUES('허브', 12000);
INSERT INTO PRODUCT VALUES('모니터', 50000);

DELETE FROM PRODUCT WHERE P_NAME = '모니터';



SELECT * FROM PRODUCT;
SELECT AVG(P_PRICE) FROM PRODUCT;

-- DBeaver는 auto Commit : 자동으로 반영해줌
COMMIT
ROLLBACK

-- 홍씨 사장님네 메뉴 10% 인상

UPDATE PRODUCT SET P_PRICE = 10 WHERE P_NAME = '허브';



