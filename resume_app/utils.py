from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

def generate_pdf(context):
    html_string = render_to_string('resume_app/resume.html', context)
    
    pdf_file = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response
