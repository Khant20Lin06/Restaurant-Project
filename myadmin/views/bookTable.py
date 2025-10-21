from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
# Create your views here.

def BookATableList(request):
    bookATables = BookATable.objects.all()
    context = {
        'bookATables' : bookATables
    }
    return render(request,'BookATable/bookATableList.html',context)

def BookATableDelete(request,pk):
    bookATables = get_object_or_404(BookATable, pk=pk)

    if request.method == 'POST':
        bookATables.delete()
        return redirect('bookATableList')

    return render(request,'BookATable/bookATableList.html',{ 'bookATables' : bookATables })

def BookATableList(request):
    sort_by = request.GET.get('sort', 'newest')  # default newest

    if sort_by == 'oldest':
        bookATables = BookATable.objects.all().order_by('created_at')
    elif sort_by == 'recent':
        bookATables = BookATable.objects.all().order_by('-updated_at')
    else:  # newest
        bookATables = BookATable.objects.all().order_by('-created_at')

    context = {
        'bookATables' : bookATables,
        'sort_by': sort_by
    }
    return render(request,'BookATable/bookATableList.html',context)