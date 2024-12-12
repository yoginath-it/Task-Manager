from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from app.routes import auth, tasks
from app.database import create_tables

# Initialize the FastAPI app
app = FastAPI()

# OAuth2PasswordBearer setup (used in dependencies for authentication)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@app.on_event("startup")
async def startup():
    # Create tables on startup
    await create_tables()

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
