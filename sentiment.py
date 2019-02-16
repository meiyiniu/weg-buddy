from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/Reid/PycharmProjects/weg-buddy/account.json"

def analyzeText(input) -> int:
    credentials = service_account.Credentials.from_service_account_file(
        'account.json')
    langClient = language.LanguageServiceClient()

    document = types.Document(
        content=input,
        type=enums.Document.Type.PLAIN_TEXT)

    return langClient.analyze_sentiment(document=document).document_sentiment
    #return client.analyze_sentiment(input)

print(analyzeText("I love it!"))