from django.shortcuts import render, redirect,HttpResponse
from home.models import Student


# Create your views here.
def index(request):
    return render(request ,'index.html')

def nav(request):
    return render(request ,'nav.html')

def std(request):
    if request.method == 'POST':
        print('added')
        #Retrieve the user inputs
        std_roll = request.POST.get('std_roll')
        std_name = request.POST.get('std_name')
        std_email = request.POST.get('std_email')
        std_phone = request.POST.get('std_phone')

        #Creating object for model
        s = Student()
        s.roll = std_roll
        s.name = std_name
        s.email = std_email
        s.phone = std_phone
        s.save()
        return redirect('std')
    return render(request ,'std.html')