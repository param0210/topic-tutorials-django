from django.shortcuts import render,redirect
from django.http import HttpResponse
from aiohttp.client import request
from .models import * 
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def profile(request):
    if request.method=='POST' and request.is_ajax():
        username=request.POST['username']
        email=request.POST['email']
        image=request.FILES.get('img')
        obj=MyUser.objects.create(username=username,email=email,image=image)
        print(obj)
        return HttpResponse('')
        
        

    else:
        return render(request,'accounts/profile.html')
