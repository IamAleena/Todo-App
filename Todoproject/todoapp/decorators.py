from django.shortcuts import redirect

def signin_required(function):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return function(request,*args,**kwargs)
        else:
            return redirect('login')
    return wrapper

