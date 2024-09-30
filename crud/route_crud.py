from services.db_session import execute_query
from fastapi import HTTPException
import json

async def update_driver_route(driver_uuid: str, route_data: dict):
    update_query = """
    UPDATE buses
    SET route = %s
    WHERE driver_uuid = %s
    RETURNING id;
    """
    
    try:
        route_json = json.dumps(route_data)
        result = await execute_query(update_query, (route_json, driver_uuid))
        
        if not result:
            raise HTTPException(status_code=404, detail="Driver or bus not found")
        
        return result[0]['id']
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
