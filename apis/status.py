#
# Redirect endpoints.
#

import random

from fastapi import APIRouter, FastAPI, Header, Response, Query, Path, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse


router = APIRouter()



@router.get("/status/{codes}", tags = ["Status Codes"], 
    summary = "Return status code or random one if multiple given as comma-delimited list")
async def get(response: Response, 
    codes: str = Path(min_length = 3, regex = "^[0-9,]+$")
    ):

    codes = codes.split(",")

    #
    # Do some sanity checking.
    # I originally wanted a custom exception, but it got *really* challenging figuring
    # out how to add an exception while in a router, and adding it to app didn't help either. :-(
    #
    for code in codes:
        if len(code) != 3:
            retval = {"type": "code_length", "message": f"Code '{code}' is != 3 digits!"}
            raise HTTPException(status_code = 422, detail = retval)

    code = int(random.choice(codes))

    if str(code)[0] == "3":
        return RedirectResponse("/redirect/1", status_code = code)

    response.status_code = code

    return(None)


