from django import forms 

class UserForm(forms.Form):
    name= forms.CharField(max_length=30)
    alias= forms.CharField(max_length=30)
    email= forms.EmailField(max_length=30)
    birthday= forms.CharField(max_length=20)
    country= forms.CharField(max_length=30) 

class UserSearch(forms.Form):
    alias= forms.CharField(max_length=30)
    
class ProfessionalForm(forms.Form):
    name= forms.CharField(max_length=30)
    email= forms.EmailField(max_length=30)
    ssn= forms.IntegerField()
    area= forms.CharField(max_length=20)

class ProfessionalSearch(forms.Form):
    name= forms.CharField(max_length=30)
    
class BusinessForm(forms.Form):
    business_name= forms.CharField(max_length=30)
    tin= forms.IntegerField()
    area= forms.CharField(max_length=30)
    email= forms.EmailField(max_length=30)
    
class BusinessSearch(forms.Form):
     business_name= forms.CharField(max_length=30)
    
    