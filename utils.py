import random, string
from fastapi import HTTPException
from sqlalchemy.orm import Session
import models

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_short_url(db: Session, original_url: str):
    short_code = generate_short_code()
    db_url = models.URL(short_code=short_code, original_url=original_url)
    db.add(db_url)
    db.commit()
    return {"short_url": f"http://localhost:8000/{short_code}"}

def get_original_url(db: Session, short_code: str):
    db_url = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    if db_url:
        return {"original_url": db_url.original_url}
    raise HTTPException(status_code=404, detail="Short URL not found")