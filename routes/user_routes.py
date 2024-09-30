from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from crud.user_crud import create_user

router = APIRouter()

class UserCreate(BaseModel):
    email: str
    name: str
    surname: str
    mobile_phone: str
    user_type: str
    is_driver: bool = False

@router.post("/users")
async def create_user_route(user: UserCreate):
    try:
        user_uuid = await create_user(user)
        return {"message": "User created successfully", "uuid": user_uuid}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
