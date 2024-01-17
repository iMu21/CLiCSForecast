select 

Id as clics_db_id, 

EnrolId as enroll_id, 

ProductId as product_id, 

groupPolicyclusterProductId as group_policy_cluster_product_id, 

CoverageAmount as coverage_amount, 

FORMAT(EffectiveDateUtc,'yyyy-mm-dd') as effective_date 

from EnrolProducts 

--clics_db_id,enroll_id,product_id,group_policy_cluster_product_id,coverage_amount,effective_date 