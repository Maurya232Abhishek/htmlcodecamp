from django.http import HttpResponse
from django.shortcuts import render
from bank.models import AccountDetail

# Create your views here.
def registration(request):
    accno=""
    name=""
    balance=0
    if request.GET:
        accno=request.GET["accno"]
        name=request.GET["name"]
        balance=request.GET["balance"]
        account=AccountDetail(accno=accno, name=name, balance=balance)
        account.save()
    data={"accno":accno,"name":name,"balance":balance}
    return render(request,"registration.html",{"data":data})
def withdrawDeposit(request):
    accno=""
    amount=0
    cmd=""
    result=""
    balance=0
    
    if request.GET:
        cmd = request.GET["cmd"]
        accno = request.GET["accno"]
        amount = int(request.GET["amount"])
    account = AccountDetail.objects.filter(accno = accno)
    if len(account) == 0:
        result="No Account"
    else:
        if cmd == "Withdraw":
            account[0].balance += amount
            account[0].save()
        if cmd == "Deposit":
            account[0].balance += amount
            account[0].save()
    data={"result":result , "balance" : balance, "accno":   accno, "amount":amount}
    return render(request,"withdrawDeposit.html",{"data":data})
        
        
