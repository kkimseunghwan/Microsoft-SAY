-- ctrl + m 코드 전체 화면?

-- SQL (Structured Query Language)
--		DB를 제어할 때 쓰는 언어 (PL 아님)
--		중에 데이터를 C R U D 하는 부분만 목표함
--		CRUD (= Create Read Update Delete)
--		DB메이커는 다양하지만 SQL은 공통
--		대소문자 구분x
--			-> 오피셜로는 대무문자
--			-> 소문자로 써놔도 대문자로 인식
---------------------------------------------
-- DB는 table 테이블 형태로 데이터를 관리
-- Table - 행과 열로 구성
-- feild(필드) = column(열) 
-- record(레코드) = row(행) = data(데이터)
---------------------------------------------
-- 용량
--		숫자, 영어, ... : 1글자가 1byte
-- 		한글, 한자, ... : 1글자가 3bytes
-- 		7 : 7 bytes
--		7 char (단위의 char) = 7글자 라는 뜻.
---------------------------------------------
-- 자료형 : 데이터의 특징을 파악해서 적절한 자료형을 할당
-- 글자
--	- char(용량) : 공백을 넣어서라도 무조건 그 용량대로 저장
--		-> 용량 낭비, 테이터 변형 발생 위험
--		-> varchar2 보다 속도가 빠름
--		char(5 char) 
--			-> "zzzzz"(저장) -> "zzzzz"
--			-> "zz"(저장) -> "zz   "(공백 3개 포함 저장)
--	- varchar2(용량) -> (오라클에만 있는) (기본 varchar을 개선한..)
--		: 용량을 조절 해서 저장 => 용량 낭비x, 데이터 변형x
--		: char 보다 느림 (글자 수 체크, 용량 조절)
--		varchar2(5 char)
--			-> "zzzzz"(저장) -> "zzzzz"
--			-> "zz"(저장) -> "zz" (2byte만 사용)
--			
-- 숫자
--		int : 4byte = -21억 ~ 21억 -> 용량 낭비
--		number(용량) : 필요한 만큼만 할당 가능
--		number(3) : 3byte : 999(3자리까지 표현되는 정수)
--		number(5, 2) : 999.99 (전체자리수, 소수점이하)
-- 날짜/시간 : date
-- 동영상, 음악, ... 기타 파일
--		-> 용량 문제로 시간 손실이 매우 큼.
--		DB서버에는 파일 명만 저장해놓고
--		실제 파일은 웹서버/AI모델 서버에 놓는게..
---------------------------------------------
-- 옵션
--		not null : 필수 -> 사실상 기본적으로 넣자
--		primary key : (기본키) = not null + 중복불허
--			-> 그 데이터를 대표하는 값
--			-> 데이터를 찾을 때 기준이 될 값
--			=> (권장사항) 테이블 하나 만들면 PK는 지정해주는걸로.
---------------------------------------------
-- [ ALTER 테이블 수정 ] 
-- 기능상 가능은 한데, 데이터가 매우 많은 실전에서 쓰는건 불가능
---------------------------------------------
-- [ DROP 테이블 삭제 ]
-- DROP TABLE 테이블명 CASCADE CONSTRAINT purge; 휴지통으로 보내지 말고 바로 삭제
DROP TABLE Apr01_Snack CASCADE CONSTRAINT purge;
---------------------------------------------
-- [ CREATE : 만들기 ]

-- TABLE 테이블 만들기
-- CREATE TABLE 테이블명(
--		-- 필드(열)에 대한 정보를 정의 (열제목=필드명)
--		열제목 자료형 [옵션(필요 시)],
--		필드명 자료형,
--		...
-- ); 

-- 컬럼명 짓기 문화 -> 테이블명 관련 약자_이름 형식
CREATE TABLE Apr01_Snack( s_name varchar2(10 char), s_price number(5) );

-- 시본 옵션 항목 추가
CREATE TABLE Apr01_Snack( 
	s_name varchar2(10 char) PRIMARY KEY, 
	s_price number(5) NOT NULL,
	s_exp DATE NOT NULL
);

---------------------------------------------
-- [ INSERT : 데이터 넣기 ]
-- INSERT INTO 테이블명(필드명1, 필드명2, 필드명3, ...) 
-- VALUES(값1, 값2, 값3, ...); --> 각 값이 해당되는 필드명에 할당
INSERT INTO Apr01_Snack(s_name, s_price) VALUES('새우깡', 1500);

-- 필드 순서 바꾸기 가능 : 딱히..?
INSERT INTO Apr01_Snack(s_price, s_name) VALUES(5000, '단백질바');

-- 값이 0이면 계산 가능한데, 값이 없으면 계산 불가함
-- 특정 필드 제외하고 가능 (NULL값으로 입력됨) : 딱히..? -> 의미 없음..
INSERT INTO Apr01_Snack(s_name) VALUES('후렌치파이');
-- 옵션 NOT NULL 추가 후에는 에러 발생

-->> 그렇다면?? >>
-- INSERT INTO 테이블명 VALUES(값1, 값2, 값3, ...); 
--> 필드명 정의 부분을 제외. -- 입력한 값이 기존 만들었던 순서대로 데이터가 들어감
INSERT INTO Apr01_Snack VALUES('오감자', 2000);

-- 한번 더? -> 오류 발생
INSERT INTO Apr01_Snack VALUES('오감자', 2000);
-- PRIMARY KEY 옵션 추가 후, s_name이 중복되는 데이터는 입력 불가

-- 날짜/시간
-- 		현재시간날짜 : sysdate (INSERT 하는 시점의 서버시간)
INSERT INTO Apr01_Snack VALUES('마이쮸', 500, sysdate);
-- 		특정시간날짜 : 
-- 			to_date(값, 패턴) : str -> datetime
-- Y M D AM PM HH MI SS
--		 	   HH24 (24시간제)
INSERT INTO Apr01_Snack 
	VALUES('단백질바', 500, 
	to_date('2025-05-01 14', 'YYYY-MM-DD HH24'));

---------------------------------------------
-- [ SELECT : 데이터 조회 Read ] 
SELECT * FROM Apr01_Snack;



