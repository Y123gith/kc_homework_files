import utils

def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str) -> None:
    """
    the func gets soldier_id (int), duty_name(str) and day(str) and adds the duty to the soldier
    """

    soldier_d = utils.find_soldier_by_id(soldier_id)
    if not soldier_d:
        raise KeyError
    if utils.soldier_has_duty(soldier_d, duty_name):
        raise ValueError
    if not utils.is_valid_day(day):
        raise ValueError
    soldier_duties = soldier_d.get("duties")
    new_duties_d = {"name": duty_name, "day": day, "status": "pending"}
    soldier_duties.append(new_duties_d)



def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    """
    the func gets soldier_id(int), duty_name(str) and new_status(str) and updates the soldiers statsus of the given duty
    """
    soldier_d = utils.find_soldier_by_id(soldier_id)
    if not soldier_d:
        raise KeyError
    if not utils.soldier_has_duty(soldier_d, duty_name):
        raise KeyError
    if not utils.is_valid_status(new_status):
        raise ValueError
    soldier_duties = soldier_d.get("duties")
    for duty_d in soldier_duties:
        if duty_d["name"] == duty_name:
            duty_d["status"] = new_status
            

def get_soldier_duties(soldier_id: int) -> list:
    """
    the func gets the soldier_id(int) and returns the list(list) containing all of his duties
    """
    soldier_d = utils.find_soldier_by_id(soldier_id)
    if not soldier_d:
        raise KeyError
    return soldier_d["duties"]