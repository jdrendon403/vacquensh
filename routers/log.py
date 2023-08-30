from fastapi import APIRouter, Body, Request, HTTPException, Depends, status, Path
from fastapi.responses import JSONResponse
from typing import List
from service.log import insert_log, get_last_24, get_po, get_range
import json
from datetime import datetime, timedelta

log = APIRouter()

@log.get("/last24/", tags=["Logs"])
def last_24():
    data = get_last_24()
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)

@log.get("/logpo/{po_n}", tags=["Logs"])
def po_log(po_n: int = Path(min=0)):
    data = get_po(po_n)
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)

@log.get("/logrange/{start}/{end}", tags=["Logs"])
def data_range(start: datetime = Path(), end: datetime = Path()):
    data = get_range(start, end)
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)

@log.post("/logdata/", tags=["Logs"])
def log_data(data = Body(...)):
    id = insert_log(data)
    return JSONResponse(content=id, status_code=status.HTTP_200_OK)