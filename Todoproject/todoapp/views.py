from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib import messages
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from todoapp.decorators import signin_required
from .models import Task

# Create your views here.

@method_decorator(signin_required,name='dispatch')
class Index(TemplateView):
    template_name = "index.html"

    def get(self,request):
        display = Task.objects.filter(user=self.request.user)
        task_id = request.GET.get('id','')
        task_action = request.GET.get('action','')
        if task_id!="" or task_action!="":
            task_obj = Task.objects.get(id=task_id)
            if task_action == 'delete':
                task_obj.delete()
            elif task_action == 'done':
                task_obj.completed = True
                task_obj.save()
            elif task_action == 'undo':
                task_obj.completed = False
                task_obj.save()
            return redirect('index')
        return render(request,self.template_name,{'name':display})

    def post(self,request):
        tasklist = request.POST.get('taskinput')
        task_id = request.POST.get('task-id','')
        if Task.objects.filter(user=request.user,title=tasklist).exists():
            messages.warning(request,'Task already exists !')
            return redirect('index')

        if task_id:
            tasks=Task.objects.get(id=task_id)
            tasks.title = tasklist
            tasks.save()
        else:
            Task.objects.create(title = tasklist,user=request.user)
        return redirect('index')

class Signup(TemplateView):
    template_name = "signup.html"

    def get_context_data(self, **kwargs):               
        context = super().get_context_data(**kwargs)
        return context

    def post(self,request):
        name = request.POST['uname']
        Email_id = request.POST['email']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        if p1 == p2:
            if User.objects.filter(username=name).exists():
                messages.info(request,'Username already exists')
                # return redirect('sign')
                return render(request,'signup.html')

            elif User.objects.filter(email=Email_id).exists():
                messages.info(request,'Email id already exists ! please choose another one')
                # return redirect('sign')
                return render(request,'login.html')

            else:
                user = User.objects.create_user(username=name,email=Email_id,password=p1)
            user.save()
            print('user created')
            return redirect('login')
        else:
            # return redirect('sign')
            return render(request,'signup.html')

class Login(TemplateView):
    template_name = "login.html"

    def dispatch(self, request, *args, **kwargs):
        if  request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self,request):
        username = request.POST['uname']
        password = request.POST['pwd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'username or password is incorrect')
            return redirect('login')

@signin_required
def userlogout(request):
    auth.logout(request)
    return redirect('login')