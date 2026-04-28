from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core import security
from app.core.logger import logger


def create_user(db: Session, user_in: UserCreate):
    hashed_pw = security.get_password_hash(user_in.password)
    
    data_obj = User(
        surname=user_in.surname,
        name=user_in.name,
        middleName=user_in.middleName,
        sex=user_in.sex,
        birthday=user_in.birthday,
        email=user_in.email,
        hashed_password=hashed_pw
    )
    logger.debug("created user similar model user")
    
    try:
        db.add(data_obj)
        db.commit()
        db.refresh(data_obj)
        logger.info(f"User created successfully: {data_obj.email}")
        return data_obj
    
    except Exception as e:
        db.rollback()
        logger.error(f"Database error during user creation: {e}")
        raise e
