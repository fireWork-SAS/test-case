from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from urllib.request import Request, urlopen

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from todo_proxy.settings import EXTERNAL_API_BASE

import urllib 
import requests
import json

def get_proxy_data(user_name):
	if user_name is not None:
		data = {'name':user_name}
		req_complete = EXTERNAL_API_BASE + 'todos'
		rr = requests.get(req_complete)
		
		if (rr.ok):
			json_data = rr.json()
			res_array = rr.json()
			data={'name':user_name, 'todos':res_array}
		else:
			data={'name':user_name, 'todos':'nope'}
	else:
		data = {'name':'nobody'}
	return data
	


def index(request):
	todo_data = {'name':'empty'}
	if request.user.is_authenticated:
	# Do something for authenticated users.
		todo_data = get_proxy_data(request.user.username)


	else:
	# Do something for anonymous users.
		pass

	context = {'data':todo_data}
	return render(request, 'base.html', context)


def todo_get(request):

    return HttpResponse("hidden request.")


def login_request(request):
    context={}
    return render(request, 'login.html', context)
    return redirect("todo_wrapper:homepage")


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("todo_wrapper:homepage")