# 1

def find_overage_active_employees(workers_list):
    NAME = 0
    AGE = 1
    WORKING_STATUS = 2
    overage_active_workers = []
    for worker in workers_list:
        if worker[AGE] >= 18 and worker[WORKING_STATUS]:
            overage_active_workers.append(worker[NAME])
    return overage_active_workers

lst_of_workers = [
    ["Dan", 25, False],
    ["Noa", 16, True],
    ["Yael", 30, False],
]

print(find_overage_active_employees(lst_of_workers))

# 2
# הפונקציה הבאה עושה יותר מדי דברים. פצלו אותה לפונקציות קטנות וממוקדות:
def validates_email(user_email):
    if not user_email:
        print("Invalid user")
        return None

def allowed_purchase_quantitiy(quantity,stock):
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return None

def calc_total_cost(quantity,product_price):
    price = product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85
    return price

def handle_stock(order_status,quantity):
    if order_status == "confirmed":
        stock -= quantity
        return

def handle_purchase(user_email, product_name, product_price, stock, quantity):
    # if not user_email:
    #     print("Invalid user")
    #     return None
    # if quantity <= 0 or quantity > stock:
    #     print("Invalid quantity")
    #     return None

    # price = product_price * quantity
    # if quantity >= 10:
    #     price *= 0.9
    # if quantity >= 50:
    #     price *= 0.85

    stock -= quantity

    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = price
    order_status = "confirmed"
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")
    return order_user, order_product, order_quantity, order_total, order_status

