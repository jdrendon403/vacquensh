from fastapi import APIRouter, Body, Request, HTTPException, Depends, status, Path
from fastapi.responses import JSONResponse
from typing import List
from schemas.batch import Batch
from service.batch import po_by_po_n, po_list, delete_po, insert_po, update_po

batchs = APIRouter()

@batchs.get("/batchs/",
            tags=["Batchs"],
            response_model=List[str]
            )
def pos_list():
    pos = po_list()
    return JSONResponse(content=pos, status_code=status.HTTP_200_OK)

@batchs.get("/po/{po_n}",
            tags=["Batchs"],
            response_model=Batch
            )
def po(po_n: int = Path(min=0) ):
    po = po_by_po_n(po_n)
    if po != None:
        return JSONResponse(content=po, status_code=status.HTTP_200_OK)
    return JSONResponse(content=po, status_code=status.HTTP_204_NO_CONTENT)

@batchs.post("/po/",
            tags=["Batchs"],
            response_model=Batch,
            )
def start_po(po: Batch = Body(...)):
    id = insert_po(po)
    return JSONResponse(content=id, status_code=status.HTTP_201_CREATED)

@batchs.put("/po/{po_n}",
            tags=["Batchs"],
            response_model=Batch,
            )
def end_po(po_n: int = Path(min = 0)):
    po = update_po(po_n)
    return JSONResponse(content=po, status_code=status.HTTP_202_ACCEPTED)

@batchs.delete("/po/{po_n}",
            tags=["Batchs"],
            response_model=Batch,
            )
def del_po(po_n: int = Path(min=0)):
    po = delete_po(po_n)
    return JSONResponse(content=po, status_code=status.HTTP_202_ACCEPTED)