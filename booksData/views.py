from django.shortcuts import render, redirect
from booksData.forms import BooksForm
from booksData.models import Library

# Creating views here.

#book function which will be run on a post request and if it'll be valid it'll open show.html file and if to add new
#record of book it'll open index.html
def book(request):
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = BooksForm()
    return render(request,'index.html',{'form':form})

#function to show number of enteries in our database from our online application
def show(request):
    books = Library.objects.all()
    return render(request,"show.html",{'books':books})

#function to edit an entry in our database from our online application
def edit(request, id):
    #getting book id that is given by user
    book = Library.objects.get(id=id)
    return render(request,'edit.html', {'book':book})

#function to change/update an entry in our database from our online application
def update(request, id):
    #getting book id that is given by user
    books = Library.objects.get(id=id)
    form = BooksForm(request.POST, instance = books)

    #on correct enteries it'll update the enteries & on incorrect it'll not respond
    if form.is_valid():
        # saving an updated entry
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'book': book})

#function to delete an entry in our database from our online application
def destroy(request, id):
    #getting book id that is given by user
    book = Library.objects.get(id=id)
    #deleting an entry
    book.delete()
    return redirect("/show")
