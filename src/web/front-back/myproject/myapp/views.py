from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core import serializers
from myapp.models import User
import json


# Create your views here.
@require_http_methods(["GET"])
def show_user(request):
    response = {}
    try:
        users = User.objects.all()
        response['list'] = json.loads(serializers.serialize("json", users))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
