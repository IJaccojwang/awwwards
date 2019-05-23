from django import forms
from .models import Project, Profile


class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('design', 'usability', 'creativity', 'content', 'overall', 'posted', 'user' )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profilepic','bio', 'prefname', 'contact')