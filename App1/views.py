from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    return HttpResponse("ok")

def home(request):
    return render(request,'home.html')

class FormView(View):
    form_class = UserForm
    template_name = 'loginForm.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('basic:index')
        else:
            return render(request, 'form-login.html', {'message': "Either username or password is not valid"})


def SignUp(request):
    # form_class = UserForm
    # template_name = 'registerForm.html'

    print('yuyd')
    print(request.method)

    # if request.method=='GET':
        # form = form_class(None)
        # print('ok')
        # return render(request, template_name, {'form': form})
    # else :
    #     form = form_class(request.POST)
    #     again = request.POST['again']
        
    #     if form.is_valid():
    #         user = form.save(commit=False)

    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']

    #         if again != password:
    #             return render(request, template_name, {'message': "password fields don't match"})

    #         user.set_password(password)
    #         user.save()

    #         return redirect('/')

    # def post(self, request):
