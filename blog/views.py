from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
class PostList(LisView):
    context_object_name = 'posts'
    def get_queryset(self):
        queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

class PostDetail(DetailView):
    model = Post

#def post_detail(request, pk): 
 #       post = get_object_or_404(Post, pk=pk) 
  #      comments=Comment.objects.filter(post=post).order_by('created_date')
   #     if request.method == "POST":
    #        form = CommentForm(request.POST)
     #       if form.is_valid():
      #          comment = form.save(commit=False)
       #         comment.author = request.user
        #        comment.post = post
         #       comment.save()
          #      return redirect('post_detail', pk=post.pk)
        #else:
         #   form = CommentForm()

        #return render(request, 'blog/post_detail.html', {'post': post,'comments':comments,'form':form})

class PostCreate(CreateView):
    model = Post
    fields = ['title','text']
    template_name = 'blog/post_edit.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super(PostCreate,self).form_valid(form)

    def get_success_url(self):
        return reverset('post_detail',kwargs={'pk': self.object.pk})

# @login_required(login_url='login')
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#    #         post.published_date = timezone.now()
#   #          post.save()
#  #           return redirect('blog.views.post_detail', pk=post.pk)
# #    else:
# #        form = PostForm()
#  #   return render(request, 'blog/post_edit.html', {'form': form})

# @login_required(login_url='login')
# def post_edit(request, pk):
#         post = get_object_or_404(Post, pk=pk)
#         if request.method == "POST":
#             form = PostForm(request.POST, instance=post)
#             if form.is_valid():
#                 post = form.save(commit=False)
#                 post.author = request.user
#                 post.save()
#             return redirect('blog.views.post_detail', pk=post.pk)
#         else:
#             form = PostForm(instance=post)
#         return render(request, 'blog/post_edit.html', {'form': form})


# @login_required(login_url='login')
# def post_delete(request,pk):
#         post = get_object_or_404(Post, pk=pk)
#         post.delete()
#         return redirect('blog.views.post_list')