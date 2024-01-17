select  

Id as clics_db_id, 

FORMAT(StartDate,'yyyy-mm-dd') as start_date, 

FORMAT(EndDate,'yyyy-mm-dd') as end_date, 

EnrolDependentId as dependent_id 

from EnrolDependentInactiveCycles 

--clics_db_id,start_date,dependent_id 