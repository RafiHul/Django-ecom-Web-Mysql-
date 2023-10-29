from core.models import Produk
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewItem, EditItem

def detail(request,pk):
    produk = get_object_or_404(Produk,pk=pk)

    return render(request, 'items/detail.html',{
        'produk': produk,
    })

@login_required
def new(request):
    if request.method == "POST":
        form = NewItem(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
        
            return redirect('items:detail', pk=item.id)

    else:
        form = NewItem()

    return render(request, 'items/new.html',{
        'form':form,
        'title':"New Item"
    })

@login_required
def edit(request,pk):
    produk = get_object_or_404(Produk, pk=pk, created_by=request.user)
    if request.method == "POST":
        form = EditItem(request.POST, request.FILES, instance=produk)

        if form.is_valid():
            form.save()

            return redirect('items:detail', pk=produk.id)

    else:
        form = EditItem(instance=produk)

    return render(request, 'items/edit.html', {
        'form': form,
        'item': produk.id,
    })

@login_required
def delete(request,pk):
    produk = get_object_or_404(Produk, pk=pk, created_by=request.user)
    produk.delete()

    return redirect('core:index')