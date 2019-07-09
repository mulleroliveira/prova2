from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required



def index(request):
    return render(request, 'index.html')


@login_required
def users(request):
    users = User.objects.all()
    return render(request, 'usuario/listagem.html', {"users":users})


@permission_required("delete_user", login_url="/gestao/listagem/")
@login_required
def delete(request, id):
    user = User.objects.all().get(pk=id).delete()
    messages.success(request, "Operação concluida")
    return redirect("/gestao/listagem/")