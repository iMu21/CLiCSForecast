select  

Id as clics_db_id, 

FORMAT(StartDate,'yyyy-mm-dd') as start_date, 

FORMAT(EndDate,'yyyy-mm-dd') as end_date, 

EnrolId as enroll_id 

from EnrolInactiveCycles 

--clics_db_id,start_date,enroll_id 