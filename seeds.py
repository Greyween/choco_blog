import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
											'choco_app.settings')
import django

django.setup()

from blog.models import Category, Post

def populate():
	cats = ["Python", "Django", "Other frameworks"]
	for cat in cats:
		add_cat(cat)


def add_cat(name):
	cat = Category.objects.get_or_create(name=name)[0]
	cat.save()
	return cat	