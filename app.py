from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database, utils

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/shorten/")
def shorten_url(url: str, db: Session = Depends(database.get_db)):
    return utils.create_short_url(db, url)

@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(database.get_db)):
    return utils.get_original_url(db, short_code)