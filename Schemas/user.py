
#Transform data response from DB to suitable API response.
def userEntity(item) -> dict:
  return{
    "id":str(item["_id"]),
    "name":item["name"],
    "email":item["email"]

  }

def usersEntity(entity) -> list:
  return [userEntity(item) for item in entity]

#The fucntions for prediction are same as the users one. Basically just take out from db and print out all the previosu predictions we have sent.

def predictEntity(item) -> dict:
  return{
    "id":str(item["_id"]),
    "tweet_text":item["tweet_text"],
    "predicted_label":item["predicted_label"]

  }

def predictionsEntity(entity) -> list:
  return [predictEntity(item) for item in entity]
