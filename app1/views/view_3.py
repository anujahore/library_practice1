# import traceback

from django.http import HttpResponse
from django.shortcuts import redirect, render

from app1.models import Book

# Create your views here.



# url define karat eehe
def homepage(request):

    print(request.method)
    # print(request.GET)
    # print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('bname')
        price = request.POST.get('bprice')
        qty = request.POST.get('bqty')
        if not request.POST.get('bid'):
            book_name = name
            book_price = price
            book_qty = qty

            # print(book_name, book_price, book_qty)
            # creating object to stire data in database
            Book.objects.create(name=book_name, price=book_price, qty=book_qty)
            return redirect('home')
        
        else:
            b_id = request.POST.get('bid')
            book_obj = Book.objects.get(id=b_id)
            book_obj.name = name 
            book_obj.price = price
            book_obj.qty = qty
            book_obj.save()
            return redirect('show_all_books')

    elif request.method == 'GET':
        return render(request, 'homepage.html') # for normal html page
        # return render(request, 'bootstrap_practice.html')



def show_all_books(request):
    '''to show all books'''
    data = Book.objects.all()
    contxt = {'abc': data} # ithla name apn html page la use karto data display karayla 

    return render(request, 'show_books.html', context=contxt)



def edit_data(request, id):
    '''to edit/update the data by id'''
    book = Book.objects.get(id=id)
    return render(request, 'homepage.html', context={'single_book': book})


def delete_data(request, id):
    '''to delete the book '''
    print(request.method)
    if request.method == 'POST':
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExit as err_msg:
            traceback.print_exc()
            # print(err_msg)
            return HttpResponse(f'Book does not exits for id_-{id}')
        else:
            book.delete()
        return redirect('show_all_books')
    else:
        return HttpResponse(f'Request method:-"{request.method}" not allowed... only post method is allowed')


# url action la --> /home/ ashe dyav lagte i=otherwise te home/home as gheil and page not found error yeil 
# ------------------------------------------------------------------------------------------------------------------


from app1.forms import Student_Form
 
# Create your views here.
def form_view(request):
    context ={'form': Student_Form()}
    return render(request, "form_view.html", context)


from app1.forms import Book_Model_form

def book_model_view(req):
    '''
    this fuction is to create book model form view'''
    con = {'b_form': Book_Model_form()}
    return render(req, 'book_model_view.html', con)

from app1.forms import Test_form
def test_form_view(req):
    '''
    this function is for rendering the test_form
    '''
    data = {'data': Test_form()}
    return render (req, 'test_form_view.html', data)