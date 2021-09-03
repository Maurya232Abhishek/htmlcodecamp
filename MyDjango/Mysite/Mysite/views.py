from django.http import HttpResponse
from django.shortcuts import render
from example.models import Book
import  requests
import  json
import datetime as dt
def index(request):
    html = "<h1>Default View</h1>"
    return HttpResponse(html)
def hello(request):
    return HttpResponse("Hello")
def manas(request):
    return HttpResponse("Chai☕")
def calculate(request):
    a=0
    b=0
    ans=0
    temp=0
    json={}
    cmd=""
    if request.GET:
        a=int(request.GET["a"])
        b=int(request.GET["b"])
        cmd=request.GET["cmd"]
    if cmd=="add":
        ans = a+b
    elif cmd=="sub":
        ans = a-b
    elif cmd == "mul":
        ans = a*b
    elif cmd == "div":
        ans = a/b
    data={"a":a,"b":b,"ans":ans}
    return render(request,"SimpleCalc.html",{"data":data}) 
def wheather(request):
    appid="4a1f8a61b74546825af1e0be106e797b"
    city="delhi"
    result=""
    temp=""
    humidity=""
    
    if request.GET:
        city=request.GET["city"]
    url="https://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}&units=metric".format(appid,city)
    try:
        response=requests.get(url)
        code=response.status_code
        if code != 200:
            result ="!!!Something went wrong or You entered the wrong city name!!!"
        else:
            jsondata=json.loads(response.text)
            temp=jsondata["main"]["temp"]
            humidity=jsondata["main"]["humidity"]
            result=""
    except:
        result="!!!Something went wrong or You entered the wrong city name!!!"
                
    data={"city":city,"temp":temp,"humidity":humidity,"result":result}
    return render(request,"Wheather.html",{"data":data})
    