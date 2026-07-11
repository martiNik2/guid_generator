from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import generator

app = FastAPI()

origins=[
    "http://0.0.0.0"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/")
def print_crap():
    guid=generator.generate_guid()
    return {"guid":guid}