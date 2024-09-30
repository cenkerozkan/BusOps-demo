from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from crud.route_crud import update_driver_route

router = APIRouter()

class RouteUpdate(BaseModel):
    driver_uuid: str
    route: dict

@router.put("/routes")
async def update_route(route_data: RouteUpdate):
    try:
        bus_id = await update_driver_route(route_data.driver_uuid, route_data.route)
        return {"message": "Route updated successfully", "bus_id": bus_id}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
