from django.contrib import admin

# Register your models here.
from .models import * #About,Service,portfolio,Education,Experience,Skills

# Register your models here.
admin.site.register(About)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(portfolio)
admin.site.register(Service)