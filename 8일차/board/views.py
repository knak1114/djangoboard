from django.shortcuts import render,redirect
from .models import Board

# Create your views here.
def index(request):
    return render(request, 'board/index.html')


def list(request):
    b = Board.objects.order_by('-date')
    context = {
        'bset':b
    }
    
    return render(request, 'board/list.html', context)

def detail(request, bpk):
    b = Board.objects.get(id=bpk) 
    b.incrementReadCount()
    context = {
        'b':b
    }
    return render(request, 'board/detail.html',context)


def create(request):
    if request.method =="POST":
        nt = request.POST.get('ntitle')
        nw = request.POST.get('nwriter')
        nc = request.POST.get('ncontent')
        Board(title=nt, writer=nw, content=nc).save()
        return redirect('board:list')
    return render(request, 'board/create.html')

def update(request, bpk):
    b = Board.objects.get(id=bpk)
    context = {
        'b':b
    }
    if request.method == "POST":
        ut = request.POST.get('utitle')
        uw = request.POST.get('uwriter')
        uc = request.POST.get('ucontent')
        b.title, b.writer, b.content = ut, uw, uc
        b.save()
        return redirect('board:detail', bpk)
    return render(request, 'board/update.html',context)


def delete(request,bpk):
    b = Board.objects.get(id=bpk)
    b.delete()
    return redirect('board:list')