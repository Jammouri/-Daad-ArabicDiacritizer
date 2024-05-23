from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from keras.models import load_model
from pre_processing import predict

app = FastAPI()

class r_text(BaseModel):
    text:str

model=load_model('shape400ResidualsNormalized.h5')
@app.post("/")
async def read_root(myText: r_text):
    data=predict(myText.text,model)
    return {"diacatarize": data}

