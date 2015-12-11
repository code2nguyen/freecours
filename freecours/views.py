import os

from django.http import HttpResponse
from django.template import RequestContext, loader

import settings

def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def luyentap(request):
	template = loader.get_template('luyentap.html')
	exercises = []

	#Walk the tree
	basepath = settings.TEMPLATES[0]['DIRS'][0] + '/exercises';
	for fname in os.listdir(basepath):
		path = os.path.join(basepath, fname)
		if os.path.isdir(path):
			exercises.append(fname)

	context = RequestContext(request, {'exercises':exercises})
	return HttpResponse(template.render(context))
