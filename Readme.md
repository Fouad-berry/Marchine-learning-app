## Marchine Learning app
une web app de machine learning utilisant l'api de openai pour repondre aux questions de l'utilisateur; le tout en utilisant gpt3
## Description
- Ce projet est une application web multilingue construite avec Django. Il permet aux utilisateurs de changer de langue pour l'interface. Le projet montre comment implémenter l'internationalisation (i18n) et la localisation (l10n) dans une application Django.
## Features
- Multilingual support (e.g., English, French)
- Dynamic language switching
- Bootstrap for responsive design

## Prerequisites
- Python 3.10.4 ou supérieur
- pip (installateur de paquets Python)
- Virtualenv (facultatif, pour créer des environnements isolés)

## Setup Instructions

### 1. Clone the Repository
Clone the project repository from GitHub.

```bash
git clone https://github.com/yourusername/projectname.git
cd projectname
```

### 2. Create a Virtual Environment
It is recommended to create a virtual environment to manage dependencies.

```bash
py -m venv .env
source .env\Scripts\activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install the required Python packages using `pip`.

```bash
pip install -r requirements.txt
```

### 4. Database Setup
Apply migrations to set up the database.

```bash
python manage.py migrate
```

### 5. Create a Superuser
Create a superuser to access the Django admin interface.

```bash
python manage.py createsuperuser
```

Follow the prompts to set up a superuser account.


### 6. Run the Development Server
Start the development server to test the application locally.

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000`.

### Openapi api key 
Go to the .env files and paste your openai key to use the chatbot
```
OPENAI_API_KEY=
```

## Language Switching

### Adding New Languages
1. Open `settings.py` and add the new language code to `LANGUAGES`.

```python
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
]
```

2. Create message files for the new language.

```bash
django-admin makemessages -l <language_code>
```

For example, to add Spanish:

```bash
django-admin makemessages -l es
```

3. Translate the message files located in the `locale` directory.

4. Compile the translations.

```bash
django-admin compilemessages
```

5. Restart the server to apply the changes.
