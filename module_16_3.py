from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def post_user(username: str, age: int) -> str:
    new_id = str(int(max(users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int) -> str:
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is updated"
    return f"User {user_id} not found"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    if user_id in users:
        users.pop(user_id)
        return f"User {user_id} has been deleted"
    return f"User {user_id} not found"
