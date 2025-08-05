from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
import tempfile

from .forms import ResumeForm

def resume_form_view(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES) 
        if form.is_valid():
            action = request.POST.get('action')
            data = form.cleaned_data
            photo = request.FILES.get('photo')  
            context = {
                'data': data,
                'photo': photo  
            }

            if action == 'preview':
                return render(request, 'resume_app/resume.html', context)

            elif action == 'pdf':
                template = get_template('resume_app/resume.html')
                html = template.render(context)
                with tempfile.NamedTemporaryFile(delete=True) as output:
                    HTML(string=html).write_pdf(output.name)
                    output.seek(0)
                    response = HttpResponse(output.read(), content_type='application/pdf')
                    response['Content-Disposition'] = 'filename="resume.pdf"'
                    return response
    else:
        form = ResumeForm()

    return render(request, 'resume_app/form.html', {'form': form})

