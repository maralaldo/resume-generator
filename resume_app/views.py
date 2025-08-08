import base64
import tempfile
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .forms import ResumeForm
from weasyprint import HTML


def resume_form_view(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        action = request.POST.get('action')

        if form.is_valid():
            data = form.cleaned_data
            request.session['form_data'] = data  # сохраняем данные формы

            # Обработка фото
            photo = request.FILES.get('photo')
            if photo:
                image_data = photo.read()
                encoded_image = base64.b64encode(image_data).decode('utf-8')
                request.session['photo_base64'] = encoded_image

            context = {
                'data': data,
                'photo_base64': request.session.get('photo_base64')
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

            elif action == 'back':
                # Возврат к форме с сохраненными данными
                form_data = request.session.get('form_data')
                form = ResumeForm(initial=form_data) if form_data else ResumeForm()
                return render(request, 'resume_app/form.html', {
                    'form': form,
                    'photo_base64': request.session.get('photo_base64')
                })

        else:
            # Если форма не валидна — просто вернуть её обратно с ошибками
            return render(request, 'resume_app/form.html', {
                'form': form,
                'photo_base64': request.session.get('photo_base64')
            })

    else:
        # GET-запрос: заполнить форму ранее введенными данными
        form_data = request.session.get('form_data')
        form = ResumeForm(initial=form_data) if form_data else ResumeForm()

    return render(request, 'resume_app/form.html', {
        'form': form,
        'photo_base64': request.session.get('photo_base64')
    })
