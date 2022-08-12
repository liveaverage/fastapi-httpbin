#
# All requests
#

from fastapi import APIRouter
from fastapi import FastAPI, Header, Request

router = APIRouter()


#
# Our core function to return the same data for each request.
#
def core(request: Request):

    retval = {}

    retval["args"] = request.query_params
    retval["headers"] = request.headers
    retval["source"] = {
        "ip": request.client[0],
        "port": request.client[1]
        }
    retval["url"] = request.url

    return(retval)


@router.get("/get", tags = ["HTTP Methods"], summary = "The request's GET parameters.")
async def get(request: Request):
    retval = core(request)
    return(retval)


@router.delete("/delete", tags = ["HTTP Methods"], summary = "The request's DELETE parameters.")
async def delete(request: Request):
    retval = core(request)
    return(retval)


@router.patch("/patch", tags = ["HTTP Methods"], summary = "The request's PATCH parameters.")
async def patch(request: Request):
    retval = core(request)
    return(retval)


@router.post("/post", tags = ["HTTP Methods"], summary = "The request's POST parameters.")
async def post(request: Request):
    retval = core(request)
    return(retval)


@router.put("/put", tags = ["HTTP Methods"], summary = "The request's PUT parameters.")
async def put(request: Request):
    retval = core(request)
    return(retval)



