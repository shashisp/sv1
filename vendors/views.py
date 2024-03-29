from django.shortcuts import render_to_response
from vendors.models import Organisation
from django.http import HttpResponse
from forms import OrganisationForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.generic import ListView
from django.views.generic.edit import FormView
from rest_framework import viewsets
from vendors.serializers import OrganisationSerializer



class AddOrganisationView(FormView):
	form_class = OrganisationForm
	success_url = "/"
	template_name = 'addorg.html'

	def form_valid(self, form):
		form.save(commit = True)
		return super(AddOrganisationView, self).form_valid(form)






class OraganisationViewSet(viewsets.ModelViewSet):
	queryset = Organisation.objects.all()
	serializer_class = OrganisationSerializer
	paginate_by = 10
	paginate_by_param = "page_size"


class TestList(ListView):
	model = Organisation

"""
def join(request):
	if request.POST:
		form = OrganisationForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/admin')
	else:
		form = OrganisationForm()

	args = {}
	args.update(csrf(request))

	args['form'] = form

	return render_to_response('addorg.html', args)
"""



