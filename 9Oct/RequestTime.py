from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
import time
import traceback

app = FastAPI()

# Setup logging
logging.basicConfig(level=logging.INFO)


# Custom middleware
@app.middleware("http")
async def process_time_middleware(request: Request, call_next):
    start_time = time.time()

    try:
        response = await call_next(request)
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

    process_time = time.time() - start_time
    formatted_time = f"{process_time:.4f}"
    response.headers["X-Process-Time"] = formatted_time

    logging.info(f"Request to {request.url.path} took {formatted_time} seconds")

    return response


# Sample endpoint
@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/ping")
async def ping():
    return {"message": "pong"}
