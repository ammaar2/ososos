from fastapi import FastAPI, HTTPException

# حقوق الملكية @jokerpython3
app = FastAPI()

def date_sc(Id: int):
    try:
        if Id > 1 and Id < 1279000:
            return 2010
        elif Id > 1279001 and Id < 17750000:
            return 2011
        elif Id > 17750001 and Id < 279760000:
            return 2012
        elif Id > 279760001 and Id < 900990000:
            return 2013
        elif Id > 900990001 and Id < 1629010000:
            return 2014
        elif Id > 1900000000 and Id < 2500000000:
            return 2015
        elif Id > 2500000000 and Id < 3713668786:
            return 2016
        elif Id > 3713668786 and Id < 5699785217:
            return 2017
        elif Id > 5699785217 and Id < 8507940634:
            return 2018
        elif Id > 8507940634 and Id < 21254029834:
            return 2019
        else:
            return "2020-2023"
    except Exception as e:
        return str(e)

@app.get("/date_sc/")
async def get_date_sc(id: int):
    try:
        result = date_sc(id)
        return {"result": result, "copyright": "@jokerpython3"}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid 'id' parameter.")
