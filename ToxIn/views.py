from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

def home(request):
    return render_to_response('index.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        u = User.objects.get(username=request.POST['login'])
        print(u)
        return JsonResponse({'a': u.username})
    return None

@csrf_exempt
def register(request):
    if request.method == 'POST':
        u = User.objects.filter(username=request.POST['login'])
        e = User.objects.filter(email=request.POST['email'])
        if u:
            return JsonResponse({'e': 'Користувач з таким логіном вже існує'})
        elif e:
            return JsonResponse({'e': 'Користувач з такою ел.поштою вже існує'})
        else:
            u = User.objects.create_user(request.POST['login'], request.POST['email'], request.POST['passwd'])
            u.first_name = request.POST['username']
            u.save()
            return JsonResponse({'a': True})
    return None

@csrf_exempt
def getallusers(request):
    if request.method == 'POST':
        users = list(map(lambda u: u.first_name, User.objects.all()))
        return JsonResponse({'a': users})
    return None
