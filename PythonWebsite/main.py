from operator import truediv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str


app = FastAPI()

stock_db = [{"title": "Pepsi", "price": 26},{"title": "Lays", "price": 30}]
userInfo_db = {
"userData": [["test", "1234"], ["test2", "12345"]]
}

@app.get("/stock/")
async def get_stock():
    return stock_db
@app.get("/hello/")
async def root():
    return {"message": "Hello World"}
@app.get("/search/{item_id}")
async def search(item_id: int):

    return stock_db[item_id-1]

@app.post("/login")
async def handleLogin(user: UserLogin):
    for i in range(len(userInfo_db ["userData"])):
        if user.username == userInfo_db["userData"][i][0] and user.password == userInfo_db["userData"][i][0]:
            return {"result": "ยินดีต้อนรับเข้าสู่ระบบ"}
        return {"result": "คุณกรอกชื่อผู้ใช้หรือว่ารหัสผ่านไม่ถูกต้อง"}
app.mount("/", StaticFiles(directory="web"), name="web")