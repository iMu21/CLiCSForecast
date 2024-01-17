select  

Id as clics_db_id, 

GroupPolicyId as group_policy_id, 

ProductId as product_id, 

FORMAT(EffectiveDateUtc,'yyyy-mm-dd') as effective_date 

from GroupPolicyProducts 

--clics_db_id,group_policy_id,product_id,effective_date 