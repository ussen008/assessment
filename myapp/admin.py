from django.contrib import admin
from .models import *
# Register your models here.

# class ComprehensiveControlAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "observer":
#             kwargs["queryset"] = get_user_model().objects.filter(
#                 username=request.user.username
#             )
#         return super(ComprehensiveControlAdmin, self).formfield_for_foreignkey(
#             db_field, request, **kwargs
#         )

#     def get_readonly_fields(self, request, obj=None):
#         if obj is not None:
#             return self.readonly_fields + ("observer",)
#         return self.readonly_fields

    # def add_view(self, request, form_url="", extra_context=None):
    #     data = request.GET.copy()
    #     data["author"] = request.user
    #     request.GET = data
    #     return super(NotesAdmin, self).add_view(
    #         request, form_url="", extra_context=extra_context
    #     )

admin.site.register(ComprehensiveControl)
admin.site.register(Lesson)
admin.site.register(CategoryClass)
admin.site.register(OrganizeStudy)
admin.site.register(Resources)

admin.site.register(Teaching)
admin.site.register(PlanningLesson)