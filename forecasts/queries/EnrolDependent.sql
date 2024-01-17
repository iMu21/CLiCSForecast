select 

Id as clics_db_id, 

EnrolId as enroll_id, 

CASE 

	WHEN Gender = 1 then 'Male' 

	WHEN Gender = 1 then 'Female' 

	ELSE 'Other' 

END as gender, 

FORMAT(BirthDate,'yyyy-mm-dd') as birth_date, 

FORMAT(EffectiveDate,'yyyy-mm-dd') as effective_date 

from EnrolDependents 

--clics_db_id,enroll_id,gender,birth_date,effective_date 