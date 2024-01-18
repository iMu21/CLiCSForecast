SELECT  

Id as clics_db_id, 

GroupPolicyId AS group_policy_id, 

CertificateNumber AS certificate_number, 

CASE  

	WHEN Gender = 1 THEN 'M' 

	WHEN Gender = 2 THEN 'F' 

	ELSE 'O' 

END AS gender, 

DATE_FORMAT(Birthdate, '%Y-%m-%d') AS birth_date, 

DATE_FORMAT(EffectiveDate, '%Y-%m-%d') AS effective_date, 

GroupPolicyClusterId AS group_policy_cluster_id 

FROM Enrols 