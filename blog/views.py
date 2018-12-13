from django.shortcuts import render

def index (request):
    return render(request, 'blog/homePage.html')
# Create your views here.
def post_list(request):
   return render(request, 'blog/post_list.html')
def post(request):
   return render(request, 'blog/post.html')