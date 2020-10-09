from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm

# Create your views here.


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoseNotExist:
        raise Http404("게시글을 찾을 수 없습니다.")

    return render(request, "board_detail.html", {"board": board})


def board_write(request):
    if not request.session.get("user"):
        return redirect("/fcuser/login/")

    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get("user")
            fcuser = Fcuser.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data["title"]
            board.contents = form.cleaned_data["contents"]
            board.writer = fcuser
            board.save()

            return redirect("/board/list")
    else:
        form = BoardForm()

    return render(request, "board_write.html", {"form": form})


def board_list(request):
    # 모든 게시글을 가져오는데 가장 최신것을 가져온다.
    all_boards = Board.objects.all().order_by("-id")
    page = int(request.GET.get("p", 1))
    # Paginator 첫번째 매개변수는 게시글, 두번째 매개변수는 한페이지당 몇 개의 게시글을 넣을것인지
    paginator = Paginator(all_boards, 3)

    boards = paginator.get_page(page)
    return render(request, "board_list.html", {"boards": boards})
