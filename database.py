import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Cloud FireStore functions
def new_instance():
    cred = credentials.ApplicationDefault()
    # cred = credentials.Certificate("../weg-buddy-231919-firebase-adminsdk-de72u-77d425a00f")
    firebase_admin.initialize_app(cred, {
        u'project_id': u'weg-buddy-231919',
    })
    db = firestore.client()
    return db


def add_recipe(id_num, recipe, details):
    db = firestore.client()
    rec_ref = db.collection(u'recipes').document(id_num)
    rec_ref.set({
        u'recipe': recipe,
        u'details': details
    })


def add_groceries(id_num, item, price, location):
    db = firestore.client()
    groc_ref = db.collection(u'groceries').document(id_num)
    groc_ref.set({
        u'item': item,
        u'price': price,
        u'location': location
    })


