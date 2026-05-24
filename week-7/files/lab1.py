def create_diary():
    with open("diary.txt", "w", encoding="utf-8") as file:
        file.write("2024-01-15: היה יום עמוס\n")
        file.write("2024-01-16: למדתי על file handeling ב- python\n")
        file.write("2024-01-17: השלמתי את התרגיל הראשון\n")
    print("היומן נוצר בהצלחה")
    with open ("diary.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line)

def add_entry(filename, date, content):
    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(filename + date + content)
    
    with open ("diary.txt", "r", encoding = "utf-8") as file:
        for line in file:
            print(line)

create_diary()
add_entry("txt.diary","2024-01-18","! יום נפלא — סיימתי תרגיל 1")

def search_diary(filename, keyword):
    new_lst = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if keyword in line:
                new_lst.append(line)
        return new_lst

lst = search_diary("diary.txt", "תרגיל")
for line in lst:
    print(line)