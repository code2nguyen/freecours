from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import View

import settings

class DetailView(TemplateView):
	""" Display the excercise detail """

class ExerciseListView(View):
	""" Display a list of Exercises with the information statistics """

	def get(self, request):
		template = loader.get_template('excercise_list.html')
		exercises = []

		#Walk the tree
		basepath = settings.TEMPLATES[0]['DIRS'][0] + '/exercises';
		for fname in os.listdir(basepath):
			path = os.path.join(basepath, fname)
			if os.path.isdir(path):
				exercises.append(fname)

		context = RequestContext(request, {'exercises':exercises})
		return HttpResponse(template.render(context))
