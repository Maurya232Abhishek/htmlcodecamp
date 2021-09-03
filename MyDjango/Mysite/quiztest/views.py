from django.http import HttpResponse
from django.shortcuts import render
from quiztest.models import quizClass
# Create your views here.

def test(request):
     
    qno = 1
    que=""
    opta=""
    optb=""
    optc=""
    optd=""
    ans=""
    mark=0
    rightans=""
    score=0
    cmd=""
    if request.GET:
        ans = request.GET["ans"]
        #score = request.GET["score"]
        if request.GET["cmd"] :
            cmd=request.GET["cmd"]
            
        qno = int(request.GET["qno"])
        if qno==1:
            qno+=1
        score = int(request.GET["score"])
        
    q = quizClass.objects.filter(qno=qno)
    qp= quizClass.objects.filter(qno=qno)
    if qno>1:
        qp= quizClass.objects.filter(qno=qno-1)
    if len(q)==0:
            
            return HttpResponse(score)
        
    qno=q[0].qno
    que=q[0].que    
    opta=q[0].opta
    optb=q[0].optb
    optc=q[0].optc
    optd=q[0].optd
    rightans=qp[0].rightans
    
        
    d={1:qp[0].opta,2:qp[0].optb,3:qp[0].optc,4:qp[0].optd}
    if d[rightans] == ans:
        mark=1
    if cmd == "Next":
        score += mark
        qno += 1
        if qno==1:
            qno +=1
    if cmd == "Previous":
        if qno!=1:
            qno -= 1
    
    
      
    data = {"qno":qno,"que":que,"opta":opta,"optb":optb,"optc":optc,"optd":optd,"rightans":rightans,"score":score,"ans":ans,"cmd":cmd}
    
        
    return render(request,"quiz.html",{"data":data})
