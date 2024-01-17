SELECT  

p.Id as clics_db_id, 

code as code, 

ct.PrefixNumber as claim_type, 

p.MaximumAge as maximum_age, 

CASE 

when ProductCategoryId =1 then 'CriticalIllness' 

when ProductCategoryId =2 then 'Accidental' 

when ProductCategoryId =3 then 'InHospital' 

when ProductCategoryId =4 then 'OrdinaryLife' 

when ProductCategoryId =5 then 'UniversalLife' 

when ProductCategoryId =6 then 'MonthlyBenefit' 

when ProductCategoryId =7 then 'Life' 

when ProductCategoryId =8 then 'Disability' 

when ProductCategoryId =9 then 'PA' 

else 'Others'  

End as product_category, 

case  

when Lob = 10 then 'Lob10' 

when Lob=20 then 'Lob20' 

when Lob = 40 then 'Lob40' 

else 'LobNull' 

end as lob 

from Products p 

join ClaimTypes ct on ct.Id=p.ClaimTypeId 

  

--clics_db_id,code,claim_type,maximum_age,product_category,lob 

 