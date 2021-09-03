from django.http import HttpResponse
from django.shortcuts import render
from example.models import Book

# Create your views here.
def insert(request):
    name = "C for Begginer"# request.GET["name"]
    bid =  132 #request.GET["bid"]
    author= "Manjit"#request.GET["author"]    
    price=180# request.GET["price"]
    book=Book(name=name, bid=bid, author=author,price=price)
    book.save()
    return HttpResponse('Inserted')
def delete(request):
    book = Book.objects.filter(price=100)
    if len(book)==0:
        return HttpResponse("none")
    else:
        book[0].delete()
        return HttpResponse("Delete name "+str(book[0].name))
def find(request):
    book=Book.objects.filter(price=180) & Book.objects.filter(author='Manjit')
    if len(book) == 0:
        return HttpResponse("none")
    else:
        return HttpResponse("find name = "+str(book[0].name))
def update(request):
	book=Book.objects.filter(bid=400)
	if len(book)==0:
		return HttpResponse("None")
	else:
		book[0].author="New Name"
		book[0].save()
		return HttpResponse("Book Name = " + str(book[0].author))

def edit(request):
    name=""
    bid=""
    price=""
    author=""
    result="" 
    cmd=""
    if request.GET:
        cmd=request.GET["cmd"]
    if cmd=="Insert":
        name=request.GET["name"]
        bid= request.GET["bid"]
        price= request.GET["price"]
        author=request.GET["author"]
        book= Book(name=name, bid=bid, price=price, author=author)
        book.save()
        result="Inserted Sucsesfully"
    if cmd =="Search":
        bid=request.GET["bid"]
        book=Book.objects.filter(bid=bid)
        if len(book) == 0:
            result = "No such data exist"
        else:
            name=book[0].name
            bid=book[0].bid
            price=book[0].price
            author=book[0].author
            result = "Found"
    if cmd == "Delete":
        bid=request.GET["bid"]
        book=Book.objects.filter(bid=bid)
        if len(book)==0:
            result ="record you want to delete does not exist"
        else:
            name=book[0].name
            bid=book[0].bid
            price=book[0].price
            author=book[0].author
            book[0].delete()
            result ="Recorde deleted"
    if cmd=="Update":
        
        bid=request.GET["bid"]

        
        book=Book.objects.filter(bid=bid)
        if len(book)==0:
            result="data not found"
        else:
            book[0].name= name=request.GET["name"]
        
            book[0].price=price= request.GET["price"]
            book[0].author=author=request.GET["author"]
        
        
            book[0].save()
            result="Updated"
    
    data={"name":name, "bid":bid, "price":price, "author":author,"result":result}
    return render (request,"Database.html",{"data":data})
    
        
        
    
