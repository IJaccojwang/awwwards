from django import forms
from .models import Projects, Profile


class UploadForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ('design', 'usability', 'creativity', 'content', 'overall', 'posted' )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profilepic','bio', 'prefname', 'contact')