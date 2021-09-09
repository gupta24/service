from typing import Optional
from fastapi import FastAPI, Depends, Request
from .database import engine
from .core import models
from .v1.middleware_routers import new_router
from .sub_main import app1


app = FastAPI()
models.Base.metadata.create_all(engine)


app.mount("/app1", app1)
app.include_router(new_router.router)
