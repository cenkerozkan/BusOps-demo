from services.db_session import execute_query, execute_transaction
import uuid
from fastapi import HTTPException

async def create_user(user_data):
    user_uuid = uuid.uuid4()
    
    user_query = """
    INSERT INTO users (uuid, email, name, surname, mobile_phone, user_type)
    VALUES (%s, %s, %s, %s, %s, %s)
    RETURNING uuid;
    """
    user_values = (str(user_uuid), user_data.email, user_data.name, user_data.surname, user_data.mobile_phone, user_data.user_type)
    
    try:
        if user_data.is_driver:
            driver_query = """
            INSERT INTO drivers (id, name, surname)
            VALUES (%s, %s, %s)
            """
            driver_values = (str(user_uuid), user_data.name, user_data.surname)
            
            queries = [
                (user_query, user_values),
                (driver_query, driver_values)
            ]
            await execute_transaction(queries)
        else:
            await execute_query(user_query, user_values)
        
        return str(user_uuid)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
