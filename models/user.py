#Establish model for user. Have used simplistic string data.
from pydantic import BaseModel

class User(BaseModel):
  name: str
  email: str

# Inclduing a model for how the input would be coming in.
class Tweet(BaseModel):
  tweet_text: str

# Including a model for who the reponse would be shaped.
class PredictionResponse(BaseModel):
  tweet_text: str
  predicted_label: str
