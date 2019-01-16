from django import forms
from django.utils.translation import gettext_lazy as _

# import floppyforms.__future__ as forms
from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Invisible

from .models import Profile, Recommendation

class CaptchaForm(forms.Form):
    # captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
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
            'grad_month',
            'grad_year',
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
            'grad_month': _('Month PhD was obtained'),
            'grad_year': _('Year PhD was obtained'),
            'brain_structure': _('Field of Research - Brain Structure'),
            'modalities': _('Field of Research - Modalities'),
            'methods': _('Field of Research - Methods'),
            'domains': _('Field of Research - Domain'),
            'keywords': _('Field of Research - Keywords'),
        }
        help_texts = {
            'country': _('Country of current institution'),
            'webpage': _('Make sure people can look you up easily by providing a link to a personal website, profile or institution site.'),
            'position': _('Please choose your \'highest\' title from the proposed options to ease future searches.'),
            'grad_month': _('Leave empty if no PhD (yet).'),
            'grad_year': _('Please enter the full year (4 digits). Leave empty if no PhD (yet).'),
            'domains': _('There are free keywords at the end of the questionnaire to input further information.'),
            'keywords': _('Optionally you can add some more specific terms to describe your field of research, separated by commas.'),
        }

class RecommendModelForm(CaptchaForm, forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = [
            'reviewer_name',
            'reviewer_institution',
            'reviewer_position',
            'seen_at_conf',
            'comment',
        ]
        labels = {
            'reviewer_name': _('Full Name'),
            'reviewer_institution': _('Institution/Company'),
            'seen_at_conf': _('I saw one of her talks'),
        }
        help_texts = {
            'reviewer_position': _('Please choose the \'closest\' title from the proposed options.'),
            'comment': _('Describe here why you recommend this person for conference invitations or collaborations. If you attended one of her talks, add details on the event (year, event name). Please also mention potential conflicts of interest, like personal or professional relationships (friends, colleagues, former PI, ...)'),
        }
