from django import forms

class ResumeForm(forms.Form):
    full_name = forms.CharField(required=False)
    profession = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False)
    github = forms.URLField(required=False)
    linkedin = forms.URLField(required=False)
    summary = forms.CharField(widget=forms.Textarea, required=False)
    education = forms.CharField(widget=forms.Textarea, required=False)
    experience = forms.CharField(widget=forms.Textarea, required=False)
    skills = forms.CharField(widget=forms.Textarea, required=False)
    additional = forms.CharField(widget=forms.Textarea, required=False)
