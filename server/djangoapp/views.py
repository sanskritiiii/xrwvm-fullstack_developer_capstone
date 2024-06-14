from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    # handle post request
    if request.method == "POST":
        # get use name and password from post request
        username = request.POST['username']
        password = request.POST['psw']

        # authenticate user
        user = authenticate(username=username, password=password)
        # if authorized log in and redirect else do not login
        if user is not None:
            login(request, user)
            return redirect("djangoapp:index")
        else:
            return redirect("djangoapp/index.html")
    else:
        return redirect("djangoapp/index.html")

# Create a `logout_request` view to handle sign out request
#def logout_request(request):
# ...

# Create a `registration` view to handle sign up request
#@csrf_exempt
 #def registration(request):
# ...

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
 #def get_dealerships(request):
# ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
 #def get_dealer_reviews(request,dealer_id):
# ...

# Create a `get_dealer_details` view to render the dealer details
 #def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
 #def add_review(request):
# ...
