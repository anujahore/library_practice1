
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import login, logout, authenticate

def view_c(request):
    return HttpResponse('in view_c')

def view_d(request):
    return HttpResponse('in view_d')



class Home(View):
    
    def get(self, request):
        print('in get method')
        return HttpResponse('in get method')
    
    def post(self, request):
        # print('in post method', request.POST, request.body) #request.body -- for getting row data --> b'abciohicbquwihxnwuesidnsbdufhdjcbvufwidjfguwdjhfuhd\r\nqkjhxnbjhyuajdcw'
                            # request.body--> op in bytes -->
                            # to convert into str --> .decode("utf-8")

        # curl -- 
        # curl -X POST "http://127.0.0.1:8000/cbv-home/" --> post method
        #  ---> a) curl -d "data1=anuja&age=24&city=anjangon" "http://127.0.0.1:8000/cbv-home/" --> for adding data in post method
        # ----> b) curl -X POST -F "name=anuja" -F "age=24" "http://127.0.0.1:8000/cbv-home/"
        # crul "http://127.0.0.1:8000/cbv-home/" -- > to get req
        # 
        print('in post method', request.POST)
        return HttpResponse('in post method')
    
    def put(self, request):
        print('in put method')
        return HttpResponse('in put method')

    def patch(self, request):
        print('in patch method')
        return HttpResponse('in patch method')

    def delete(self, request):
        # print('in delete method')
        return HttpResponse('in delete method', status=204)




def anuja(req):
    return HttpResponse('jsncuishsiu')


def user_login(req):
    user_name = req.POST.get('username')
    user_password = req.POST.get('password')
    user = authenticate(user_name, user_password)
    if user:
        login(req, user)
        return HttpResponse('<h1>Successfully logged in....!<h1>')
