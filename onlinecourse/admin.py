from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

class LessonInline(admin.StackedInline): 
    model = Lesson
    extra = 5

class ChoiceInline(admin.StackedInline): # added ChoiceInline class
    model = Choice
    extra = 2

class QuestionInline(admin.StackedInline): # added QuestionInline class
    model = Question
    extra = 2

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class QuestionAdmin(admin.ModelAdmin): # added QuestionAdmin class
    inlines = [ChoiceInline]
    list_display = ['content']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin) # just added
admin.site.register(Choice) # just added
admin.site.register(Submission) # just added
