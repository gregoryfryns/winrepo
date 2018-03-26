from django.forms import Form, ModelForm

from captcha.fields import ReCaptchaField

from .models import Profile, Recommendation

class CaptchaForm(Form):
    captcha = ReCaptchaField(attrs={'theme' : 'clean',})

    
class SendEmailForm(Form):
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
    
    
class CreateProfileForm(CaptchaForm, SendEmailForm, ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 
            'email', 
            'webpage', 
            'institution',
            'country',
            'position',
            'grad_date',
            'brain_structure',
            'modalities',
            'methods',
            'domain',
            'keywords',
        ]
