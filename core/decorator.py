from django.shortcuts import redirect, reverse

def cls_login_required(fn):
    def wrapper(request, *args, **kwargs):
        if not(request.user.is_authenticated):
            return redirect(f"{reverse('account_login')}?next={request.path}")
        
        return (fn(request, *args, **kwargs)        )
    return (wrapper)