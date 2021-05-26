from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def books(request):
    allbooks = Book.objects.all()
    print(allbooks)
    context = {
        'booksFromDB': allbooks
    }
    return render(request, 'booksTemplate.html', context)

def createBook(request):
    print('printing request.POST')
    print(request.POST)
    newBook = Book.objects.create(title = request.POST["titleFromHtml"], desc = request.POST["descFromHtml"])
    return redirect('/')

def showBook(request, bookId):
    bookToShow = Book.objects.get(id = bookId)
    context = {
        'book' : bookToShow,
        'allAuthors': Author.objects.all()
    }

    return render(request,'bookInfo.html', context)

def addAuthorToBook(request, bookId):
    print('*****************')
    print(request.POST)
    print('*****************')
    book = Book.objects.get(id = bookId)
    author = Author.objects.get(id = request.POST["authorId"])
    book.authors.add(author)
    return redirect(f"/books/{bookId}")

def authors(request):
    context = {
        'authorsFromDB': Author.objects.all()
    }
    return render(request, 'authorsTemplate.html', context)

def createAuthor(request):
    newAuthor = Author.objects.create(first_name = request.POST["fnFromHtml"], last_name = request.POST["lnFromHtml"], notes = request.POST["noteFromHtml"])
    return redirect('/authors')

def showAuthor(request, authorId):
    context = {
        'author': Author.objects.get(id = authorId),
        'allbooks': Book.objects.all()
        }
    return render(request, 'authorInfo.html', context)

def addBookToAuthor(request, authorId):
    author = Author.objects.get(id = authorId)
    book = Book.objects.create(title = request.POST["bookId"])
    author.booksWritten.add(book)
    return redirect(f"/authors/{authorId}")