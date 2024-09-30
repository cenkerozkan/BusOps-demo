# BusOps-backend

BusOps-backend is a FastAPI-based backend service for managing bus operations, including drivers, vehicles, and routes.

## Endpoints

### 1. Create User

Creates a new user, which can be a driver or a regular user.

- **URL**: `/users`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "john.doe@example.com",
    "name": "John",
    "surname": "Doe",
    "mobile_phone": "+1234567890",
    "user_type": "driver",
    "is_driver": true
  }
  ```
- **Success Response**:
  - **Code**: 200
  - **Content**: `{"message": "User created successfully", "uuid": "123e4567-e89b-12d3-a456-426614174000"}`

### 2. Get All Drivers with Vehicles

Retrieves all drivers along with their assigned vehicles.

- **URL**: `/drivers`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200
  - **Content**:
    ```json
    {
      "drivers": [
        {
          "uuid": "123e4567-e89b-12d3-a456-426614174000",
          "name": "John",
          "surname": "Doe",
          "email": "john.doe@example.com",
          "mobile_phone": "+1234567890",
          "vehicles": [
            {
              "id": 1,
              "plate": "ABC123",
              "capacity": 50,
              "route": {...}
            }
          ]
        }
      ]
    }
    ```

### 3. Update Driver Route

Updates the route for a specific driver's bus.

- **URL**: `/routes`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "driver_uuid": "123e4567-e89b-12d3-a456-426614174000",
    "route": {
      "name": "Route 1",
      "stops": [
        {"latitude": 40.7128, "longitude": -74.0060, "name": "Stop 1"},
        {"latitude": 40.7129, "longitude": -74.0061, "name": "Stop 2"}
      ]
    }
  }
  ```
- **Success Response**:
  - **Code**: 200
  - **Content**: `{"message": "Route updated successfully", "bus_id": 1}`

### 4. Get All Drivers and Buses

Retrieves all drivers and buses in a single request.

- **URL**: `/drivers-and-buses`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200
  - **Content**:
    ```json
    {
      "drivers": [
        {
          "uuid": "123e4567-e89b-12d3-a456-426614174000",
          "name": "John",
          "surname": "Doe",
          "email": "john.doe@example.com",
          "mobile_phone": "+1234567890"
        }
      ],
      "buses": [
        {
          "id": 1,
          "plate": "ABC123",
          "capacity": 50,
          "route": {...},
          "driver_uuid": "123e4567-e89b-12d3-a456-426614174000"
        }
      ]
    }
    ```

### 5. Get Driver Details

Retrieves detailed information about a specific driver, including their vehicle and route.

- **URL**: `/drivers/{driver_uuid}`
- **Method**: `GET`
- **URL Parameters**: `driver_uuid=[string]`
- **Success Response**:
  - **Code**: 200
  - **Content**:
    ```json
    {
      "uuid": "123e4567-e89b-12d3-a456-426614174000",
      "name": "John",
      "surname": "Doe",
      "email": "john.doe@example.com",
      "mobile_phone": "+1234567890",
      "vehicle": {
        "id": 1,
        "plate": "ABC123",
        "capacity": 50,
        "route": {...}
      }
    }
    ```

## Setup and Running

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your environment variables in a `.env` file
4. Run the server: `uvicorn app:app --reload`

## Docker

To run the application using Docker:

1. Build the Docker image: `docker build -t busops-backend .`
2. Run the container: `docker run -p 8000:8000 busops-backend`

Alternatively, use Docker Compose:

```
docker-compose up --build
```

The API will be available at `http://localhost:8000`.

## API Documentation

Once the server is running, you can access the auto-generated API documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`