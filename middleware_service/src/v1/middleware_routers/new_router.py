from sqlalchemy.orm.session import Session
from fastapi import FastAPI, Depends, status, HTTPException, APIRouter
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi.encoders import jsonable_encoder
import requests
from ...database import get_db
from ...core import models



router = APIRouter()
db: Session = Depends(get_db)



@router.get(
    '/client_data_request',
    status_code=status.HTTP_200_OK,
    tags=['client'])
def verify_client_for_data():
    return "no"



    

