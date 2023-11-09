from fastapi import FastAPI
from db.base_class import Base
from db.sessions import engine
from models.user import User
from models.deposit import Deposit
from models.withdraw import Withdraw
from routers import user
from routers import withdraw
from routers import deposit

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(deposit.router, prefix="/deposits", tags=["deposits"])
app.include_router(withdraw.router, prefix="/withdraw", tags=["withdraw"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
