from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse

app = FastAPI()


@app.get("/")
async def hello():
	return "Hello World"


@app.get("/test/{num}")
async def test(num: int):
	response = {
		"message": f"Your num is {num}"
	}

	return JSONResponse(response)
