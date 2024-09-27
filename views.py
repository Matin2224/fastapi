from typing import Any

from fastapi import UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

import dependencies
import schemas
from database import SessionLocal
from main import upload_image, app
from .models import Post, User


@app.post("/posts/")
def create_post(title: str, description: str, image: UploadFile = File(...)):
    db: Session = SessionLocal()

    image_data = upload_image(image)
    image_path = image_data['file_path']

    new_product = Post(name=title, description=description, image_url=image_path)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


@app.post("/signup", response_model=schemas.User, status_code=201)  # 1
def create_user_signup(
        *,
        db: Session = Depends(dependencies.get_db),  # 2
        user_in: schemas.UserRegister,  # 3
) -> Any:
    user = db.query(User).filter(User.username == user_in.username).first()  # 4
    if user:
        raise HTTPException(  # 5
            status_code=400,
            detail="The user with this email already exists in the system",
        )
    user = crud.user.create(db=db, obj_in=user_in)  # 6

    return user
