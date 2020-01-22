from django.contrib import admin
from .models import Session, Response, Profile, Question

# Register models here.
admin.site.register(Session)
admin.site.register(Response)
admin.site.register(Profile)
admin.site.register(Question)


