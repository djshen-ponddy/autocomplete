from django.contrib import admin

from .models import Classroom, Member, Book
from .forms import MemberForm

class MemberInline(admin.TabularInline):
    model = Member
    form = MemberForm

    def get_queryset(self, request):
        return Member.objects.select_related('user').prefetch_related('books')

class ClassroomAdmin(admin.ModelAdmin):
    inlines = [MemberInline]

admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Book)
