import factory
from factory.django import DjangoModelFactory
from .models import Category, Post, Comment
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")
    url = factory.Faker("slug")

def getImageFile(name="test.png",size=(100,100), color="blue"):
    file_ob = BytesIO()
    image = Image.new("RGB", size, color)
    image.save(file_ob, "JPEG")
    file_ob.seek(0)
    return ContentFile(file_ob.read(), name=name)

class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence")
    url = factory.Faker("slug")
    content = factory.Faker("text")
    category = factory.SubFactory(CategoryFactory)
    published = True
    image = factory.LazyAttribute(lambda _: getImageFile())

class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    post = factory.SubFactory(PostFactory)
    name = factory.Faker("name")
    email = factory.Faker("email")
    message = factory.Faker("text")

    