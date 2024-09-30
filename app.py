from fastapi import FastAPI
from routes import user_routes
from routes import route_routes
from routes import driver_routes

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(driver_routes.router)
app.include_router(route_routes.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


