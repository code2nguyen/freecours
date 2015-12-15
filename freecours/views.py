import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import View

class Index(View):
	def get(self, request):
		template = loader.get_template('index.html')
		context = RequestContext(request, {})
	return HttpResponse(render(context))
