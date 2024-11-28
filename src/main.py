from fastapi import FastAPI
import uvicorn

from routers.task import task_router

app = FastAPI(title="To-Do List API")
app.include_router(task_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
