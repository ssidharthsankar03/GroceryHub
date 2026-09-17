from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api.v1.router import api_router
from app.db.session import get_db


app = FastAPI(
    title="GroceryHub API",
    version="1.0.0",
)

app.include_router(
    api_router,
    prefix="/api/v1",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/health/db")
def database_health_check(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT current_database(), current_user"))
    database, user = result.fetchone()

    return {
        "status": "ok",
        "database": database,
        "user": user,
    }