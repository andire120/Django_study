from django.shortcuts import render

from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    num_books = Book.objects.all().count # 책 오브젝트 모두 가져옴
    num_instances = BookInstance.objects.all().count() #책 복사본 오브젝트 가져옴

    #대출 가능한 책의 갯수 카운트
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    #작가를 모두 가져오고 갯수 카운트
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
    }

    #index.html에 변수를 render한다.
    return render(request, 'index.html', context=context)