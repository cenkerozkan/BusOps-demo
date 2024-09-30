from fastapi import APIRouter, HTTPException
from crud.driver_crud import get_all_drivers_with_vehicles, get_all_drivers_and_buses, get_driver_vehicle_and_route

router = APIRouter()

@router.get("/drivers")
async def get_drivers_with_vehicles():
    try:
        drivers = await get_all_drivers_with_vehicles()
        return {"drivers": drivers}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/drivers-and-buses")
async def get_drivers_and_buses():
    try:
        data = await get_all_drivers_and_buses()
        return data
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/drivers/{driver_uuid}")
async def get_driver_details(driver_uuid: str):
    try:
        driver_info = await get_driver_vehicle_and_route(driver_uuid)
        return driver_info
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
