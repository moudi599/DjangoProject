from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    # View book(s)
    path('view-book/',views.view_books,name='view-book'),
    # Add a book
    path('add-book/',views.add_book, name='add-book'),
    # Delete a book
    path('delete-book/',views.delete_book, name='delete-book'),
    # Edit a book
    path('edit-book/',views.edit_book, name='edit-book'),
]




