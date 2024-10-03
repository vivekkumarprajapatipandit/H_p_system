from django.contrib import admin
from .models import Details

class detailsadmin(admin.ModelAdmin):
    list_display=('id','Name','Username','Email','Password','DOB','Gender','Language','Aadhar','Profilepic') # type: ignore
admin.site.register(Details,detailsadmin)