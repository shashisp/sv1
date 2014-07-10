from .models import Organisation
from rest_framework import serializers



class OrganisationSerializer(serializers.HyperlinkedModelSerializer)
	class Meta:
		model = Organisation
		fields = ('name', 'service_type', 'address', 'city', 'contact', 'logo', 'description')