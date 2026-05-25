import os

# 1
def load_tasks(filename):
    '''
    loads the file name and returns a list with all of lines of data stored as dicts
    '''
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as file:
        lst_of_dicts = []
        lst_of_lines = file.readlines()
        for line in lst_of_lines:
            split_line = line.split("|")
            lst_of_dicts.append({"id": split_line[0], "status":split_line[1], "desc": split_line[2]})
    return lst_of_dicts
        

# 2
"""
adds the task to the file 
"""
def save_tasks(filename, tasks):
    with open(filename, "a") as file:
        for line_d in tasks:
            file.write(f"{line_d[id]}|{line_d["status"]|{line_d["desc"]}}\n")


# 3
def add_task(filename, description):
    """
    adds a new task to the file
    """
    id = 0
    with open(filename, "r", encoding="utf-8") as r_file:
        if not os.path.exists(filename):
            return
        lst_of_lines = r_file.readlines()
        if lst_of_lines:
            last_line = lst_of_lines[-1]
            id,useless1,useless2 = last_line.split("|")
            id = int(id.strip())
    with open(filename, "a", encoding="utf-8") as w_file:
        w_file.write(f"{str(id + 1)}|PENDING|{description}\n")


# 4
def complete_task(filename, task_id):
    """
    updates file task to 'done'
    """
    index = 0
    with open(filename, "r", encoding="utf-8") as r_file:
        lines_in_lst = r_file.readlines()
        for i, value in enumerate(lines_in_lst):
            value = value.split("|")[0]
            if str(task_id) == value:
                index = i
                break
        lst_update = lines_in_lst.pop(index)
        id,useless,desc = lst_update.split("|")
        lines_in_lst.insert(index, f"{id}|DONE|{desc}")
    with open(filename, "w", encoding="utf-8") as w_file:
        w_file.writelines(lines_in_lst)


# 5
def list_tasks(filename):
    """
    prints tasks asthetically
    """
    with open(filename, "r", encoding="utf-8") as file:
        lst_of_lines = file.readlines()
    for line in lst_of_lines:
        id,status,desc = line.split("|")
        status = status.strip().lower()
        if status == "done":
            print(f"{desc.strip()} | {id} [✓]\n")
        else:
            print(f"{desc.strip()} | {id} [ ]\n")


# 6+
def remove_by_id(filename,id):
    """
    removes tasks from the file
    """
    index = 0
    with open(filename, "r", encoding="utf-8") as r_file:
        lines_in_lst = r_file.readlines()
        for i, value in enumerate(lines_in_lst):
            if str(id) == value[0]:
                index = i
                lines_in_lst.pop(index)
                break
    with open(filename, "w") as w_file:
        w_file.writelines(lines_in_lst)


def main():
    FILENAME = "tasks.txt"
    while True:
        print('\n=== To-Do List Manager ===')
        print('הצג משימות 1.')
        print('הוסף משימה 2.')
        print('סמן כהושלם 3.')
        print('4. Remove task')
        print('5. Exit')
        choice = input('בחירה:')
        if choice == '1':
            list_tasks(FILENAME)
        elif choice == '2':
            desc = input(' :תיאור המשימה')
            add_task(FILENAME, desc)
            print('!המשימה נוספה')
        elif choice == '3':
            task_id = int(input('משימה מספר:'))
            complete_task(FILENAME, task_id)
        elif choice == '4':
            id = int(input('משימה מספר:'))
            remove_by_id(FILENAME, id)
        elif choice == '5':
            print('!להתראות')
            break
        else:
            print('בחירה לא תקינה')
if __name__ == '__main__':
    main()