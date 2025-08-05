# Resume Generator

Генератор резюме на Django: пользователь заполняет форму и получает оформленное PDF-резюме.

## Стек

- Python 3
- Django
- WeasyPrint (PDF генерация)
- HTML/CSS

## Как запустить

```bash
git clone https://github.com/maralaldo/resume-generator.git
cd resume-generator

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python manage.py runserver
```

### Открой в браузере:
http://127.0.0.1:8000/

#### Возможности
Форма с вводом данных (имя, опыт, образование и т.д.)
HTML-превью резюме
Генерация PDF-файла одним кликом
