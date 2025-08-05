from django import forms

class ResumeForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    profession = forms.CharField(label='Profession', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone Number', max_length=20)
    github = forms.URLField(label='GitHub URL', required=False)
    linkedin = forms.URLField(label='LinkedIn URL', required=False)
    photo = forms.ImageField(label='Upload Photo', required=False)
    summary = forms.CharField(widget=forms.Textarea, label='Summary')
    education = forms.CharField(widget=forms.Textarea, label='Education')
    experience = forms.CharField(widget=forms.Textarea, label='Experience')
    skills = forms.CharField(widget=forms.Textarea, label='Skills')
    additional = forms.CharField(widget=forms.Textarea, label='Additional Info', required=False)
