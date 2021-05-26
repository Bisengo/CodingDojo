from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('createBook', views.createBook),
    path('books/<int:bookId>', views.showBook),
    path('addAuthorToBook/<int:bookId>', views.addAuthorToBook),
    path('authors', views.authors),
    path('authors/createAuthor', views.createAuthor),
    path('authors/<int:authorId>', views.showAuthor),
    path('addBookToAuthor/<int:authorId>', views.addBookToAuthor)
]