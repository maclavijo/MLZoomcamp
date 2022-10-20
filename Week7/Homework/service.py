import numpy as np

import bentoml
from bentoml.io import JSON
from bentoml.io import NumpyNdarray

from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    country: str
    rating: float

model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")
#model_ref = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5")

model_runner = model_ref.to_runner()

svc = bentoml.Service("Wweek7_homework", runners=[model_runner])


@svc.api(input=NumpyNdarray(), output=JSON())
async def classify(UserProfile):
    
    prediction = await model_runner.predict.async_run(UserProfile)
    print(prediction)