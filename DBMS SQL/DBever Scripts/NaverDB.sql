


CREATE SEQUENCE COMPANY_SEQ;

SELECT * FROM SPV;

SELECT * FROM COMPANY;
INSERT INTO SPV VALUES({id}, '{M_NAME}', {M_PRICE}, '{M_MAKER}', '{C_LINK}', ROOP)
INSERT INTO COMPANY VALUES(ROOP, {id}, '{M_NAME}')

SELECT * FROM(
	SELECT ROWNUM AS RN, M_NO, M_NAME, M_PRICE, M_MAKER, C_LINK, M_C_NO FROM(
		SELECT M_NO, M_NAME, M_PRICE, M_MAKER, C_LINK, M_C_NO  FROM SPV WHERE M_C_NO IN (SELECT C_NO FROM COMPANY WHERE C_NAME = '네이버')
	)
)WHERE RN BETWEEN 3 AND 5;


SELECT * FROM COMPANY WHERE C_NAME IN (SELECT DISTINCT C_NAME FROM COMPANY WHERE C_NAME LIKE '%네%');