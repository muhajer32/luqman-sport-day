from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from .models import Participant, Activity

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['first_name', 'last_name', 'age_group', 'gender', 'activities']
        widgets = {
            'activities': forms.CheckboxSelectMultiple,
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age_group': 'Age Group',
            'gender': 'Gender',
            'activities': 'Activities',
        }
ParticipantFormSet = modelformset_factory(
    Participant,
    form=ParticipantForm,
    extra=1,
    can_delete=True,
    max_num=10,
    min_num=1,
    validate_min=True,
    widgets={
        'activities': forms.CheckboxSelectMultiple,
    }
)