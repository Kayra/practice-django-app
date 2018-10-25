from django.contrib import admin

from mysite.polls.models import Question, Choice


admin.site.register([Question, Choice])
