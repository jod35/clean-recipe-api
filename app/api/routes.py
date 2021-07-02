from fastapi import FastAPI,HTTPException,Depends
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.sql.functions import current_user
from starlette import status
from ..models.database import Base, Session
from ..models.recipes import User,Recipe
from pydantic import BaseModel
from typing import List
from passlib.hash import pbkdf2_sha256
from fastapi_jwt_auth import AuthJWT


app=FastAPI()

class UserSchema(BaseModel):
    username:str
    email:str
    passwd_hash:str

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "username":"johndoe123",
                "email":"johndoe1234",
                "password":"password"
            }
        }

class LoginSchema(BaseModel):
    username:str
    password:str

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "username":"username",
                "password":"password"
            }
        }

class UserLogin(BaseModel):
    username:str
    password:str

    class Config:
        schema_extra={
            "example":{
                "username":"username",
                "password":"password"
            }
        }


class RecipeSchema(BaseModel):
    title:str
    preparation_time:int
    description:str


    class Config:
        orm_mode=True


    
class Settings(BaseModel):
    authjwt_secret_key='1fc97ba2a7d57e24e777631b'


@AuthJWT.load_config
def get_config():
    return Settings()

db=Session()


@app.get('/users')
def get_all_users():
    
    users=db.query(User).all()

    return users


@app.post('/signup',status_code=201)
def create_new_user(user:UserSchema):
    """
    # Sign Up a user
    - This creates a user using this schema
    ```
            {
                "username":"johndoe123",
                "email":"johndoe1234",
                "password":"password"
            }
    
    ```
    
    """

    db_user=db.query(User).filter(User.username==user.username).first()


    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User already exists with username {user.username}"
        )
    new_user=User(
        username=user.username,
        email=user.email,
        passwd_hash=pbkdf2_sha256.hash(user.passwd_hash)
    )


    db.add(new_user)
    db.commit()

    return {"message":"Account Created Successfully"}


@app.post('/login',status_code=200)
def login(user:UserLogin,Authorize:AuthJWT=Depends()):
    """
       # Login a user
       This helps you to get access and refresh token.
       All you need to provide is

       ```
            {
                "username":"username",
                "password":"password"
            }
       ```
    """
    db_user=db.query(User).filter(User.username==user.username).first()

    if db_user and db_user.check_password(user.password):
        access_token=Authorize.create_access_token(subject=user.username)
        refresh_token=Authorize.create_refresh_token(subject=user.username)

        return {
            "access_token":access_token,
            "refresh_token":refresh_token
        }

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid Username Or Password"
    )

@app.post('/recipes',status_code=status.HTTP_201_CREATED)
def create_recipe(recipe:RecipeSchema,Authorize:AuthJWT=Depends()):

    """
        # Create a recipe 

        This creates recipe and all you need is a schema

        ```  
        {        
                "username":"johndoe123",
                "email":"johndoe1234",
                "password":"password"
            }
        ```
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )

    current_user=Authorize.get_jwt_subject()

    db_user=db.query(User).filter(User.username==current_user).first()

    new_recipe=Recipe(
        title=recipe.title,
        description=recipe.description,
        preparation_time=recipe.preparation_time,
        user=db_user
    )

    db.add(new_recipe)
    db.commit()

    return {"message":"Recipe Added"}


@app.get('/recipes',status_code=200,response_model=List[RecipeSchema])
def get_all_recipes():
    """
        # Get all recipes
        Returns a list of all items
    
    """
    recipes=db.query(Recipe).all()

    return recipes



@app.get('/recipe/{recipe_id}',status_code=200,response_model=RecipeSchema)
def get_recipe(recipe_id:int,Authorize:AuthJWT=Depends()):

    """
        # Get a recipe by its ID

        It requires an ID of a recipe
    """

    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please Provide a valid Token"
        )
        
    recipe=db.query(Recipe).filter(Recipe.id ==recipe_id).first()

    if recipe is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not found")
    return recipe


@app.put('/recipe/{recipe_id}',status_code=200,response_model=RecipeSchema)
def update_a_recipe(recipe_id:int,recipe:RecipeSchema,Authorize:AuthJWT=Depends()):
    """
        # Update a recipe
        - This updates a recipe by its ID
        - You will need to provide a a schema having your update data

        ```
            {
                "title":"title",
                "description":"description",
                "preparation_time":"preparation_time"
            }

        ```
    
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=401,detail="Please provide a valid token")


    db_recipe=db.query(Recipe).filter(Recipe.id==recipe_id).first()

    db_recipe.preparation_time=recipe.preparation_time
    db_recipe.title=recipe.title
    db_recipe.description=recipe.description

    db.commit()

    return db_recipe


@app.delete('/recipe/{recipe_id}',status_code=200,response_model=RecipeSchema)
def delete_a_recipe(recipe_id:int,Authorize:AuthJWT=Depends()):
    """
        # Delete a recipe
        - All you need is to provide a recipe_id within the URL
    """

    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=401,detail="Please provide a valid token")

    db_recipe=db.query(Recipe).filter(Recipe.id == recipe_id).first()

    db.delete(db_recipe) 

    db.commit()

    return db_recipe   

    


