from django.contrib import admin
from .models import ResumeModel

# Register your models here.
@admin.register(ResumeModel)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id','FirstName','LastName','Email','ContactNo','Gender','DOB','City','State','Language','Programming_Language','Education','Prefered_loc','Prof_image','Project']