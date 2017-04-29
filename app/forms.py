from django import forms
from django.contrib.auth import get_user_model

from .models import Member
from .widgets import ModelSelect2, ModelSelect2Multiple

User = get_user_model()

class RelatedMixin(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance is not None:
            for name, field in self.fields.items():
                widget = field.widget if not hasattr(field.widget, 'widget') else field.widget.widget
                if isinstance(widget, ModelSelect2Multiple):
                    if hasattr(instance, '_prefetched_objects_cache'):
                        qs = instance._prefetched_objects_cache.get(name)
                        if qs is not None:
                            field.choices = [field.choices.choice(obj) for obj in qs]
                elif isinstance(widget, ModelSelect2):
                    cache_name = '_%s_cache' % name
                    if hasattr(instance, cache_name):
                        obj = getattr(instance, name)
                        field.choices = [field.choices.choice(obj)]

class MemberForm(RelatedMixin, forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user', 'classroom', 'books']
        widgets = {
            'user': ModelSelect2(url='user-autocomplete'),
            'books': ModelSelect2Multiple(url='book-autocomplete'),
        }
