from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.db.models import Q
from ToxIn.models import *


class HomeView(View):

    def get(self, request):
        return render_to_response('index.html')


class SignInView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SignInView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        print('IN: '+str(request.POST))
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user:
            login(request, user)
            return JsonResponse({'a': {'username': user.username,
                                       'first_name': user.first_name,
                                       'last_name': user.last_name}})
        else:
            return JsonResponse({'e': 'Невірний логін або пароль'})


class SignUpView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SignUpView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        print('UO: '+str(request.POST))
        users = User.objects.filter(
            Q(username=request.POST['username']) | Q(email=request.POST['email'])
        )
        if users:
            return JsonResponse({'e': 'Користувач з такими даними вже існує'})
        else:
            user = User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password']
            )
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            profile = UserProfile(user=user)
            profile.save()
            return JsonResponse({'a': True})

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
