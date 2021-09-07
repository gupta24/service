from sqlalchemy.orm.session import Session
from fastapi import (
    Depends, status, HTTPException, APIRouter, Body, Request, Response)
from typing import Optional, Callable, List
from ...database import get_db
from ...core.schema_models import (ClientSignatureWithData)
from ...core import models
from fastapi.routing import APIRoute

import logging


logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


router = APIRouter()
db: Session = Depends(get_db)


@router.post(
    '/client_data_request',
    status_code=status.HTTP_200_OK,
    tags=['client'])
async def verify_client_for_data(request: ClientSignatureWithData):
    # get the raw data and HMAC signature from client side..
    logger.info("start")
    return {"message": "done"}


@router.get(
    '/client_data',
    status_code=status.HTTP_200_OK,
    tags=['client'])
async def verify_client_for_data():
    # get the raw data and HMAC signature from client side..
    return 2
