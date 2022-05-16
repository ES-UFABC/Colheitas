from django.shortcuts import redirect, render

from ..forms import AccountForm
from ..models import User


def update_account(request,id):
    account_to_update = User.objects.get(id=id)
    form = AccountForm(request.POST or None, instance=account_to_update)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'account/account_update.html', {'form': form, 'account': account_to_update})

def private_profile(request, id):
    user = User.objects.get(id=id)
    return render(request, 'private_profile.html', {'account':user})