from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def print_crap():
    return {"hello":"world"}