select  

Id as clics_db_id, 

FORMAT(StartDate,'yyyy-MM-dd') as start_date, 

FORMAT(EndDate,'yyyy-MM-dd') as end_date, 

GroupPolicyClusterProductId as group_policy_cluster_product_id 

from GroupPolicyClusterProductInactiveCycles 

--clics_db_id,start_date,end_date,group_policy_cluster_product_id 