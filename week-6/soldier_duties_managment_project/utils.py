from data import all_soldiers_lst

def find_soldier_by_id(soldier_id: int) -> dict | None:
    """
    the function gets an id as an int if the soldier existst it returns the soldiers dict otherwise None
    """
    for soldier in all_soldiers_lst:
        if soldier_id in soldier.values():
            return soldier
        return None


def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    """
    the func searches for the duty by name (which is given as an str) inside of duties which is given as a list.
    if it is dfound it returns a dict otherwise None
    """
    for duty in duties:
        duty_d = duty.values()
        if duty_name in duty_d:
            return duty
        return None


def is_valid_status(status: str) -> bool:
    """
    the func checks if the status which is given as an str. it returns True or False accordingly 
    """
    status = status.lower()
    valid_status = ["pending","completed","missed"]
    if status in valid_status:
        return True
    return False


def is_valid_name(name: str) -> bool:
    """
    checks if the name (which is given as a str) if it is valid and returns True or False accordingly
    """
    if name:
        return True
    return False


def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    """
    the func gets the soldiers dict and his duty_name as an str and checks:
         if the soldier has the duty and retruns True or False accordingly
    """
    duty_lst = soldier.get("duties")
    for duty_d in duty_lst:
        if duty_name in duty_d.values():
            return True
    return False

def is_valid_day(day: str) -> bool:
    """
    the func gets the day as an str and checks if the day is a valid days choice and returns True or False accordingly
    """
    day = day.lower()
    valid_days = ["sunday","monday","tuesday","wedensday","thursday"]
    if day in valid_days:
        return True
    return False