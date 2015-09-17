from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context
from django.http import Http404
from class_activity.models import *
import MySQLdb

# Create your views here.
def index(request):
	return render_to_response('index.html')
