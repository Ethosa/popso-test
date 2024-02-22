from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from werkzeug.security import check_password_hash, generate_password_hash


@csrf_exempt
def auth(req: HttpRequest) -> HttpResponse:
    # some validation here lol
    return JsonResponse({"response": "success"})

