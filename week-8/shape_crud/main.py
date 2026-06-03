from shape_manager import ShapeManager
from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle
from hexagon import Hexagon

def main():
    manager = ShapeManager()
    shapes_map = {
        '1': (Circle, ['radius']),
        '2': (Rectangle, ['width', 'height']),
        '3': (Square, ['side']),
        '4': (Triangle, ['side_a', 'side_b', 'side_c']),
        '5': (Hexagon, ['side'])
    }

    while True:
        print("\n--- Menu ---")
        print("1. Add Shape\n2. View All\n3. Update Shape\n4. Exit")
        choice = input("Select option: ")

        if choice == '1':
            print("1.Circle 2.Rectangle 3.Square 4.Triangle 5.Hexagon")
            s_type = input("Select shape: ")
            if s_type in shapes_map:
                cls, fields = shapes_map[s_type]
                try:
                    kwargs = {f: float(input(f"Enter {f}: ")) for f in fields}
                    kwargs['id'] = ShapeManager.get_next_id()
                    manager.create_shape(cls(**kwargs))
                except Exception as e:
                    print(e)

        elif choice == '2':
            for shape in manager.get_all_shapes():
                print(shape)

        elif choice == '3':
            try:
                s_id = int(input("Enter shape ID: "))
                field = input("Enter field to update: ")
                val = float(input("Enter new value: "))
                manager.update_shape(s_id, {field: val})
            except Exception as e:
                print(e)

        elif choice == '4':
            break

if __name__ == "__main__":
    main()