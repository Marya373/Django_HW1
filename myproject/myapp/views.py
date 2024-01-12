import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse('Это главная страница! Приятно познакомиться! Меня зовут Мария Файвисович')

def about(request):
    logger.info('Index page accessed')
    return HttpResponse('Я живу в городе Москва. Мне 44 года и, как сказал мой руководитель, Ваше программирование - это хобби)')


    # try:
    #     # some code that might raise an exception
    #     result = 1/0
    # except Exception as e:
    #     logger.exception(f'Error in about page: {e}')
    #     return HttpResponse('Oops, something went wrong.')
    # else:
    #     logger.debug('About page accessed')
    #     return HttpResponse('This is the about page.')
