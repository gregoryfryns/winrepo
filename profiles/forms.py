from django import forms
from django.utils.translation import gettext_lazy as _

# import floppyforms.__future__ as forms
from captcha.fields import ReCaptchaField

from .models import Profile, Recommendation

class CaptchaForm(forms.Form):
    captcha = ReCaptchaField(label="", attrs={'theme' : 'clean',})


class CreateProfileModelForm(CaptchaForm, forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 
            'institution',
            'country',
            'email',
            'webpage',
            'position',
            'grad_date',
            'brain_structure',
            'modalities',
            'methods',
            'domains',
            'keywords',
        ]
        labels = {
            'name': _('Full Name'),
            'institution': _('Institution/Company'),
            'email': _('Email Address'),
            'webpage': _('Linked In or web page'),
            'grad_date': _('Year/month PhD was obtained'),
            'brain_structure': _('Field of Research - Brain Structure'),
            'modalities': _('Field of Research - Modalities'),
            'methods': _('Field of Research - Methods'),
            'domain': _('Field of Research - Domain'),
            'keywords': _('Field of Research - Keywords'),
        }
        help_texts = {
            'country': _('Country of current institution'),
            'webpage': _('Make sure people can look you up easily by providing a link to a personal website, profile or institution site.'),
            'position': _('Please choose your \'highest\' title from the proposed options to ease future searches'),
            'grad_date': _('Leave empty if no PhD (yet). Day unimportant if not remembered, just put the 1st.'),
            'modalities': _('Please preferentially choose from the proposed options to ease future searches. There are free keywords at the end of the questionnaire to input specialized information.'),
            'methods': _('Please preferentially choose from the proposed options to ease future searches. There are free keywords at the end of the questionnaire to input specialized information.'),
            'domain': _('Please preferentially choose from the proposed options to ease future searches. There are free keywords at the end of the questionnaire to input specialized information.'),
        }
        # widgets = {
        #     'name'
        # }


# class CreateProfileForm(CaptchaForm, forms.Form):
#     name = forms.CharField(
#         max_length=100, label='Full Name', help_text='Please provide your full name')
#     email = forms.EmailField(required=False)
#     webpage = forms
