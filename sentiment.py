import os
import json
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account

#
# Before this app will work, you will need to provide a private key for a service account
#
# To get the private key:
# 1. browse to: https://console.cloud.google.com/apis/credentials
# 2. select Create Credentials -> Service Account Key
# 3. Select "New Service Account" on the service account dropdown
# 4. Give your service account a name, and set the role to "Project->Owner"
# 5. Select the "JSON" radio button
# 6. Press the create button, and download the key
# 7. copy-paste the content of the downloaded file between the """'s in the private-key variable definiton below
#
private_key = """{
  "type": "service_account",
  "project_id": "weg-buddy-231919",
  "private_key_id": "",
  "private_key":"
  "client_email": "weg-buddy-231919@appspot.gserviceaccount.com",
  "client_id": "",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": ""
}

"""

project_id = 'weg-buddy-231919'
info = json.loads(private_key, strict=False)
credentials = service_account.Credentials.from_service_account_info(info)

#import os
# THIS LINE IS NEEDED IF YOUR SYSTEM ENVIRONMENT VARIABLE DOES NOT WORK
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/Reid/PycharmProjects/weg-buddy/account.json"

def analyzeText(input) -> str:

    langClient = language.LanguageServiceClient(credentials=credentials)

    document = types.Document(
        content=input,
        type=enums.Document.Type.PLAIN_TEXT)

    sentiment = langClient.analyze_sentiment(document=document).document_sentiment
    return str(sentiment.score)
    #return client.analyze_sentiment(input)

def getIDs(sentiment_score, i) -> str:
    sentiment_score = float(sentiment_score)
    if sentiment_score < -0.8:
        if i == 0:
            return ("9082")
        elif i == 1:
            return ("21597")
    elif -0.8 <= sentiment_score < -0.6:
        if i == 0:
            return ("21539")
        elif i == 1:
            return ("21597")
    elif -0.6 <= sentiment_score <  -0.4:
        if i == 0:
            return ("18670")
        elif i == 1:
            return ("21539")
    elif -0.4 <= sentiment_score < -0.2:
        if i == 0:
            return ("10782")
        elif i == 1:
            return ("18670")
    elif -0.2 <= sentiment_score < 0:
        if i == 0:
            return ("12346")
        elif i == 1:
            return ("10782")
    elif 0 <= sentiment_score < 0.2:
        if i == 0:
            return ("8463")
        elif i == 1:
            return ("12346")
    elif 0.2 <= sentiment_score < 0.4:
        if i == 0:
            return ("8100")
        elif i == 1:
            return ("8463")
    elif 0.4 <= sentiment_score < 0.6:
        if i == 0:
            return ("14872")
        elif i == 1:
            return ("8100")
    elif 0.6 <= sentiment_score < 0.8:
        if i == 0:
            return ("19494")
        elif i == 1:
            return ("14872")
    else:
        if i == 0:
            return ("22379")
        else:
            return ("19494")

print("\nTest 1" + str(analyzeText("i am feeling not so good")))
print("\nTest 2" + str(analyzeText("I am so happy")))
print("\nTest 3" + str(analyzeText("I am angry")))
