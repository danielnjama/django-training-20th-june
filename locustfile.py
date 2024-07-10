from locust import HttpUser, task, between, TaskSet
from factory import Faker
import os
import django
import logging

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangotraining.settings")
django.setup()

from blogapp.factories import PostFactory, CommentFactory

class UserBehavior(TaskSet):

    @task(3)
    def createComment(self):
        post = PostFactory()
        response = self.client.get(f"/blog/{post.url}/")

        if response.status_code == 200:
            self.client.post(
                "postcomment",
                {
                    "post":post.id,
                    "name":Faker("name").generate({}),
                    "email":Faker("email").generate({}),
                    "message":Faker("text").generate({}),
                    "url":post.url
                }
            )
    @task(2)
    def retrieveBlog(self):
        self.client.get("/blog/")

class BlogUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)