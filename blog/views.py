from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
#def index (request):
#    return render(request, 'blog/homePage.html')
# Create your views here.
def post_list(request):
   #Post.objects.order_by('published_date')
   posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   return render(request, 'blog/post_list.html',{'posts':posts})
   Post.objects.get(pk=pk)
#def post(request):
#   return render(request, 'blog/post.html')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
def index (request):
    return render(request, 'blog/learn_hour.html')