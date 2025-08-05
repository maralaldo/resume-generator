from django import forms

class ResumeForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone Number', max_length=20)
    education = forms.CharField(label='Education', widget=forms.Textarea)
    experience = forms.CharField(label='Experience', widget=forms.Textarea)
    skills = forms.CharField(label='Skills', widget=forms.Textarea)
    additional = forms.CharField(label='Additional Info', widget=forms.Textarea, required=False)
