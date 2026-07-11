from fastapi import FastAPI
import generator

app = FastAPI()


@app.get("/")
def print_crap():
    guid=generator.generate_guid()
    return {"guid":guid}