from django import forms
from django.contrib.auth import get_user_model
from dal import autocomplete

from .models import Member

User = get_user_model()

class RelatedMixin(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance is not None:
            for name, field in self.fields.items():
                if isinstance(field, forms.ModelMultipleChoiceField):
                    if hasattr(instance, '_prefetched_objects_cache'):
                        qs = instance._prefetched_objects_cache.get(name)
                        if qs is not None:
                            field.choices = [field.choices.choice(obj) for obj in qs]
                elif isinstance(field, forms.ModelChoiceField):
                    cache_name = '_%s_cache' % name
                    if hasattr(instance, cache_name):
                        obj = getattr(instance, name)
                        field.choices = [field.choices.choice(obj)]

class MemberForm(RelatedMixin, forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user', 'classroom', 'books']
        widgets = {
            'user': autocomplete.ModelSelect2(url='user-autocomplete'),
            'books': autocomplete.ModelSelect2Multiple(url='book-autocomplete'),
        }
