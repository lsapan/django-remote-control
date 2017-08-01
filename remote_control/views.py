# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from remote_control.requests import handle_request


@csrf_exempt
def receive_request(request):
    signed_request = json.loads(request.body).get('request')
    result = handle_request(signed_request)
    return JsonResponse(result)
