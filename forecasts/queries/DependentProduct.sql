select  

Id as clics_db_id, 

EnrollDependentId as dependent_id, 

ProductId as product_id, 

GroupPolicyClusterProductId as group_policy_cluster_product_id, 

CoverageAmount as coverage_amount, 

FORMAT(EffectiveDateUtc,'yyyy-MM-dd') as effective_date 

from EnrollDependentProducts 

--clics_db_id,dependent_id,product_id,group_policy_cluster_product_id,coverage_amount,effective_date 