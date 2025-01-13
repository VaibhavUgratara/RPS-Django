from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import GameRoomInfo
import random
import secrets
import string
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    page_data={'title':'Home'}
    return render(request, 'index.html',context=page_data)

def join(request):
    page_data={'title':'Join'}
    if request.method == "POST":
        roomID= request.POST.get('room_id')
        try:
            ROOM = get_object_or_404(GameRoomInfo,room_id=roomID)
        except Http404:
            page_data["error"]=True
        else:
            return redirect(f"/game?room_ID={roomID}")
    return render(request,'joinroom.html',context=page_data)

def create(request):
    roomid=""
    for i in range(random.randint(5,10)):
        chars=string.ascii_letters+string.digits
        roomid+=secrets.choice(chars)
    ROOM=GameRoomInfo(room_id=roomid)
    ROOM.save()
    page_data={'title':'Create Room', 'R_ID':roomid}
    return render(request,'createroom.html',context=page_data)

@login_required
def gamewindow(request):
    room_ID=request.GET.get('room_ID')
    if(room_ID is None):
        return redirect("/")
    page_data={'title':'Play', 'R_ID':room_ID}
    ROOM=GameRoomInfo(room_id=page_data['R_ID'])
    ROOM.save()
    return render(request, 'gamewindow.html',context=page_data)

def signup_player(request):
    page_data={'title' : 'Signup'}
    if request.method == 'GET':
        form = UserCreationForm()
        page_data["form"]=form
    else:
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            page_data["success"]=True
        else:
            page_data["signup_err"]=True
            page_data["form_err"]=form.errors
    return render(request,'signup.html',context=page_data)

def login_player(request):
    page_data = {'title' : 'Login'}
    if request.method=='GET':
        form = LoginForm()
        page_data["form"]=form
        return render(request,'login.html',context=page_data)
    
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            player=authenticate(username=username,password=password)
            if player:
                login(request,player)
                return redirect('/')
            page_data["login_err"]=True
            return render(request,'login.html',context=page_data)
        
def logout_player(request):
    logout(request)
    return redirect('/')
