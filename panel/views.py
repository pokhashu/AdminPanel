from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import *


def index(request):
    return redirect('/admin')


def getSchedule(request):
    posts = Publicaton.objects.all()
    schedule = []
    for i in posts:
        schedule.append([i.city.lower(), [i.time.hour, i.time.minute]])
    response = {'data': schedule}
    return JsonResponse(response)


def getChatId(request):
    g = Groups.objects.all()
    city = request.GET["city"].lower()
    try:
        chatId = Groups.objects.get(city=city).chat_id
    except:
        chatId = 0

    return JsonResponse({"data": chatId})


def askForApproval(request):
    if request.GET:
        name = request.GET["name"]
        chat_id = request.GET["chat_id"]
        city = request.GET["city"].lower()

        Groups.objects.create(name=name, chat_id=chat_id, city=city)

        return JsonResponse({"data": "200"})
    else:
        return HttpResponse({"data": "403"})


def isGroupApproved(request):
    if request.GET:
        if "chat_id" not in request.GET:
            return JsonResponse({"data": False})
        if request.GET["chat_id"]:
            chat_id = request.GET["chat_id"]
        try:
            approved = Groups.objects.get(chat_id=chat_id).approved
        except:
            approved = False

        return JsonResponse({"data": approved})


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>404 <h3>Error</h3></h1>')
