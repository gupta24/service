from fastapi import FastAPI, Response, HTTPException, status
from ..signatures.signature_validation import check_signature
from starlette.types import ASGIApp, Message, Scope, Receive, Send
from starlette.responses import PlainTextResponse
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse
from typing import Callable, Awaitable
import logging
from starlette.middleware.base import BaseHTTPMiddleware



logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class RequestBody(Request):
    def __init__(self, scope: Scope, body: bytes) -> None:
        super().__init__(scope, self._receive)
        self._body = body
        self.request_completed = False

    async def _receive(self) -> Message:
        if self.request_completed:
            return {"type": "http.disconnect"}
        else:
            self.request_completed = True
            return {"type": "http.request", "body": self._body, "more_body": False}


class CustomMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[StreamingResponse]]):
        logger.info('first')
        body = await request.body()
        # logger.info(body)
        client_signature = request.headers['signature']
        valid_signature = check_signature(client_signature, body)
        # logger.info(client_signature)
        if valid_signature:
            request = RequestBody(request.scope, body)
            response = await call_next(request)
            # response = PlainTextResponse("valid Request", status_code=200)
            return response
        else:
            response: Response
            response = PlainTextResponse("Invalid Request", status_code=400)
            return response

 
        


