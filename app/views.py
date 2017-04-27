from dal import autocomplete
from django.contrib.auth import get_user_model

from .models import Book

class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        User = get_user_model()
        qs = User.objects.filter(is_superuser=False)
        if self.q:
            qs = qs.filter(username__icontains=self.q)
        return qs

class BookAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Book.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs
