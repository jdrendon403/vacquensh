from config.db import myclient
from schemas.batch import Batch
import json
from datetime import datetime, timezone


def po_list():
    pos = list(myclient.vacquensh.batch.find({"end":{"$ne":None}}, {"_id":0, "po":1}))
    pol = []
    for po in pos:
        pol.append(po["po"])
    
    return pol

def insert_po(po: Batch):
    po = dict(po)
    po["start"] = datetime.now(timezone.utc)
    id = str(myclient.vacquensh.batch.insert_one(po).inserted_id)
    return id

def po_by_po_n(po_n):
    po = myclient.vacquensh.batch.find_one({"po": po_n}, {"_id":0})
    if po != None:
        po["start"] = str(po["start"])
        po["end"] = str(po["end"])
    return po

def update_po(po_n):
    po = dict(myclient.vacquensh.batch.find_one_and_update(
        {"po": po_n},
        {
            "$set":{
                "end":datetime.now(timezone.utc)
            }
        }
    ))

    if po != None:
        po["start"] = str(po["start"])
        po["end"] = str(po["end"])
        del po["_id"]
    print(po)
    return po


def delete_po(po_n):
    po = myclient.vacquensh.batch.find_one_and_delete({"po": po_n})
    if po != None:
        po["start"] = str(po["start"])
        po["end"] = str(po["end"])
        del po["_id"]
    return po


