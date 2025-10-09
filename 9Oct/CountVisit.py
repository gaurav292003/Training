from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
import time
import traceback

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Dictionary to store visit counts
visit_counter = {}


# Custom middleware
@app.middleware("http")
async def count_visits_middleware(request: Request, call_next):
    start_time = time.time()
    path = request.url.path

    # Count the number of visits per path
    visit_counter[path] = visit_counter.get(path, 0) + 1

    try:
        response = await call_next(request)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

    process_time = time.time() - start_time
    logging.info(f"Path: {path} | Visits: {visit_counter[path]} | Time taken: {process_time:.4f}s")

    return response


# Sample endpoints
@app.get("/")
async def root():
    return {"message": "Welcome!", "visits": visit_counter.get("/", 0)}


@app.get("/about")
async def about():
    return {"message": "This is the about page.", "visits": visit_counter.get("/about", 0)}


@app.get("/stats")
async def stats():
    return visit_counter
