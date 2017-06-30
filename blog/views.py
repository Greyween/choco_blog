from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required 

from .models import Category, Post, Comment
from .forms import PostForm, CommentForm


class PostListView(ListView):
	model = Post
	context_object_name = 'posts'
	paginate_by = 10
	template_name = 'blog/post/list.html'


class TopPostListView(ListView):
	queryset = Post.objects.order_by('-ratio').all()
	context_object_name = 'posts'
	paginate_by = 10
	template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post, 
													created__year=year, 
													created__month=month, 
													created__day=day)
	comments = post.comments.filter(status='published')
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.author = request.user
			new_comment.save()
	else:
		comment_form = CommentForm()		

	return render(request, 
								'blog/post/detail.html', 
								{'post': post, 
								 'comments': comments, 
								 'comment_form': comment_form})	

@login_required
def post_add(request):
	if request.method == 'POST':
		post_form = PostForm(data=request.POST)
		if post_form.is_valid():
			post = post_form.save(commit=False)
			post.author = request.user
			post.save()
	else:
		post_form = PostForm()
	return render(request, 'blog/post/add.html', {'form': post_form})

@login_required
def post_rate(request):
	post_id = None
	if request.method == 'GET':
		post_id = request.GET['post_id']
		action = request.GET['action']
		ratio = 0
		karma = 0
		if post_id:
			post = Post.objects.get(id=int(post_id))
			if post:
				if action == 'Like':
					ratio = post.ratio + 1
					post.ratio = ratio
					post.save()
					author_profile = post.author.profile
					karma = author_profile.karma + 1
					author_profile.karma = karma
					author_profile.save()
				elif action == 'Dislike':
					ratio = post.ratio - 1
					post.ratio = ratio
					post.save()
					author_profile = post.author.profile
					karma = author_profile.karma - 1
					author_profile.karma = karma
					author_profile.save()
	return HttpResponse(ratio)	


class CategoryListView(ListView):
	model = Category
	context_object_name = 'categories'
	paginate_by = 10
	template_name = 'blog/category/list.html'

def category_detail(request, category):
	category = get_object_or_404(Category, slug=category)
	posts = category.posts.all()
	return render(request, 
								'blog/category/detail.html', 
								{'category': category, 
								 'posts': posts})					