from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from werkzeug.security import check_password_hash, generate_password_hash

from .models import User


def auth_middleware(req: HttpRequest) -> HttpResponse | None:
    if len(req.GET.keys()) != 2:
        return JsonResponse(
            {"error": "invalid request"},
            status=400,
            json_dumps_params={'ensure_ascii': False}
        )
    elif 'login' not in req.GET or 'password' not in req.GET:
        return JsonResponse(
            {"error": "invalid request"},
            status=400,
            json_dumps_params={'ensure_ascii': False}
        )
    return None


@csrf_exempt
def auth(req: HttpRequest) -> HttpResponse:
    if req.method == "OPTIONS":
        return HttpResponse('', status=200)
    if _ := auth_middleware(req) is not None:
        return _
    user = None
    try:
        user = User.objects.get(login=req.GET['login'])
    except User.DoesNotExist:
        return JsonResponse(
            {"error": "неправильный логин или пароль!"},
            status=403,
            json_dumps_params={'ensure_ascii': False}
        )
    if not check_password_hash(user.password, req.GET['password']):
        return JsonResponse(
            {"error": "неправильный логин или пароль!"},
            status=403,
            json_dumps_params={'ensure_ascii': False}
        )
    return JsonResponse({"response": {
        "id": user.id
    }})


@csrf_exempt
def register(req: HttpRequest) -> HttpResponse:
    if req.method == "OPTIONS":
        return HttpResponse('', status=200)
    if _ := auth_middleware(req) is not None:
        return _
    user = None
    try:
        user = User.objects.get(login=req.GET['login'])
        return JsonResponse(
            {"error": "такой пользователь уже существует"},
            status=403,
            json_dumps_params={'ensure_ascii': False}
        )
    except User.DoesNotExist:
        pass
    user = User.objects.create(
        first_name="", last_name="",
        login=req.GET['login'],
        password=generate_password_hash(req.GET['password'])
    )
    user.save()
    return JsonResponse({"response": {
        "id": user.id
    }}, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def update_user(req: HttpRequest) -> HttpResponse:
    user = None
    try:
        user = User.objects.get(login=req.GET['oldLogin'])
    except User.DoesNotExist:
        return JsonResponse(
            {"error": "неправильный логин или пароль!"},
            status=403,
            json_dumps_params={'ensure_ascii': False}
        )
    if not check_password_hash(user.password, req.GET['oldPassword']):
        return JsonResponse(
            {"error": "неправильный логин или пароль!"},
            status=403,
            json_dumps_params={'ensure_ascii': False}
        )
    update_fields = []
    if 'password' in req.GET:
        user.password = generate_password_hash(req.GET['password'])
        update_fields.append('password')
    if 'login' in req.GET:
        user.login = req.GET['login']
        update_fields.append('login')
    if 'first_name' in req.GET:
        user.first_name = req.GET['first_name']
        update_fields.append('first_name')
    if 'last_name' in req.GET:
        user.last_name = req.GET['last_name']
        update_fields.append('last_name')
    user.save(update_fields=update_fields)
    return JsonResponse({'response': "success"})


@csrf_exempt
def get_by_id(req: HttpRequest, user_id: int) -> HttpResponse:
    user = None
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse(
            {"error": "Пользователя с таким ID не существует!"},
            status=403,
            json_dumps_params={'ensure_ascii': False}
        )
    return JsonResponse({'response': {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }})

