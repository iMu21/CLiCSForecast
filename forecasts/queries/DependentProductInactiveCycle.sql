select  

Id as clics_db_id, 

FORMAT(StartDate,'yyyy-MM-dd') as start_date, 

FORMAT(EndDate,'yyyy-MM-dd') as end_date, 

EnrollDependentProductId as dependent_product_id 

from EnrolDependentProductInactiveCycles 

--clics_db_id,start_date,dependent_product_id 