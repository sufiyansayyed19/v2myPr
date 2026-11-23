from fastapi import FastAPI
from config.settings import settings
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/test/users")
def create_test_user(email: str, db: Session = Depends(get_db)):
    user = User(
        id="test-001",
        email=email
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "id": user.id,
        "email": user.email
    }