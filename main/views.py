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

def index(request):
    context = {}
    return render(request, 'index.html', context)
