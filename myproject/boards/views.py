from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

def home(request):

    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards': boards})
    # boards = Board.objects.all()
    # boards_names = list()
    #
    # for board in boards:
    #     boards_names.append(board.name)
    #
    # response_html = ', '.join(boards_names)
    #
    # # return HttpResponse(response_html)
    # return render(request,'boards/home.html')
# Create your views here.
