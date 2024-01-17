select 

id as clics_db_id, 

grouppolicyclusterid as group_policy_cluster_id, 

grouppolicyproductid as group_policy_product_id, 

FORMAT(EffectiveDateUtc,'yyyy-mm-dd') as effective_date 

from groupPolicyClusterProducts 

--clics_db_id,group_policy_cluster_id,group_policy_product_id,effective_date 