select  

Id as clics_db_id, 

FORMAT(StartDate,'yyyy-mm-dd') as start_date, 

FORMAT(EndDate,'yyyy-mm-dd') as end_date, 

GroupPolicyId as group_policy_id 

from GroupPolicyInactiveCycles 

--clics_db_id,start_date,group_policy_id 