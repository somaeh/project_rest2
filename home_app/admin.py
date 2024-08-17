from django.contrib import admin

from.models import Person, Question, Answer


admin.site.register(Person)
# admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)