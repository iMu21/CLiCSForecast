
  select  

Id as clics_db_id, 

FORMAT(StartDate,'yyyy-mm-dd') as start_date, 

FORMAT(EndDate,'yyyy-mm-dd') as end_date, 

GroupPolicyClusterId as group_policy_cluster_id 

from GroupPolicyClusterInactiveCycles 

--clics_db_id,start_date,group_policy_cluster_id 