from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Book

def index(request):
    return render(request,"myapp\index.html",{})

def view_books(request):
    if request.method == 'POST':
        # Retrieve form data
        # the parameter is the name of the textfield
        # the output value is a dictionary
        title = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')
        publication_year = request.POST.get('publication_year')

        # Filter books based on filled fields
        # retrieves all the objects (books) from the Book model/table in the database.
        books = Book.objects.all()

        # if here checks if the value is null or not
        if title:
            books = books.filter(title=title)
        if author:
            books = books.filter(author=author)
        if category:
            books = books.filter(category=category)
        if publication_year:
            books = books.filter(publication_year=publication_year)

        # Convert matched books to a list of dictionaries
        matched_books = []
        for book in books:
            matched_books.append({
                'title': book.title,
                'author': book.author,
                'category': book.category,
                'publication_year': book.publication_year
            })

        # Return JSON response
        return JsonResponse({'books': matched_books})

    return render(request,"myapp\index.html",{})



def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')
        publication_year = request.POST.get('publication_year')

        # Additional validation for all fields filled
        if title and author and category and publication_year:
            book = Book(title=title, author=author, category=category, publication_year=publication_year)
            book.save()
            return JsonResponse({'message': 'Book added successfully'})
        else:
            return JsonResponse({'error': 'All fields must be filled'}, status=400)

    return redirect("myapp\index.html")  # Redirect to the home page or any other page

def delete_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        # Additional validation for Title field filled
        if title:
            Book.objects.filter(title=title).delete()
            return JsonResponse({'message': 'Book deleted successfully'})
        else:
            return JsonResponse({'error': 'Title field must be filled'}, status=400)

    return redirect('myapp\index.html')  # Redirect to the home page or any other page

def edit_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')
        publication_year = request.POST.get('publication_year')

        # Additional validation for Title field filled
        if title:
            book = Book.objects.filter(title=title).first()
            if book:
                # Update the book fields if they are provided
                if author:
                    book.author = author
                if category:
                    book.category = category
                if publication_year:
                    book.publication_year = publication_year
                book.save()
                return JsonResponse({'message': 'Book edited successfully'})
            else:
                return JsonResponse({'error': 'Book not found'}, status=404)
        else:
            return JsonResponse({'error': 'Title field must be filled'}, status=400)

    return redirect('myapp\index.html')  # Redirect to the home page or any other page



