//IN
SELECT * FROM emp WHERE dept IN ('HR','IT') AND SALARY>3000;

//OR
SELECT * FROM emp WHERE dept = 'HR' OR dept = 'IT';

//AND
SELECT * FROM emp WHERE dept = 'HR' AND SALARY>30000;

//NOT
SELECT * FROM emp WHERE dept = 'HR' AND NOT SALARY>30000;

//BETWEEN 
SELECT * FROM emp WHERE salary BETWEEN 20000 AND 40000;

//DISTINCT
SELECT DISTINCT dept FROM emp;

//ORDER BY 
SELECT * FROM empt ODER BY salary;
SELECT * FROM empt ODER BY salary DESC;
SELECT fname FROM emp ORDER BY salary;
SELECT fname FROM emp ORDER BY salary DESC ;

//LIKE
SELECT * FROM emp WHERE fname LIKE '%a';  ends with a
SELECT * FROM emp WHERE fname LIKE 'a%';  start with a  
SELECT * FROM emp WHERE fname LIKE '%a%'; in between a   this can give omkar 
SELECT * FROM emp WHERE fname LIKE '_%ar%_'; exact in between of and word, this will not give omkar
SELECT * FROM emp WHERE fname LIKE 'a__'; exact three latters and start with a
SELECT * FROM emp WHERE fname LIKE '__'; exact 2 letters
SELECT * FROM emp WHERE fname LIKE '_a_' exact 3 letters with middle a
SELECT * FROM emp WHERE fname LIKE 'a%a'; start with a and end with a

//ILIKE
SELECT * FROM emp WHERE fname ILIKE '%A'; it will not follow case-sensitive will also give results with A

//NOT LIKE 
SELECT * FROM emp WHERE fname NOT LIKE '%a'; it will give all names which does not end with a also give name which ends with a but a should be A



