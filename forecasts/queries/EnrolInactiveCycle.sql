select  

Id as clics_db_id, 

FORMAT(StartDate,'yyyy-MM-dd') as start_date, 

FORMAT(EndDate,'yyyy-MM-dd') as end_date, 

EnrolId as enroll_id 

from EnrolInactiveCycles 

--clics_db_id,start_date,end_date,enroll_id 