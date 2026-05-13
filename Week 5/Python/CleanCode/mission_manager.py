
def mission_status_into_english(all_missions_lst = None):
    non_bool_missions = []
    for mission in all_missions_lst:
        non_bool_missions.append({
            'mission_name': mission["mission_name"],
            'level': mission["level"],
            'mission_completed': "Completed"  if mission["mission_completed"] else "Not Completed"
        })
    return non_bool_missions


def show_all_missions(all_missions = None):
    for mission in all_missions:
        print(mission)

def count_open_or_closed_missions(mission_list = None,open_missions = None):
    counter = 0
    for mission in mission_list:
        if mission['mission_completed']:
            counter += 1
    if open_missions:
        return counter
    else:
        return len(mission_list)-counter
    
def number_of_misisions(mission_lst = None):
    return len(mission_lst)

def number_of_urgent_missions(mission_lst = None):
    counter = 0
    for mission in mission_lst:
        if mission['level'] == "high":
            counter += 1
    return counter
    
def daily_summary(n_missions,n_open_missons,n_completeed_missions,n_urgennt_missions):
    print(f"Number of Missions: {n_missions}, Number of Open Missions: {n_open_missons}, Number of Completed Missions: {n_completeed_missions}, Number of Urgent Missions: {n_urgennt_missions}")


missions_list_bool_values =[{'mission_name': "Ruster call", 'level': "high", 'mission_completed': False},
                            {'mission_name': "Green night", 'level': "medium", 'mission_completed': False},
                            {'mission_name': "Rise", 'level': "low", 'mission_completed': False},
                            {'mission_name': "Yellow stone", 'level': "medium", 'mission_completed': False},
                            {'mission_name': "Clean house", 'level': "high", 'mission_completed': False},
                            {'mission_name': "Sharp edge", 'level': "low", 'mission_completed': False}
                            ]


# change the "mission completed" value from bool to English 
non_bool_mission_keys = mission_status_into_english(missions_list_bool_values)
# shows all missions
show_all_missions(non_bool_mission_keys)
# gets number of open mission
num_open_missions = count_open_or_closed_missions(missions_list_bool_values,1)
# counts number of completed missions
num_closed_missions = count_open_or_closed_missions(missions_list_bool_values,0)
# counts the amount missions rated high
num_urgent_missions = number_of_urgent_missions(missions_list_bool_values)
# shows the daily summary
num_of_missions = number_of_misisions(missions_list_bool_values)
daily_summary(num_of_missions,num_open_missions,num_closed_missions,num_urgent_missions)