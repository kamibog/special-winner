from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def post_user(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]
) -> str:
    new_id = str(int(max(users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[str, Path(description="Enter User ID")],
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]
) -> str:
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is updated"
    return f"User {user_id} not found"

@app.delete("/user/{user_id}")
async def delete_user(
    user_id: Annotated[str, Path(description="Enter User ID")]
) -> str:
    if user_id in users:
        users.pop(user_id)
        return f"User {user_id} has been deleted"
    return f"User {user_id} not found"

