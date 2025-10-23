from fastapi import APIRouter,status,HTTPException
from passlib.context import CryptContext
from models.users import User
from odmantic import AIOEngine
from pydantic import BaseModel,EmailStr

router = APIRouter(prefix="/users", tags=["Users"])
engine=AIOEngine()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class userCreate(BaseModel):
    firstname:str
    lastname:str
    email:EmailStr
    password:str

@router.get("/")
def get_users():
    #A dummy
    return [{"id": 1, "name": "John Doe"}]


@router.post("/createuser",status_code=status.HTTP_201_CREATED)
async def CreateUser(user:userCreate):
    try:
        existing_user=await  engine.find_one(User,User.email==user.email)
        if(existing_user):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists"
            )
        
        hashed_password=pwd_context.hash(user.password)

        new_User=User(
            first_name=user.firstname,
            last_name=user.lastname,
            email=user.email,
            password_hash=hashed_password
        )

        await engine.save(new_User)

        return {
            "message": "User created successfully",
            "user": {
                "id": str(new_User.id),
                "first_name": new_User.first_name,
                "last_name": new_User.last_name,
                "email": new_User.email
            }
        }
    except HTTPException as httperror:
        raise httperror
    except Exception as e:
        # Catch any unexpected error
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )
        





    
