import uvicorn
from typing import Optional
from fastapi import FastAPI, Depends, Request
from .src.database import engine
from .src.core import models
from .src.v1.middleware_routers import new_router
from .src.sub_main import app1


app = FastAPI()
models.Base.metadata.create_all(engine)


app.mount("/app1", app1)
app.include_router(new_router.router)



def start():
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)
