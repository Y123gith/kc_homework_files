from datetime import datetime
import logging
import json
import os

from shape import Shape
import shape
import rectangle, circle, hexagon, square, triangle


IDS_FILE = 'id.txt'
SHAPES_FILE = f'shapes{datetime.now().strftime("%d_%m_%y")}.json'

logger = logging.getLogger('shape_manager.py')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(message)s | %(levelname)s')
logger_handle = logging.StreamHandler()
logger_handle.setFormatter(formatter)
logger.addHandler(logger_handle)


class ShapeManager:
    @staticmethod
    def get_next_id() -> int:
        next_id = 1
        try:
            with open(IDS_FILE, 'r', encoding='utf-8') as f:
                next_id = int(f.read().strip())
        except (FileNotFoundError, ValueError) as e:
            logger.info("ID file not found or corrupted. Starting from 1.")
        
        with open(IDS_FILE, 'w', encoding='utf-8') as f:
            f.write(str(next_id+1))
        return next_id


    def __init__(self):
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape: Shape) -> None:
        self.shapes.append(shape)
        self.save_to_json()
        logger.info(f"Shape created successfully with ID: {shape.id}")


    def get_all_shapes(self) -> list:
        return [str(shape) for shape in self.shapes]
    

    def remove_shape(self, shape_id: int) -> None:
        undesired_shape = self.find_shape_by_id(shape_id)
        self.shapes.remove(undesired_shape)
        self.save_to_json()


    def total_arae(self):
        return sum(shape.get_area() for shape in self.shapes)


    def update_shape(self, shape_id, new_data) -> None:
        try:
            shape = self.find_shape_by_id(shape_id)
            for key, value in new_data.items():
                if not hasattr(shape, key):
                    raise KeyError(f"Error: Field '{key}' does not exist in {shape.shape_type}")
                
                setattr(shape, key, value)
                
            self.save_to_json()
            logger.info(f"Shape with ID {shape_id} was updated.")
        except KeyError as e:
            logger.error(f"Update failed: {e}")
            raise
        except (TypeError, ValueError) as e:
            logger.error(f"Validation error during update: {e}")
            raise

    def find_shape_by_id(self, shape_id) -> Shape:
        for shape in self.shapes:
            if shape.id == shape_id:
                return shape
        raise KeyError("Shape not found")

    def save_to_json(self) -> None:
        self.load_from_json
        with open(SHAPES_FILE, 'w', encoding='utf-8') as f:
            shapes = [s.to_dict() for s in self.shapes]
            json.dump(shapes, f, indent=4)

    def load_from_json(self, filename = SHAPES_FILE) -> None:
        try:
            with open (filename, 'r', encoding='utf-8') as f:
                shapes = json.load(f)
                for s in shapes:
                    shape = Shape.recreate_shape_from_dict(s)
                    if shape not in self.shapes:
                        self.shapes.append(shape) 
                logger.info(f"Loaded {len(self.shapes)} shapes from {filename}")
        except FileNotFoundError:
            self.shapes = []
            logger.info("No existing shapes file found. Starting with empty")
        except json.JSONDecodeError as e:
            self.shapes = []
            logger.error(f"Error reading JSON file: {e}")