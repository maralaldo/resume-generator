import base64
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
import tempfile

from .forms import ResumeForm


def resume_form_view(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        action = request.POST.get('action')

        if form.is_valid():
            data = form.cleaned_data
            context = {'data': data}

            # Получаем фото из формы или из сессии
            photo = request.FILES.get('photo')
            if photo:
                # Чтение и кодирование фото
                photo_data = photo.read()
                request.session['photo_content'] = base64.b64encode(photo_data).decode('utf-8')
                request.session['photo_name'] = photo.name
                context['photo_base64'] = request.session['photo_content']
            elif request.session.get('photo_content'):
                context['photo_base64'] = request.session['photo_content']

            # Сохраняем данные формы в сессии (для возврата назад)
            request.session['form_data'] = request.POST

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

            elif action == 'back':
                return render(request, 'resume_app/form.html', {'form': form})

    else:
        # Если возвращаемся назад, берём данные формы и фото из сессии
        form_data = request.session.get('form_data')
        if form_data:
            form = ResumeForm(form_data)
        else:
            form = ResumeForm()

    return render(request, 'resume_app/form.html', {'form': form})
