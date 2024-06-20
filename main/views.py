import os
from django.http import HttpResponseRedirect
from django.utils.translation import activate
from django.conf import settings
import logging
from django.shortcuts import render
from .models import Article
from dotenv import load_dotenv
import openai
from django.utils import translation

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'index.html', context)

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_liste.html', {'articles': articles})

# Récupérer la clé API depuis les variables d'environnement
openai.api_key = os.getenv('OPENAI_API_KEY')

def chatbot(request):
    # Initialisation de l'historique si non présent
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    if request.method == 'POST':
        # Récupère les données du formulaire
        question = request.POST.get('question')
        clear_history = request.POST.get('clear_history')

        # Si l'utilisateur demande à supprimer l'historique
        if clear_history:
            request.session['chat_history'] = []  # Efface l'historique
            request.session.modified = True  # Enregistre les modifications
        else:
            # Appel à l'API OpenAI pour obtenir la réponse
            response_text = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question},
                ]
            ).choices[0].message['content'].strip()

            # Ajout de la question et de la réponse à l'historique
            request.session['chat_history'].append({
                'role': 'user',
                'question': question,
                'response': response_text
            })
            request.session['chat_history'].append({
                'role': 'bot',
                'response': response_text
            })
            
            # Enregistre les modifications dans la session
            request.session.modified = True

    return render(request, 'chatbot.html', {'chat_history': request.session.get('chat_history')})

