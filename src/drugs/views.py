import pymongo
from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView

def products(request):
    client = pymongo.MongoClient(
        "mongodb+srv://admin:medical7@cluster0.g6nvd.mongodb.net/project?retryWrites=true&w=majority")
    db = client["project"]
    col = db["drugs_drugs"]
    context = {
        'items': col.find({}, {'_id': 0, 'item': 1, 'qty': 1})
    }
    return render(request,"products.html",context)

def checkout(request):
    return render(request,"checkout.html")



def drug_view(request):
    client = pymongo.MongoClient(
        "mongodb+srv://admin:medical7@cluster0.g6nvd.mongodb.net/project?retryWrites=true&w=majority")
    db = client["project"]
    col = db["drugs_drugs"]
    context={
        'items':col.find()
    }
    return render(request,"home.html",context)
