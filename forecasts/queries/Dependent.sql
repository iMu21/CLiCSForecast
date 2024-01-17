SELECT  

Id as clics_db_id, 

EnrolId as enroll_id, 

CASE  

	WHEN Gender = 1 THEN 'M' 

	WHEN Gender = 2 THEN 'F' 

	ELSE 'O' 

END AS gender, 

DATE_FORMAT(Birthdate, '%Y-%m-%d') AS birth_date, 

DATE_FORMAT(EffectiveDate, '%Y-%m-%d') AS effective_date 

from EnrolDependents 
--clics_db_id,enroll_id,gender,birth_date,effective_date