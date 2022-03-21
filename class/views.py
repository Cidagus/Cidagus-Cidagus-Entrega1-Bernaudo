from django.shortcuts import render
from .models import User,Professional,Business
from .forms import UserForm,UserSearch,ProfessionalForm,ProfessionalSearch,BusinessForm,BusinessSearch



def create(request):
    return render(request,"create/create.html",{})


def create_business(request):
    
    if request.method == 'POST':
            form = BusinessForm(request.POST)
            
            if form.is_valid():
                data = form.cleaned_data
                business = Business(name=data['name'], tin=data['tin'],area=data['area'],email=data['email'])
                business.save()
                return render(request, 'index/about.html', {'business': business})
                
    form = BusinessForm()
    return render(request, 'create/create_business.html', {'form': form})



def create_user(request):
    
    if request.method == 'POST':
            form = UserForm(request.POST)
            
            if form.is_valid():
                data = form.cleaned_data
                user = User(name=data['name'], alias=data['alias'],birthday=data['birthday'],email=data['email'],country=data['country'])
                user.save()
                return render(request, 'index/about.html', {'user': user})
                
    form = UserForm()
    return render(request, 'create/create_user.html', {'form': form})




def create_professional(request):
    
    if request.method == 'POST':
            form = ProfessionalForm(request.POST)
            
            if form.is_valid():
                data = form.cleaned_data
                professional = Professional(name=data['name'], ssn=data['ssn'],area=data['area'],email=data['email'])
                professional.save()
                return render(request, 'index/about.html', {'professional': professional})
                
    form = BusinessForm()
    return render(request, 'create/create_business.html', {'form': form})

