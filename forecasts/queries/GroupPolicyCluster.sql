select 

id as clics_db_id, 

grouppolicyid as group_policy_id, 

FORMAT(EffectiveDateUtc,'yyyy-mm-dd') as effective_date 

from GroupPolicyClusters 

--clics_db_id,group_policy_id,effective_date 