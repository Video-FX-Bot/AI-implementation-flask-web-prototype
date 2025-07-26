import uvicorn
from fastapi import FastAPI
from app.api import routes
from app.database.session import create_indexes

app = FastAPI()
app.include_router(routes.router)

@app.on_event("startup")
async def startup_event():
    await create_indexes()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
