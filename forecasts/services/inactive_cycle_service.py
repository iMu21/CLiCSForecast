def is_inactive_on_date(sorted_inactive_cycle,parent_id,date):
    if parent_id == None:
        return False
    fst = find_first_index(sorted_inactive_cycle,parent_id) 
    if fst==-1:
        return False
    en = len(sorted_inactive_cycle)      
    for i in range(fst,en):
        if sorted_inactive_cycle[i].parent_id > parent_id:
            return False
        elif date < sorted_inactive_cycle[i].start_date:
            return False
        elif parent_id == sorted_inactive_cycle[i].parent_id and (
            (sorted_inactive_cycle[i].start_date <= date and sorted_inactive_cycle[i].end_date is None) or
            sorted_inactive_cycle[i].start_date <= date and date <= sorted_inactive_cycle[i].end_date):
            return True
        
    return False

def find_first_index(sorted_inactive_cycle,parent_id):
    beg = int(0)
    en = len(sorted_inactive_cycle) - 1

    return binary_search(sorted_inactive_cycle,parent_id,beg,en)

def binary_search(sorted_inactive_cycle,parent_id,begg,enn):
    if begg>enn:
        return -1
    if begg == enn and sorted_inactive_cycle[begg].parent_id != parent_id:
        return -1
    
    if begg == enn and sorted_inactive_cycle[begg].parent_id == parent_id:
        return begg
    mid = (begg+enn)//2
    if parent_id<=sorted_inactive_cycle[mid].parent_id:
        return binary_search(sorted_inactive_cycle,parent_id,begg,mid)
    else:
        if mid==begg:
            mid+=1
        return binary_search(sorted_inactive_cycle,parent_id,mid,enn)