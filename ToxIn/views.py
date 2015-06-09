from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as enter
from ToxIn.models import *

def home(request):
    return render_to_response('index.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        print('LOGIN: '+str(request.POST))
        u = authenticate(username=request.POST['username'], password=request.POST['passwd'])
        if u:
            enter(request, u)
            return JsonResponse({'a': {'username': u.username, 'first_name': u.first_name, 'last_name': u.last_name}})
        else:
            return JsonResponse({'e': 'Невірний логін або пароль'})
    return None

@csrf_exempt
def register(request):
    if request.method == 'POST':
        print('REG: '+str(request.POST))
        u = User.objects.filter(username=request.POST['username'])
        e = User.objects.filter(email=request.POST['email'])
        if u:
            return JsonResponse({'e': 'Користувач з таким логіном вже існує'})
        elif e:
            return JsonResponse({'e': 'Користувач з такою ел.поштою вже існує'})
        else:
            u = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['passwd'])
            u.first_name = request.POST['first_name']
            u.last_name = request.POST['last_name']
            u.save()
            up = UserProfile(user=u)
            up.save()
            return JsonResponse({'a': True})
    return None

@csrf_exempt
def getallusers(request):
    if request.method == 'POST':
        username = request.POST['username']
        conv = lambda u: {'username': u.username, 'first_name': u.first_name, 'last_name': u.last_name}
        users = list(map(conv, User.objects.filter(is_staff=False).exclude(username=username)))
        return JsonResponse({'a': users})
    return None

@csrf_exempt
def getallcontacts(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.POST['username'])
        contacts = Contact.objects.filter(user=user)
        conv = lambda c: {'username': c.contact.username,
                          'first_name': c.contact.first_name,
                          'last_name': c.contact.last_name

                          }
        print(list(map(conv, contacts)))
        return JsonResponse({'a': list(map(conv, contacts))})
    return None

@csrf_exempt
def addcontacttouser(request):
    if request.method == 'POST':
        contact = User.objects.get(username=request.POST['contact'])
        user = User.objects.get(username=request.POST['user'])
        creator = Contact(user=user, contact=contact, creator=True)
        creator.save()
        joined = Contact(user=contact, contact=user, creator=False)
        joined.save()
        return JsonResponse({'a': True})
    return None

@csrf_exempt
def getuserprofile(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(user=user)
        conv = lambda up: {'first_name': up.user.first_name,
                           'last_name': up.user.last_name,
                           'email': up.user.email,
                           'workplace': up.workplace,
                           'position': up.position
                           }
        return JsonResponse({'a': conv(user_profile)})
    return None

@csrf_exempt
def setuserprofile(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        user = User.objects.get(username=username)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        user_profile = UserProfile.objects.get(user=user)
        user_profile.workplace = request.POST['workplace']
        user_profile.position = request.POST['position']
        user_profile.save()
        return JsonResponse({'a': True})
    return None
