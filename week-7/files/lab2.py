# 1
def create_grades_file(filename):
    students = [
    ("Dan", [85, 90, 78]),
    ("MOMO", [92, 88, 95]),
    ("Yoni", [70, 65, 80]),
    ("Avi", [100, 95, 98]),
    ("Sara", [60, 72, 68]),
    ]
    with open(filename, "a", encoding="utf-8") as file:
        for line in students:
            name, grades_lst = line[0],",".join([str(number) for number in line[1]])
            file.write(name + ",")
            file.writelines(grades_lst)
            file.write("\n")
create_grades_file("grades.txt")


# 2
def calculate_averages(filename):
    averages = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            lst_of_grades = line.split(",")
            name, *grades = lst_of_grades
            averages[name] = round(sum([int(grade) for grade in grades])/len(grades), 1)     
    return averages

results = calculate_averages('grades.txt')
for name, avg in results.items():
    print(f'{name}: {avg:.1f}')


# 3
def save_results(averages, output_filename):
    with open(output_filename, "a") as file:
        file.write("=== Student Results ===\n")     
        avrg_values_lst = list(averages.values())
        avrg_values_lst.sort(reverse=True)
        for grade in avrg_values_lst:
            for key,value in averages.items():
                if value == grade:
                    file.write(f"{key}:{value}\n")


averages = calculate_averages('grades.txt')
save_results(averages, 'results.txt')

def result_stats(averages, output_filename):
    with open(output_filename, "a") as file:
        file.write("=== Statistics ===\n") 
        avrg_values_lst = list(averages.values())
        avrg_grade = sum(avrg_values_lst)/ len(avrg_values_lst)
        file.write(f"Class average: {avrg_grade}\n") 
        top_grade = max(avrg_values_lst)
        lowest_grade = min(avrg_values_lst)
        for key,value in averages.items():
            if value == top_grade:
                file.write(f"Highest: {key} ({value})\n")
            if value == lowest_grade:
                file.write(f"Highest: {key} ({value})\n")
        counter = 0
        for grade in avrg_values_lst:
            if int(grade) >= 60:
                counter += 1
        file.write(f"Passing (>=60): {counter}/{len(avrg_values_lst)}\n")


result_stats(averages, 'results.txt')