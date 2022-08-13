
from django import forms
from app1.models import Book

# from django import forms
   
# creating a form 
class Student_Form(forms.Form):
    '''
    this form is just for practice (class practice)'''
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())

# print(Student_Form())
class Test_form(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField(help_text = 'Enter your age here')
    city = forms.CharField()

class Book_Model_form(forms.ModelForm): # for modelform
    class Meta:
        model = Book
        # fields = '__all__' #(all fields sathi form banel)
        # fields = ('name','qty') # for custom fields
        fields = '__all__' #want all
        # exclude = ('name',) # but excluding name
