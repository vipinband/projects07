from django.shortcuts import render

from django.shortcuts import render

from jp.models import User, City, State


def showHome(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})

#def openUserPage(request):
 #   type=request.GET.get("type")
#    return render(request,"user.html",{"type":type})

def openUserPage(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})



def userRegister(request):
    fname=request.POST.get("user_fname")
    lname=request.POST.get("user_lname")
    ustate=request.POST.get("user_state")
    ucity=request.POST.get("user_city")
    uemail=request.POST.get("user_email")
    upassword=request.POST.get("user_paswword")
    udor=request.POST.get("user_dor")
    res=City.objects.values("city_id").filter(city_name=ucity)  #getting city_id through city_name
    city_id=0
    for x in res:
        city_id=x["city_id"]  #[city_id:city_name] ,x["city_id]--getting city_id of city_name
        print('city_id')

    usr=User(first_name=fname,last_name=lname,city_name=City.objects.get(city_id=city_id),emailid=uemail,password=upassword,date=udor)
    usr.save()
    type=request.GET.get("type")
    return render(request,"index.html",{"message":"user registered successfully","type":type,'res':res})



def getCityFromState(request):
    sel_state = request.GET.get("state")
    res = State.objects.values('id').filter(name=sel_state)
    id = 0
    for x in res:
        id = x["id"]
    res1 = City.objects.values('city_name').filter(state_name=id)
    city_names = ["City"]
    if not res1:
        city_names = ["No City Available"]
    else:
        for x in res1:
            city_names.append(x['city_name'])

    res2 = State.objects.values('name')
    states = ["State"]
    for x in res2:
        states.append(x["name"])
        return render(request, "index.html",{"type": 'h_NewRegister', "city_names": city_names, "states": sel_state, "key": "one"})


def loginUser(request):
    username=request.POST.get("user_email")
    password=request.POST.get("user_password")

    res=User.objects.filter(emailid=username,password=password)
    print(res)
    if not res:
        type = "h_user"
        return render(request,"index.html",{"type":type,"message":"user not valid"})
    else:
        type = "u_home"
        res=User.objects.all()
        for x in res:
            name=x["name"]
            email=x["emailid"]
        return render(request,"userHome.html",{"type":type,"popup":"registered successfully","name":name,"email":email})
 #       print("invalid details")
   # else:
        #type = 'h_user'
    #    res=User.objects.all()
     #   return render(request,"index.html",{"type":type,"details":res,"message":"logged in successfully"})


def openUserHome(request):
    type=request.GET.get("type")
    return render(request,"userHome.html",{"type":type})


def openNewRegister(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def openAbout(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})


def showUserHome(request):
    type=request.GET.get("type")
    return render(request,"userHome.html",{"type":type})


class UserUpdate():
    model=User
    template="user_update.html"
    fields=["first_name","last_name","city_name","emailid","password","date"]
    success_url="/showUserHome/"