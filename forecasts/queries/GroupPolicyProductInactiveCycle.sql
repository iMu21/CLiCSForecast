select  

Id as clics_db_id, 

FORMAT(StartDate,'yyyy-mm-dd') as start_date, 

FORMAT(EndDate,'yyyy-mm-dd') as end_date, 

GroupPolicyProductId as group_policy_product_id 

from GroupPolicyProductInactiveCycles 

--clics_db_id,start_date,group_policy_product_id 