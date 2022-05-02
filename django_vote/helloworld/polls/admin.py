from django.contrib import admin

from .models import Question, Choice
'''
直接注册
'''
# admin.site.register(Question)
# admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']  # 过滤器
    search_fields = ['question_text']  # 搜索框


admin.site.register(Question, QuestionAdmin)  # 注册后台表单
