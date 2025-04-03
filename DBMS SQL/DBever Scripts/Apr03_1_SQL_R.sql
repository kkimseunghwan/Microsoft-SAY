


-- 데이터 조회 : R (READ)
-- SELECT 필드명, 필드명 AS 별칭, 연산자, 통계함수 ...
-- FROM 테이블명, 테이블명, ...
-- WHERE 조건식			-> 데이터 필터링
-- GROUP BY 필드명, 필드명, ...
-- HAVING 조건식		-> GROUP BY 결과를 필터링
-- ORDER BY 필드명, 필드명 [DESC], ... : 정렬


-- 서브 쿼리
--		WHERE 절에 통계함수 쓸때
--		테이블 여러개 엮을 때 사용
--		++.....
-- SELECT (서브 쿼리) FROM (서브 쿼리) WHERE (서브 쿼리) 
-- 위치마다 넣어서 활용 가능 


-- 데이터를 다 가져오나?x 
-- -> 페이지를 나눠서, 그 페이지에 해당하는 10개 -> O


-- ROWNUM : 행번호
--		select 할 때마다 자동으로 부여되는 가상 필드.
--		* 랑은 같이 못씀
--		ORDER BY 보다 먼저 ROWNUM이 부여됨.
-- 		1번 부터 조회해야하는 특성, (WHERE rownum >= 2) <= 이럼 안됨.

SELECT * FROM (
	SELECT rownum AS RN, m_no, m_name, m_price FROM (
		SELECT m_no, m_name, m_price
		FROM MENU
		ORDER BY m_price DESC
	) 
)
WHERE RN >= 3 AND RN <= 5;





-- 1p : 1 ~ 3
-- 2p : 4 ~ 6

-- 매장명, 지점명, 메뉴명, 가격
-- 매장명 가나다순, 지점명 가나다 순, 메뉴명 가나다 순 정렬
-- 4번 부터 6번까지.
--		번호 기준을 메뉴번호? 매장번호?
--		SEQ로 번호를 올림
--			INSERT를 실패해도 올라감
--			여러 테이블이 SEQ하나 같이 쓸 수 있음
--			데이터를 삭제한다고 뒷 번호가 당겨지는게 아님
--			=> 1, 2, 3을 원하는거 아님

SELECT * FROM (
	SELECT rownum AS RN, r_name, r_locate, m_name, M_PRICE FROM (
		SELECT r_name, r_locate, m_name, M_PRICE
		FROM Restaurant r, Menu m
		WHERE r.r_no = m.m_r_no
		ORDER BY r_name, r_locate, m_name
	)
) WHERE RN >= 4 AND RN <= 6

-- Oracle 12c 버전 이상 
SELECT rownum, m_no, m_name, m_price FROM (
	SELECT m_no, m_name, m_price
	FROM Menu
	ORDER BY m_price DESC
) OFFSET 2 ROWS FETCH NEXT 3 ROWS ONLY;
-- OFFSET 2 ROWS : 앞에서부터 2개의 행은 건너뛰기 -> 3부터 시작
-- FETCH NEXT 3 ROWS ONLY : 그 다음 3개의 행(3, 4, 5)만 가져와라 


-- 제일 어린 사장님네의
-- 사장이름, 생일, 매장명, 지점명, 메뉴명, 가격
-- 가격 싼순 -> 메뉴명 가나다 순 -> 매장명 가나다순 정렬
-- 3 ~ 5 까지

-- ROWNUM 활용
SELECT * FROM (
	SELECT ROWNUM AS RN, c_name, c_birth, r_locate, m_name, m_price FROM (
		SELECT c_name, c_birth, r_locate, m_name, m_price
		FROM CEO c, RESTAURANT r, MENU m, OPERATE o
		WHERE c.C_NO  = o.O_C_NO
		AND r.R_NO = o.O_R_NO
		AND m.M_R_NO  = r.R_NO
		AND c_birth IN (
			SELECT MAX(c_birth) FROM CEO
		)
		ORDER BY M_PRICE, M_NAME, R_NAME
	)
) WHERE RN >= 3 AND RN <= 5;

-- OFFSET 활용
SELECT ROWNUM AS RN, c_name, c_birth, r_locate, m_name, m_price FROM (
	SELECT c_name, c_birth, r_locate, m_name, m_price
	FROM CEO c, RESTAURANT r, MENU m, OPERATE o
	WHERE c.C_NO  = o.O_C_NO
	AND r.R_NO = o.O_R_NO
	AND m.M_R_NO  = r.R_NO
	AND c_birth IN (
		SELECT MAX(c_birth) FROM CEO
	)
	ORDER BY M_PRICE, M_NAME, R_NAME
) OFFSET 2 ROWS FETCH NEXT 3 ROWS ONLY;


-- GROUP BY 필드명, 필드명, 필드명, ...
-- "카테고리별" 메뉴 평균가 
SELECT M_CATE ,AVG(m_price) 
FROM MENU 
GROUP BY M_CATE 
ORDER BY AVG(M_PRICE);


-- 매장명별 -> 카테고리별 메뉴 갯수
SELECT R_NAME, M_CATE, COUNT(*)
FROM RESTAURANT r, MENU m
WHERE r.R_NO = m.M_R_NO
GROUP BY R_NAME, M_CATE
ORDER BY R_NAME, M_CATE;


-- 사장님 이름별 메뉴 평균가
-- 평균 구할 때, 가격이 6000원 미만인거는 빼고 구하자
SELECT C_NAME, AVG(M_PRICE)
FROM CEO c, MENU m, OPERATE o
WHERE m.M_R_NO = O_R_NO
AND c.C_NO = o.O_C_NO
AND M_PRICE >= 6000
GROUP BY C_NAME
ORDER BY C_NAME;

SELECT AVG(M_PRICE) FROM MENU;
SELECT AVG(M_PRICE) FROM (SELECT M_R_NO, M_PRICE FROM MENU WHERE M_PRICE < 8000);

-- 사장님 이름별 메뉴 평균가
-- 일단 메뉴 평균가 구하는데, 평균가가 6000원 미만인거 보기 싫다
-- 일단 평균을 계산 하고 -> 나온 결과값에서 6000원 미만이라면 표시를 하지 않음
-- HAVING 조건식 : GROUP BY '결과값'을 필터링
SELECT C_NAME, AVG(M_PRICE)
FROM CEO c, MENU m, OPERATE o
WHERE m.M_R_NO = O_R_NO
AND c.C_NO = o.O_C_NO
GROUP BY C_NAME
HAVING AVG(M_PRICE) >= 6000
ORDER BY C_NAME;


-- 사장 이름 별 매장 수
-- 테이블 수가 10개 미만인거는 뺴고
-- 매장 수가 2개 이상인 것만 보기
SELECT C_NAME, COUNT(O_R_NO)
FROM CEO c, OPERATE o, RESTAURANT r 
WHERE c.C_NO = o.O_C_NO
AND o.O_R_NO = r.R_NO
AND R_TABLE >= 10
GROUP BY C_NAME
HAVING COUNT(O_R_NO) >= 2
ORDER BY C_NAME
























