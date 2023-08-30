from config.db import myclient
from service.batch import po_by_po_n
from schemas.recipe import Recipe
import json
from datetime import datetime, timezone, timedelta

def __query_range(start = datetime.now(timezone.utc) - timedelta(days=1), end = datetime.now(timezone.utc)):
    data = []
    for x in myclient.vacquensh.datalog.find({"d_date":{"$gte":start, "$lte": end}}, {"_id":0}):
        x["d_date"] = x["d_date"].isoformat()
        data.append(x)

    return data

def insert_log(data):
    data["d_date"] = datetime.now(timezone.utc)
    id = str(myclient.vacquensh.datalog.insert_one(data).inserted_id)
    return id

def get_last_24():
    return __query_range()

def get_po(po_n):
    po = po_by_po_n(po_n)
    po["start"] = datetime.strptime(po["start"], '%Y-%m-%d %H:%M:%S.%f')
    po["end"] = datetime.strptime(po["end"], '%Y-%m-%d %H:%M:%S.%f')
    return __query_range(start=po["start"], end= po["end"])

def get_range(start, end):
    return __query_range(start, end)