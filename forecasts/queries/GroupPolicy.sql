SELECT  

Id as clics_db_id, 

GroupNumber as group_number, 

CASE  

	WHEN PremiumPaymentType = 1 THEN 'Monthly' 

	WHEN PremiumPaymentType = 2 THEN 'Quarterly' 

	WHEN PremiumPaymentType = 3 THEN 'Semi-Annually' 

	ELSE 'Annually' 

END AS premium_payment_type, 

CASE  

	WHEN GroupPolicyType = 1 THEN 'Group' 

	ELSE 'Bancassurance' 

END AS group_policy_type, 

CASE  

	WHEN Category = 1 THEN 'Local' 

	ELSE 'MultiNational' 

END AS category, 

CASE  

	WHEN GroupType = 1 THEN 'ASO' 

	WHEN GroupType = 2 THEN 'Standard' 

	ELSE 'SME' 

END AS group_type, 

DATE_FORMAT(EffectiveDateUtc, '%Y-%m-%d') AS effective_date 

FROM GroupPolicies 

--clics_db_id,group_number,premium_payment_type,group_policy_type,category,group_type,effective_date