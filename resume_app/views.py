from django.shortcuts import render, redirect
from .forms import ResumeForm
from .utils import generate_pdf

def resume_form_view(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            request.session['form_data'] = form.cleaned_data
            return redirect('resume_preview')
    else:
        form = ResumeForm(initial=request.session.get('form_data', {}))
    return render(request, 'resume_app/form.html', {'form': form})

def resume_preview(request):
    form_data = request.session.get('form_data', {})
    if not form_data:
        return redirect('resume_form_view')
    return render(request, 'resume_app/resume.html', {'form_data': form_data})

def download_pdf(request):
    form_data = request.session.get('form_data', {})
    if not form_data:
        return redirect('resume_form_view')
    return generate_pdf({'form_data': form_data})
