# from typing import Any, Dict, Optional, Union
#
# from sqlalchemy.orm import Session
#
# from crud.base import CRUDBase
# from models import User
# from schemas import UserRegister
#
#
#
# class CRUDUser(CRUDBase[User, UserRegister, UserUpdate]):
#     def get_by_email(self, db: Session, *, username: str) -> Optional[User]:
#         return db.query(User).filter(User.username == username).first()
#
#     def create(self, db: Session, *, obj_in: UserRegister) -> User:
#         create_data = obj_in.dict()
#         # create_data.pop("password")
#         db_obj = User(**create_data)
#         # db_obj.hashed_password = get_password_hash(obj_in.password)
#         db.add(db_obj)
#         db.commit()
#
#         return db_obj
#
#     # skipping...
#
# user = CRUDUser(User)
#
# from typing import Union
#
# from sqlalchemy.orm import Session
#
# from base import CRUDBase
# from models import Post
# from schemas. import RecipeCreate, RecipeUpdateRestricted, RecipeUpdate
#
#
# class CRUDRecipe(CRUDBase[Recipe, RecipeCreate, RecipeUpdate]):
#     def update(
#         self,
#         db: Session,
#         *,
#         db_obj: Recipe,
#         obj_in: Union[RecipeUpdate, RecipeUpdateRestricted]
#     ) -> Recipe:
#         db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
#         return db_obj
#
#
# recipe = CRUDRecipe(Recipe)