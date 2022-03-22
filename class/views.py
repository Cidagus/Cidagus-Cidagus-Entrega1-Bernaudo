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
                business = Business(business_name=data['business_name'], tin=data['tin'],area=data['area'],email=data['email'])
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
                
    form = ProfessionalForm()
    return render(request, 'create/create_professional.html', {'form': form})




def search(request):
    return render(request,"search/search.html",{})



def search_business(request):
    business = []
    data = request.GET.get('business_name', None)
    
    if data is not None:
        business = Business.objects.filter(business_name__icontains=data)
    
    search = BusinessSearch()
    return render(request, "search/search_business.html",
                  {'search': search, 'business': business, 'data':data})
    


def search_professional(request):
    professional = []
    data = request.GET.get('name', None)
    
    if data is not None:
        professional = Professional.objects.filter(name__icontains=data)
    
    search = ProfessionalSearch()
    return render(request, "search/search_professional.html",
                  {'search': search, 'professional': professional, 'data':data})



def search_user(request):
    user = []
    data = request.GET.get('alias', None)
    
    if data is not None:
        user = User.objects.filter(alias__icontains=data)
    
    search = UserSearch()
    return render(request, "search/search_user.html",
                  {'search': search, 'user': user, 'data':data})
