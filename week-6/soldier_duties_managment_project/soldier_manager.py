import utils, data

def add_soldier(soldier_id: int, name: str) -> None:
    """
    the func gets soldier_id (int) and name (str) and adds the soldier if it does npt already exist
    """
    soldier_d = utils.find_soldier_by_id(soldier_id)
    if soldier_d:
        raise ValueError
    if not utils.is_valid_name(name):
        raise ValueError
    new_soldier_d = {"id": soldier_id, "name": name, "duties": []}
    data.all_soldiers_lst.append(new_soldier_d)


def remove_soldier(soldier_id: int) -> None:
    """
    The func gets the soldier_d (int) and removes him from the list
    """
    soldier_d = utils.find_soldier_by_id(soldier_id)
    if not soldier_d:
        raise KeyError
    data.all_soldiers_lst.remove(soldier_d)

def get_all_soldiers() -> list:
    """
    the func rerturns the soldier list (list)
    """
    return data.all_soldiers_lst