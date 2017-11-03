from django.views import generic
from django.shortcuts import render_to_response, HttpResponse
from django.utils import timezone
from board.models import Post, Talk
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import View, DetailView
from django.core.exceptions import ObjectDoesNotExist

class indexView(generic.ListView):
    template_name = 'board/index.html'
    context_object_name = 'boardList'

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')

class postView(generic.DetailView):
    model = Post
    template_name = 'board/post.html'
    #ListView를 사용하기 위함
    def get_context_data(self, **kwargs):
        context = super(postView , self).get_context_data(**kwargs)
        context.update({
            'boardList': Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date'),
            'talkList' : Talk.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
        })
        return context

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')

def writing(request):
    return render_to_response('board/writing.html')

@csrf_exempt
def submit(request):
    br = Post  (post_title = request.POST['title'],
                post_text = request.POST['text'],
                pub_date = timezone.now(),
                hits = 0
                )
    br.save()
    url = '/board'
    return HttpResponseRedirect(url)

@csrf_exempt
def talkSubmit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    br = Talk  (talk_username = request.POST['username'],
                talk_text = request.POST['text'],
                pub_date = timezone.now(),
                )
    br.save()
    return HttpResponseRedirect(reverse('board:post', args=[post.id]))


def modify(request):
    pk = request.GET['post_id']
    boardData = Post.objects.get(id=pk)

    return render_to_response('board/modify.html', { 'post_id': request.GET['post_id'],
                                                     'boardData': boardData } )


@csrf_exempt
def modiSubmit(request):
    pk = request.POST['post_id']
    boardData = Post.objects.get(id=pk)
    Post.objects.filter(id=pk).update(
                                        post_title = request.POST['title'],
                                        post_text = request.POST['text'],
                                     )

    return HttpResponseRedirect(reverse('board:post', args=[boardData.id]))

def hit(request):
    pk = request.GET['post_id']

    boardData = Post.objects.get(id=pk)

    # 조회수를 늘린다.
    Post.objects.filter(id=pk).update(hits = boardData.hits + 1)

    return HttpResponseRedirect(reverse('board:post', args=[boardData.id]))
