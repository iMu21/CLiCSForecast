def is_inactive_on_date(sorted_inactive_cycle,parent_id,date):
    if parent_id == None:
        return False       
    for cycle in sorted_inactive_cycle:
        if cycle.parent_id < parent_id:
            continue
        elif cycle.parent_id > parent_id:
            return False
        elif date < cycle.start_date:
            return False
        elif parent_id == cycle.parent_id and (
            (cycle.start_date <= date and cycle.end_date is None) or
            cycle.start_date <= date and date <= cycle.end_date):
            return True
        
    return False