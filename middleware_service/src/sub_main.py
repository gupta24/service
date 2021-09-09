from typing import Optional, Callable, List
from fastapi import FastAPI, Response, Request, HTTPException, status
from .database import engine
from .core import models
from .v1.middleware_routers import cross_communication
from .v1.middleware.middleware import CustomMiddleware
import logging


logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


app1 = FastAPI()
models.Base.metadata.create_all(engine)

app1.include_router(cross_communication.router, prefix="/service")

app1.add_middleware(CustomMiddleware)







"""
@app1.middleware("http")
async def middleware_process(request: Request, call_next):   
    task = asyncio.create_task(foo(await request.body()))
    await task
    start_time = time.time()
    set_header(request.headers['signature'])
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
"""

