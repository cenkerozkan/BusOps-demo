from services.db_session import execute_query
from fastapi import HTTPException

async def get_all_drivers_with_vehicles():
    query = """
    SELECT 
        u.uuid, u.name, u.surname, u.email, u.mobile_phone,
        b.id AS bus_id, b.plate, b.capacity, b.route
    FROM 
        users u
    JOIN 
        drivers d ON u.uuid = d.id
    LEFT JOIN 
        buses b ON u.uuid = b.driver_uuid
    WHERE 
        u.user_type = 'driver'
    """
    
    try:
        results = await execute_query(query)
        
        drivers = {}
        for row in results:
            driver_uuid = row['uuid']
            if driver_uuid not in drivers:
                drivers[driver_uuid] = {
                    'uuid': driver_uuid,
                    'name': row['name'],
                    'surname': row['surname'],
                    'email': row['email'],
                    'mobile_phone': row['mobile_phone'],
                    'vehicles': []
                }
            
            if row['bus_id']:
                drivers[driver_uuid]['vehicles'].append({
                    'id': row['bus_id'],
                    'plate': row['plate'],
                    'capacity': row['capacity'],
                    'route': row['route']
                })
        
        return list(drivers.values())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



async def get_all_drivers_and_buses():
    query = """
    SELECT 
        u.uuid, u.name, u.surname, u.email, u.mobile_phone,
        b.id AS bus_id, b.plate, b.capacity, b.route
    FROM 
        users u
    LEFT JOIN 
        drivers d ON u.uuid = d.id
    LEFT JOIN 
        buses b ON u.uuid = b.driver_uuid
    WHERE 
        u.user_type = 'driver'
    """
    
    try:
        results = await execute_query(query)
        
        drivers_and_buses = {
            "drivers": [],
            "buses": []
        }
        
        for row in results:
            driver = {
                'uuid': row['uuid'],
                'name': row['name'],
                'surname': row['surname'],
                'email': row['email'],
                'mobile_phone': row['mobile_phone']
            }
            if driver not in drivers_and_buses["drivers"]:
                drivers_and_buses["drivers"].append(driver)
            
            if row['bus_id']:
                bus = {
                    'id': row['bus_id'],
                    'plate': row['plate'],
                    'capacity': row['capacity'],
                    'route': row['route'],
                    'driver_uuid': row['uuid']
                }
                if bus not in drivers_and_buses["buses"]:
                    drivers_and_buses["buses"].append(bus)
        
        return drivers_and_buses
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_driver_vehicle_and_route(driver_uuid: str):
    query = """
    SELECT 
        u.uuid, u.name, u.surname, u.email, u.mobile_phone,
        b.id AS bus_id, b.plate, b.capacity, b.route
    FROM 
        users u
    JOIN 
        drivers d ON u.uuid = d.id
    LEFT JOIN 
        buses b ON u.uuid = b.driver_uuid
    WHERE 
        u.uuid = %s AND u.user_type = 'driver'
    """
    
    try:
        results = await execute_query(query, (driver_uuid,))
        
        if not results:
            raise HTTPException(status_code=404, detail="Driver not found")
        
        driver_info = {
            'uuid': results[0]['uuid'],
            'name': results[0]['name'],
            'surname': results[0]['surname'],
            'email': results[0]['email'],
            'mobile_phone': results[0]['mobile_phone'],
            'vehicle': None
        }
        
        if results[0]['bus_id']:
            driver_info['vehicle'] = {
                'id': results[0]['bus_id'],
                'plate': results[0]['plate'],
                'capacity': results[0]['capacity'],
                'route': results[0]['route']
            }
        
        return driver_info
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
