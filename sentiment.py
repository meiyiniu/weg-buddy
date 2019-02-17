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
  "private_key_id": "e14f1c77c32ac170ea351b3a33616b3568d6f99e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQDmwcb3PomMbuGk\nIr4+gcNJSGNcCn0XbvlWCmpvkFqwxCyegoC+pTq3Z/9zxbFJapgoS/neB/S1Rerf\nXpP+AWbpXNMxpgADvBryzB5bmDaLU8kwgpJo/putROswLGV8ddGfi2hHOIWaqTfw\nfuxFyh8C/hzMQXkYoIRr5qyELzv7hF5iXL+u5RpGmuiNfJz0nVDa9RvwQbo3C1nw\nrg8lCqa3v5rZRLc0lx3LIuGO5o/Xo6DS7R6VOWJYFR4tAoasXCdVbU8VyMoiZkYu\nm4nCP6PjEJVgcfUOJdWZnwZ5tAc9aNUjzUvjz++oS2u7J80oZEMIVyNSdJm2ygmN\nopPEjK15AgMBAAECgf9geEWUEBc8RXQXNb94sBnwjOCOmNPxxxKHkdqzqL2gvMcc\nw5fklE+jtSqw1iEH5ujvY0JXr8waM8eVLoBJY/nViSJsdcOnZ6rmg4rJF+xCMox5\n+McXDFU9nBEgPohcJtZLC1EJPh5CcmqDTFpe//8IlVRPGhooCqLtUPmo2uQtaGus\nypm5dkQ2a6egV5TJmYCGXQXtYmOq7+qJ2heh2FjnAhAbLtmp/24xxO86t3d07lqP\ntb+10wAyQisU1gIETC7ReOdWIIbDs2F3jaXbHRWnEP24SozdR8K4cysPppY9nzT2\n7B1pvJ9IHwqLqlnFe5kKpDXqYNudI80h8mJyZYECgYEA/eEhggDBRLNQ0kaocXtC\ngLdSIKFRdge3Jq6ZUzMS16tKWo4K+zdKZmPlZ99ZYQrztLIPaNnNZZ1yg0PRZrwx\nWP684aemUh1IDyffZw1+gfoSFlJ1fvGjpFg/3bIP98aJhRSAR9Ghj7x33WA5fqNy\ne9hfk5V09fpTr5GOyQj8J8ECgYEA6K80IhNwPy24+Xj8UENZWLky9bxArwrqHpX9\nypTLpDjPMolSNDBFF3eBmKTcIUOXt5fm7DMgjq8oSxepPKpux/bfnnFJIIneZfLg\noayo7tSwLcsNBC3SY1gbnh/cnw4QZDhP3N5God4EkdBV0fuX1zdeMz3AzlRntc+b\nhNiIs7kCgYA9Pc54brgwW1UWtEazwTkElbQw/NkKsMfEg/+maz6TWdWAzJznhqni\n0xwml2EXIK4zG3TOJSP/7CAQfA6KSsFYp3JmuKtNSZT1WvfwAvhOYEV2rwN60M1Z\nupQFZYumiHTp7k0XhgEEDEGZ3DliTAk0yLgdgMMLBwyi4GjiI9G3wQKBgC/gpRyB\n3W3SjaYfg+NMCF1eNiMkKjcaStQiTsdZWJGg8tlWMij06bKLb4omGflqPBSV1/kw\nB/n0Bpl08+i8tPDGVnr2mnJsi+t0T05VBamm791sU3BRsWGppn0h1zaPIUZN4/jx\nb50s3snWEWKUn0i0ZtiqUzrhWTmqzzhFidNZAoGAW6r8dCFJJxVDxba/pTPR5PQ1\nUPVXegR7zq84oBUDc/hC/EuENZFneDqApQHSywyCB812Z5JR985sdklzQb1ITBHI\nf056YvK9/A0qOHD86/lJbDhAKGAA/fPrJ5YUV1e5HhA3XpQpmAt6Ir27ul4qudNC\nxfp2koUbpF2AYP+A3p0=\n-----END PRIVATE KEY-----\n",
  "client_email": "weg-buddy-231919@appspot.gserviceaccount.com",
  "client_id": "106483880630042982742",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/weg-buddy-231919%40appspot.gserviceaccount.com"
}

"""

#print(private_key)

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
            return ("215390")
        elif i == 1:
            return ("21597")
    elif -0.6 <= sentiment_score <  -0.4:
        if i == 0:
            return ("18670")
        elif i == 1:
            return ("215390")
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
        elif i == 1:
            return ("19494")





print("\nTest 1" + str(analyzeText("I am so sad")))
print("\nTest 2" + str(analyzeText("I am so happy")))
print("\nTest 3" + str(analyzeText("I am angry")))