from django import forms

from .models import Category, Post, Comment


class PostForm(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=Category.objects.all())
	class Meta:
		model = Post
		fields = ('title', 'body', 'picture', 'category')


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body', )
		widgets = {		
			'body': forms.Textarea(
				attrs={'class': 'form-control',
							 'rows': 3, 
						 	 'cols': 6})
		}		