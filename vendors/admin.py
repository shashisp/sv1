from django.contrib import admin
from vendors.models import Organisation


#prepopulated_fields = { 'slug': ['title'] }


class OrganisationAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ['name']}
    
admin.site.register(Organisation, OrganisationAdmin)


'''
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines=(UserProfileInline, )

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)
'''