select  

Id as clics_db_id, 

FORMAT(StartDate,'yyyy-mm-dd') as start_date, 

FORMAT(EndDate,'yyyy-mm-dd') as end_date, 

EnrolProductId as enroll_product_id 

from EnrolProductInactiveCycles 

--clics_db_id,start_date,enroll_product_id 