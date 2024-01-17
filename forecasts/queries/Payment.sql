select  

p.Id as clics_db_id, 

c.id as claim_entry_id, 

ClaimAmount as claim_amount, 

PayableAmount as payable_amount 

from PaymentQueues p 

join ClaimEntries c on c.ClaimNumber = p.ClaimNumber 

--clics_db_id,claim_entry_id,claim_amount,payable_amount 