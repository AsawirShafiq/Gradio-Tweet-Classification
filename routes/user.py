from fastapi import APIRouter ,File, UploadFile
from models.user import User
from models.user import Tweet
from models.user import PredictionResponse
from config.db import conn
from Schemas.user import usersEntity
from Schemas.user import predictionsEntity
from transformers import pipeline
import pandas as pd
import io
from typing import List, Union
#from typing import List, Dict
#Class that allows us to define routes and associated logic in modular way.
user = APIRouter()

# I just googled for tweet bullying classification from huggingace and got this. It works quote well and faster than the one I made.
model_name = "AnithaThilak/Cyberbullying-detection-tweet-comment"
pipe = pipeline("text-classification", model=model_name)

@user.get('/')
#We use async here to make these operations to be non-blocking..which means it can wait for i/o while not keeping other process.
#CAn lead to efficient handling of multiple resources.
async def find_all_users():
  return usersEntity(conn.local.user.find())

#Does the same thing as the user one. Prints out all the predictions we have done yet.
@user.get('/prediction')
async def find_all_predictions():
  return predictionsEntity(conn.local.predictions.find())

@user.post('/')
async def create_user(user: User):
  conn.local.user.insert_one(dict(user))
  return usersEntity(conn.local.user.find())

#file_path = 'cyberbullying_tweets.csv'
#data = pd.read_csv(file_path)
#data['predicted_label'] = None

# Define the endpoint to get predictions
#@user.get("/predictfromcsv/", response_model=PredictionResponse)
#async def predictfromcsv():
    #Sending all the tweets from the csv to the pipleine to get their asnwers into the database as well
#    for twe in data['tweet_text']:
#      predictions = pipe([twe])
#      predicted_label = predictions[0]['label']

#      prediction_data = {
#        "tweet_text": twe,
#        "predicted_label": predicted_label
#      }
#      conn.local.predictions.insert_one(prediction_data)

 #   return PredictionResponse(tweet_text=twe, predicted_label=predicted_label)
@user.post("/predictfromcsv/", response_model=Union[List[PredictionResponse], dict])
async def predictfromcsv(file: UploadFile = File(...)):
    contents = await file.read()
    print(contents)
    path = contents.decode('utf-8')
    data = pd.read_csv(path)
    data = data.rename(columns={data.columns[0]: 'tweet_text'})
    # Ensure the 'tweet_text' column exists in the uploaded CSV
    if 'tweet_text' not in data.columns:
        # Return an error message in the format that matches the Union type
        return {"error": "CSV file must contain a 'tweet_text' column"}

    predictions_list = []

    # Process each tweet and predict the label
    for twe in data['tweet_text']:
        predictions = pipe([twe])
        predicted_label = predictions[0]['label']

        prediction_data = {
            "tweet_text": twe,
            "predicted_label": predicted_label
        }

        # Store the prediction in the database
        conn.local.predictions.insert_one(prediction_data)

        # Append to the response list
        predictions_list.append({
            "tweet_text": twe,
            "predicted_label": predicted_label
        })

    return predictions_list


@user.post("/predict/", response_model=PredictionResponse)
async def predict(tweet: Tweet):
    # Predict using the pipeline
    predictions = pipe([tweet.tweet_text])
    predicted_label = predictions[0]['label']

    prediction_data = {
        "tweet_text": tweet.tweet_text,
        "predicted_label": predicted_label
    }

    conn.local.predictions.insert_one(prediction_data)
    return PredictionResponse(tweet_text=tweet.tweet_text, predicted_label=predicted_label)


