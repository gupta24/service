from typing import Optional
from fastapi import FastAPI, Depends, Request
from .database import engine
from .core import models
from .v1.middleware_routers import cross_communication, new_router
from .main1 import app1
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Route


app = FastAPI()
models.Base.metadata.create_all(engine)


app.mount("/app1", app1)
app.include_router(new_router.router)


"""
routes = [
    Route(
        '/service/client_data_request',
        cross_communication.verify_client_for_data, methods=['GET', 'POST']),
    Route(
        '/client_data_request',
        new_router.verify_client_for_data, methods=['GET', 'POST']),
]

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080"
    ]

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"])]

app = Starlette(routes=routes, middleware=middleware)
"""
