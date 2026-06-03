import fastapi, requests,json

from shape_manager import ShapeManager
from shape import Shape

manager = ShapeManager()

app = fastapi.FastAPI()

@app.get("/shapes")
def all_shapes() -> list:
    return manager.get_all_shapes()


@app.get("/shapes/total-area")
def all_areas_sum() -> dict:
        return {"all areas sum" : manager.total_arae()}




@app.post("/shapes")
def add_shape(body: dict) -> None:
    try:
        new_shape = Shape.recreate_shape_from_dict(body)
        manager.create_shape(new_shape)
    except ValueError as e:
        raise fastapi.HTTPException(status_code=422, detail=e)
    

@app.put("/shapes/{id}")
def update_shapes_data(id, body: dict) -> None:
    try:
        manager.update_shape(id,body)
    except (ValueError, TypeError, KeyError) as e:
        raise fastapi.HTTPException(status_code=404, detail=e)


@app.delete("/shapes/{id}")
def delete_shape(id) -> None:
    try:
        manager.remove_shape(id)
    except KeyError as e:
        raise fastapi.HTTPException(status_code=404, detail=e)

@app.get("/shapes/{id}")
def shape_by_id(id: int = 1) -> dict:
    try:
        return manager.find_shape_by_id(id).to_dict()
    except KeyError as e:
        raise fastapi.HTTPException(status_code=404, detail=e)
    # return manager.find_shape_by_id(id).to_dict()