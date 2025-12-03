from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Blog, Author, Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

def index(request):
    """View function for home page of site."""
    num_blogs = Blog.objects.all().count()
    num_authors = Author.objects.count()

    context = {
        'num_blogs': num_blogs,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5
    class meta:
         ordering = ['-pub_date']
   

class BlogDetailView(generic.DetailView):
    model = Blog

#blogger/author
class BloggerListView(generic.ListView):
    model = Author

class BloggerDetailView(generic.DetailView):
    model = Author

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(blog=blog)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.pub_date = timezone.now()
            comment.save()
            return redirect('blog_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'catalog/blog_detail.html', {
        'blog': blog,
        'comments': comments,
        'form': form
    })