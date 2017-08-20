# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

import json

from realTime.pusher_api import PusherAPI

pusher = PusherAPI()


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def send_data(request):
    if request.method == "POST":
        json_string = request.body
        sensor_dict = json.loads(json_string)
        data = {'at': sensor_dict["at"], 'hum': sensor_dict["hum"], 'ft': sensor_dict["ft"]}
        pusher.trigger('my-channel', 'my-event', data)
        return HttpResponse('<h1>OK</h1>')
    else:
        return HttpResponseNotFound('<h1>Error</h1>')
