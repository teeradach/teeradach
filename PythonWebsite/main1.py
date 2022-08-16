from fastapi import FastAPI
import math as m
app = FastAPI()
@app.get("/me")
async def getme():
	return {"name": "Natchapol","dob":"2000-08-28","email":"natchapol@lab.ai"}

@app.get("/sqrt/{number}")
async def getMath(number: int):
	number = m.sqrt(number)
	return {"result":number}