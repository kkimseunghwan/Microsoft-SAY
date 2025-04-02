DROP TABLE Apr01_Student CASCADE CONSTRAINT purge;
DROP TABLE Apr01_Students CASCADE CONSTRAINT purge;

-- 번호 : 테이블에 딱히 PK 줄만한 필드가 없으면 번호 필드를 추가해서 
CREATE TABLE Apr01_Students(
	s_no number(2) PRIMARY KEY,
	s_name varchar2(10 char) NOT NULL,
	s_birth DATE NOT NULL,
	s_kor number(3) NOT NULL,
	s_eng number(3) NOT NULL,
	s_mat number(3) NOT NULL
);

-- ctrl + alt 화살표위/아래 -> 해당 라인 복사
-- 학생 번호 : 억지로 만든거, 영양가 있는 데이터는 x -> 내가 세고있나...
-- 자동으로 좀 어떻게 할당이 안되나?

-- SEQUENCE 
--		테이블에 종속적인 존재가 아니지만,
--		지만 종속적으로 쓰는
--		=> INSERT 실패 해도 올라감, 데이터가 삭제된다고 뒷 번호가 당겨지나? 어림도 없음
--		-> 1, 2, 3, 4 를 위한 것이 아님!
-- SEQUENCE 만들기
--		CREATE SEQUENCE 시퀀스명;
CREATE SEQUENCE Apr01_Student_Seq; -- 테이블명_seq (암묵적 룰)
-- SEQUENCE 삭제
--		DROP SEQUENCE 시퀀스명;
DROP SEQUENCE Apr01_Student_Seq;
DROP SEQUENCE Apr01_Students_Seq;
-- SEQUENCE 사용
--		INSERT 할 때, 시퀀스명.nextval


INSERT INTO Apr01_Student 
	VALUES(Apr01_Student_Seq.nextval, '홍길동', 
		to_date('2003-05-05', 'YYYY-MM-DD'),100, 90, 80);

INSERT INTO Apr01_Student 
	VALUES(Apr01_Student_Seq.nextval, '김길동', 
		to_date('2003-12-15', 'YYYY-MM-DD'), 90, 50, 20);

INSERT INTO Apr01_Student 
	VALUES(Apr01_Student_Seq.nextval, '박철수', 
		to_date('2003-03-29', 'YYYY-MM-DD'), 50, 100, 40);

INSERT INTO Apr01_Student 
	VALUES(Apr01_Student_Seq.nextval, '트럼프', 
		to_date('2003-12-01', 'YYYY-MM-DD'), 60, 10, 30);

INSERT INTO Apr01_Student 
	VALUES(Apr01_Student_Seq.nextval, '바이든', 
		to_date('2003-02-15', 'YYYY-MM-DD'), 100, 40, 10);

INSERT INTO Apr01_Students 
	VALUES(Apr01_Student_Seq.nextval, '김가네', 
		to_date('2003-06-30', 'YYYY-MM-DD'), 50, 10, 0);

INSERT INTO Apr01_Student 
	VALUES(Apr01_Student_Seq.nextval, '곽두팔', 
		to_date('2003-01-01', 'YYYY-MM-DD'), 100, 80, 20);

INSERT INTO Apr01_Student 
	VALUES(Apr01_Student_Seq.nextval, '마리아', 
		to_date('2003-03-18', 'YYYY-MM-DD'), 20, 30, 40);

-- 195 168 9 144 kwon 1
---------------------------------------------
-- 데이터 조회 : R
-- SELECT 필드명, 필드명, ...
-- FROM 테이블 명
-- * = 전체
SELECT * FROM Apr01_Student;

-- 학생 이름, 국어만 조회하고 싶음.
SELECT s_name, s_kor FROM Apr01_Student;

-- 학생 이름, 영어(필드명 바꿔서)
SELECT s_name, s_eng AS english
FROM Apr01_Student;

-- 학생 이름, 국어, 영어, 수학, 평균
SELECT s_name, s_kor, s_eng, s_mat, (s_kor+s_eng+s_mat)/3 AS AVG
FROM Apr01_Student;

-- 통계 함수 : max, min, sum, avg, count ...
-- 학생 국어 반 평균
SELECT AVG(s_kor) AS Kor_AVG
FROM Apr01_Student;

-- 학생들 평균 점수의 반 평균
SELECT AVG((s_kor+s_eng+s_mat)/3) AS Kor_AVG
FROM Apr01_Student;

-- 학생들 총 몇명
SELECT COUNT(*)
FROM Apr01_Student;

SELECT MAX(s_kor), MIN(s_eng) FROM Apr01_Student;









