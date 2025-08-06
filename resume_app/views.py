import os
import glob
from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import ResumeForm


def resume_form_view(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        action = request.POST.get('action')

        if form.is_valid():
            data = form.cleaned_data

            # Обработка фото
            photo = request.FILES.get('photo')
            photo_url = None
            if photo:
                temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
                os.makedirs(temp_dir, exist_ok=True)
                for f in glob.glob(os.path.join(temp_dir, '*')):
                    os.remove(f)

                fs = FileSystemStorage(location=temp_dir)
                filename = fs.save(photo.name, photo)
                photo_url = fs.url(f'temp/{filename}')

            context = {
                'data': data,
                'form': form,
                'photo': {'url': photo_url} if photo_url else None
            }

            if action == 'preview':
                return render(request, 'resume_app/resume.html', context)
            elif action == 'back':
                return render(request, 'resume_app/form.html', context)
    else:
        form = ResumeForm()

    return render(request, 'resume_app/form.html', {'form': form})
