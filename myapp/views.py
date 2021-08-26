from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from .models import ticket
from .models import Tours
from .models import img
# Create your views here.
def index(request):
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.details = 'No thing'
    objs = Feature.objects.all()
    context = {
        'name' : 'Khanh Tran',
        'age' : 20,
        'nationality' : 'Vietnam',
    }
    return render(request, 'index.htm',{'objs' : objs})

def counter(request):
    text = request.POST['text']
    # w3band_recieved = request.POST['send']
    amount_of_text = len(text.split())
    return render(request, 'counter.htm', {'amount' : amount_of_text})

def w3band(request):
    tour1 = Tours()
    tour1.content = 'Ha Long Bay'
    tour1.day = 'Fri 26'
    tour1.details= ', in the Gulf of Tonkin, includes some 1,600 islands and islets, forming a spectacular seascape of limestone pillars. Because of their precipitous nature, most of the islands are uninhabited and unaffected by a human presence.'
    tour1.button = 'Let\'s go'

    tour2 = Tours()
    tour2.content = 'Ha Noi'
    tour2.day = 'Wed 24'
    tour2.details= ' is a capital of Vietnam'
    tour2.button = 'Let\'s go'

    tour3 = Tours()
    tour3.content = 'TP. Ho Chi Minh'
    tour3.day = 'Fri 26'
    tour3.details= ', in the Gulf of Tonkin, includes some 1,600 islands and islets, forming a spectacular seascape of limestone pillars. Because of their precipitous nature, most of the islands are uninhabited and unaffected by a human presence.'
    tour3.button = 'Let\'s go'
    
    img1 = img()
    img1.name = "Khanh Tran"

    img2 = img()
    img2.name = "Ngao"

    img3 = img()
    img3.name = "Dan"

    ticket1 = ticket()
    ticket1.month = 'September'
    ticket1.numb = 2

    ticket2 = ticket()
    ticket2.month = 'October'
    ticket2.numb = 99
    
    ticket3 = ticket()
    ticket3.month = 'November'
    ticket3.numb = 7

    tickets = [ticket1,ticket2,ticket3]

    tourist = {
        'tours' : [tour1,tour2,tour3],
        'imgs' : [img1,img2,img3],
        'tickets' : tickets
    }

    return render(request, 'page2.htm',tourist)

def w3result(request):

    

    result = {
        'name' : request.POST['name'],
        'message' : request.POST['message'],
        'email' : request.POST['email']
    }
    return render(request, 'w3result.htm', result)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/w3band')
        else:
            messages.info(request, 'Sai rồi bạn ơi !!!')
            return redirect('login')
    else:
        return render(request,'login.htm')

def logout(request):
    auth.logout(request)
    return redirect('/w3band')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirm-password']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is Already')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password= password)
                user.save()
                return redirect('login')
        else :  
            messages.info(request, 'Password not the same')      
            return redirect('register')
    else:
        return render(request, 'register.htm')