from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render (request, "home.html", {})

def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [123, 456, 789, "Abc"]
    }
    return render (request, "contact.html", my_context)