from dal.widgets import WidgetMixin
from dal_select2.widgets import Select2WidgetMixin
from django import forms

class QuerySetSelectMixin(WidgetMixin):
    def filter_choices_to_render(self, selected_choices):
        if isinstance(self.choices, forms.models.ModelChoiceIterator):
            self.choices.queryset = self.choices.queryset.filter(
                pk__in=[c for c in selected_choices if c]
            )

class ModelSelect2(QuerySetSelectMixin,
                   Select2WidgetMixin,
                   forms.Select):
    """Select widget for QuerySet choices and Select2."""


class ModelSelect2Multiple(QuerySetSelectMixin,
                           Select2WidgetMixin,
                           forms.SelectMultiple):
    """SelectMultiple widget for QuerySet choices and Select2."""
