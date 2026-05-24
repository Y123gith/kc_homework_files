import data, duty_manager, soldier_manager, utils
def show_menu() -> None:
    """
    מציגה את התפריט הראשי למשתמש.
    
    מקבלת: כלום
    מחזירה: כלום (מדפיסה לקונסול)
    
    למה הפונקציה קיימת:
    הפרדה בין הצגת התפריט לבין הלוגיקה העסקית.
    אם נרצה לשנות את התצוגה, נשנה רק כאן.
    """
    print("You Have The Following Options:", "1) Add A New Solder",
           "2) Remove A Soldier",
            "3) View All Soldiers Available",
            "4) Add A Duty To A Soldier",
            "5) Update Duty Status",
            "6) View A soldiers List of Duties",
            "7) Exit",
            sep = "\n")



def get_user_choice() -> str:
    """
    מקבלת בחירה מהמשתמש.
    
    מקבלת: כלום
    מחזירה: מחרוזת המייצגת את בחירת המשתמש
    
    למה הפונקציה קיימת:
    הפרדת קבלת קלט מהמשתמש מהלוגיקה של עיבוד הבחירה.
    מאפשר להחליף את שיטת הקלט בעתיד (למשל, GUI).
    """
    while True:
        try:
            user_choice = input("What do want to do: ")
            user_choice = int(user_choice)
            if 0 < user_choice < 8:
                return str(user_choice)
        except ValueError:
            print("You can only choose a number between 0 to 8")


def handle_add_soldier() -> None:
    """
    מטפלת בתהליך הוספת חייל חדש.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    מפרידה בין הקלט/פלט לבין הלוגיקה העסקית.
    main.py אחראי על אינטראקציה עם המשתמש,
    soldier_manager.py אחראי על הלוגיקה.
    """
    try:
        new_soldier_id = int(input("Please enter the id of the new soldier: "))
        new_soldier_name = input("Please enter the name of the new soldier: ")
        soldier_manager.add_soldier(new_soldier_id, new_soldier_name)
    except ValueError:
        print(f"either {new_soldier_id} is not an integer or the soldier already exists or that name is not valid")



def handle_remove_soldier() -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
       soldier_for_removal_id = int(input("Please enter the id of the soldier you want to remove: "))
       soldier_manager.remove_soldier(soldier_for_removal_id)
    except ValueError:
        print("Id is not an integer")
    except KeyError:
        print("Such an Id does not exist in the system")
    


def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    for soldier in soldier_manager.get_all_soldiers():
        print(soldier)


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id_duty = int(input("Please enter the id of the soldier you want to add a duty to: "))
        name_duty = input("Please enter the name of the duty you want to add to the soldier: ")
        day_duty = input("Please enter the day you want the duty to be: ")
        duty_manager.add_duty_to_soldier(soldier_id_duty, name_duty, day_duty)
    except ValueError:
        print(" Either Id is not an integer or day is invalid or this soldier has this duty already")
    except KeyError:
        print("No soldier with such an Id in the system")


def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id_duty = int(input("Please enter the id of the soldier you want to update the duty status to: "))
        duty_name = input("Please enter the name of the duty: ")
        new_status = input("Please enter the new status: ")
        duty_manager.update_duty_status(soldier_id_duty, duty_name, new_status)
    except ValueError:
        print("Either Id is not an integer or new duty is invalid")
    except KeyError:
        print("Either no soldier with such an Id or the soldier does not have such a duty")

def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id_duties = int(input("Please enter the id of the soldier you want to view the duties status: "))
        print(duty_manager.get_soldier_duties(soldier_id_duties))
    except ValueError:
        print("Id is not an integer")
    except KeyError:
        print("No soldier with such an Id")


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    while True:
        show_menu()
        user_choice = get_user_choice()
        match user_choice:
            case '1':
                handle_add_soldier()
            case '2':
                handle_remove_soldier()
            case '3':
                handle_view_soldiers()
            case '4':
                handle_add_duty()
            case '5':
                handle_update_duty_status()
            case '6':
                handle_view_soldier_duties()
            case '7':
                exit("GoodBye")

if __name__ == "__main__":
    main()