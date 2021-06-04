from django.http.response import HttpResponseRedirect
from django.shortcuts import render

#for Register
from .forms import AuthenticatingElements,MoreElements
from django.http import HttpResponse

#for Log In

from django.contrib.auth import login,authenticate

from .models import userProfile

#view for homepage
def homepage(request):
    return render(request,"firstpage.html")

#view for registration page
def registration(request):
    moreElementsForm = MoreElements(data= request.POST)
    AuthenticatingElementsForm = AuthenticatingElements(data=request.POST)
    flag = False #to check if registration occoured
    if request.method == "POST":
        moreElementsForm = MoreElements(data= request.POST)
        AuthenticatingElementsForm = AuthenticatingElements(data=request.POST)
        
        if moreElementsForm.is_valid() and AuthenticatingElementsForm.is_valid():
            #assigning username and emailid to authuser
            authuser=AuthenticatingElementsForm.save()
            #setting authuser's passowrd as the user's password
            authuser.set_password(authuser.password)
            authuser.save()
            #assigning phone number and name elements to the model
            profile = moreElementsForm.save(commit=False)
            #assigning authuser to "user" object of the model
            profile.user = authuser
            profile.save()
            flag = True
            

    return render(request,"signupuser.html",{'Aform':AuthenticatingElementsForm,"Eform":moreElementsForm,"flag":flag})

#view for login page
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        currentLogin = authenticate(username = username , password = password)
        if (currentLogin):
            login(request,currentLogin)
            userObject = userProfile.objects.all()
            for users in userObject:
                #print(users.name,users.user)
                NameofUser = ""
                PhoneofUser = ""
                if str(users.user) == str(username):
                    NameofUser = users.name
                    PhoneofUser = users.phoneNumber
                    #print(NameofUser,PhoneofUser)
                    break
            return render(request,"userdetails.html",{"Name":NameofUser,"PhoneNumber":PhoneofUser})
        else:
            return HttpResponse("Invalid username or Password")
    
    return render(request,"login.html")


