

-- 최연장자 학생 생일
SELECT MIN(s_birthday) FROM APR01_STUDENT;

SELECT * FROM APR01_STUDENT

-- 국어 점수가 80점 이상인
-- 학생 이름, 국어
SELECT s_name, s_kor 
FROM APR01_STUDENT 
WHERE s_kor >= 80; -- 조건절 WHERE

-- 홍길동
-- 평균 점수
SELECT s_name, (s_kor+s_eng+s_mat)/3 AS AVG 
FROM APR01_STUDENT 
WHERE s_name = '고길동'; -- 값이 같은지를 판단 할 때에는 '=' 한개

-- 문자열 포함 검색 : 
--		필드명 LIKE '패턴'
--					'ㅋ%' : 'ㅋ'으로 시작 
--					'%ㅋ' : 'ㅋ'으로 끝
--					'%ㅋ%' : 'ㅋ'이 포함
-- 홍씨
-- 이름, 생일
SELECT s_name, s_birthday
FROM APR01_STUDENT
WHERE s_name LIKE '홍%'

-- 김씨나 박씨의
-- 이름, 국/영/수 평균
SELECT s_name, (s_kor+s_eng+s_mat)/3 AS AVG 
FROM APR01_STUDENT
WHERE s_name LIKE '김%' OR s_name LIKE '박%'

-- 50 < 국어 < 80
-- 이름, 국어
SELECT s_name, s_kor
FROM APR01_STUDENT
WHERE s_kor > 50 AND s_kor < 80;


SELECT * FROM APR01_SNACK;

INSERT INTO APR01_SNACK values('매운새우깡', 2000, to_date('20251105', 'YYYYMMDD'));


-- to_date : 글자를 넣으면 날짜로 바꿔줌.
-- to_date('20251105', 'YYYYMMDD')

-- to_char : 날짜를 넣으면 글자 상태로 바꿔줌.
-- to_char(sysdate, 'YYYYMMDD') : 20250402 (= 날짜 부분만 뜯어서 글자로.)

-- concat() : 글자 여러개 붙일 때 사용
-- concat(... , '235959') => 20250402235959 (= 시간을 포함하여 글자로)

-- to_date(... , 'YYYYMMDDHH24MISS') = 글자 상태를 date 형식으로 변환

-- 내일 먹으면 죽는 과자
-- 전체 정보
SELECT * FROM APR01_SNACK 
WHERE s_exp <= to_date(concat(to_char(sysdate, 'YYYYMMDD'), '235959'), 'YYYYMMDDHH24MISS');

SELECT s_name, s_kor FROM APR01_STUDENT;

-- 국어 점수 최고점
-- 이름, 국어
SELECT s_name, s_kor FROM APR01_STUDENT WHERE s_kor = MAX(s_kor); -- 통계함수는 WHERE 절에는 사용할 수 없음.

-- SubQuery : 서브 쿼리
SELECT s_name, s_kor 
FROM APR01_STUDENT 
WHERE s_kor = (
	SELECT MAX(s_kor) 
	FROM APR01_STUDENT -- 국어점수 최고점
);

SELECT * FROM APR01_STUDENT;

-- 제일 어린 학생
-- 이름, 국영수평균
SELECT MAX(s_birthday) FROM APR01_STUDENT;
SELECT s_name, (s_kor+s_eng+s_mat)/3
FROM APR01_STUDENT
WHERE s_birthday IN (
	SELECT MAX(s_birthday) FROM APR01_STUDENT
);


-- 반 평균보다 시험 못 친 학생
-- 이름, 국영수평균
SELECT AVG((s_kor+s_eng+s_mat)/3) FROM APR01_STUDENT;
SELECT s_name, (s_kor+s_eng+s_mat)/3
FROM APR01_STUDENT
WHERE (s_kor+s_eng+s_mat)/3 < (
	SELECT AVG((s_kor+s_eng+s_mat)/3) FROM APR01_STUDENT
);


---------------------------------------------