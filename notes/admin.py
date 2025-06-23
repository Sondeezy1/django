from django.contrib import admin
from .models import Note

from django.contrib.auth.models import Group


admin.site.unregister(Group)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'categorie', 'termine')
    search_fields = ('title', 'content')
    list_filter = ('user', 'categorie', 'termine')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
                    
