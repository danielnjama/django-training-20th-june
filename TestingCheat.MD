# PYTHON DJANGO TESTING CHEAT-CHEAT 💭💭

### 🖇️ We Test Behaviours, Not Implementation

## 📌 Introduction To Testing
### 🎗️ Need for Testing:
    ✔️ Quality Assurance:  Ensure the application works as expecte
    ✔️ Bug Identification:  Detect and fix bugs early in the development cycle
    ✔️ Code Maintenance:  Facilitate Code refactoring enhancements with confident
    ✔️ Documentation:  Tests Servers as additional Documentation for the code Base
    ✔️ Automated Verification:  Reduce manual efforts with automated test cases.

### 🎖️ Best Practices:
    ✔️ Write Testable Code:  Ensure your code is modular and loosely coupled to make
    it easier to test.
    ✅ Use  Test-Driven Development (TDD):  Write tests before writing the actual code.
    ✔️ Keep It Simple:  Write Simple and readable test cases.
    ✅ Test Coverage: Aim for high test coverage but focus on **Critical & Complex parts**.
    ✔️ Use Fixtures: Use setup and teardown methods to prepare the test Environment.
    ✔️ Mock External Services: Use mocking for external services and APIs to avoid dependencies
    ✔️ Continuous Integration(CI): Integrate tests with CI tools and run tests automatically on code changes.

### Automated Testing Encompasses: 
1. Unit Testing
2. Performance Testing
3. Profiling & Optimization

## 1. Unit Testing.
✅"pytest" is a testing framework for Python that makes it easy to write simple and scalable test cases. It is particulary popular for its simplicity and ease of use.

### ☣️ ☣️ Installation
~~~
conda install pytest pytest-django
pip install pytest pytest-django
~~~



### 🔌🔌 Configuration
- Create a "pytest.ini" file in the root directory of your Django project:
~~~
[pytest]
DJANGO_SETTINGS_MODULE = your-project-name.settings
python_files = tests.py test_*.py *_tests.py
~~~
✅ Ensure your Django settings module is set correctly.


### 🔋🔋Writing Tests:
✅ Create a test File (i.e "test_models.py") in your app's "tests" directory.

Example:
~~~
import pytest
from myapp.models import MyModel

@pytest.mark.django_db
def test_my_model_creation():
    instance = MyModel.objects.create(name="Test")
    assert instance.name == "Test"
~~~

### 🚀🚀 Running Tests:
~~~
pytest
~~~


## 2. Performance Testing.
✅ "Locust" is an open-source load testing tool that allows you to define user behavior using Python Code. Its used to test the performance of web applications.

### ☣️ ☣️  Installation:
~~~
conda install locust
pip install locust
~~~

### 🔌🔌 Configuration:
✅  Create a "locustfile.py" in your project directory.
✅  Define User behavior and tasks

### 📊📊 Example:
~~~
from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def about(self):
        self.client.get("/about/")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(5, 15)
~~~

### 🚀🚀 Running Tests:
~~~
locust -f locustfile.py
~~~
✅ Open Browser and go to "http://localhost:8089" to start the test.

## 3. Profiling and Optimization
✅  "Silk" is a Django App for profiling and inspecting SQL queries. It helps in identifying performance bottlenecks and optimizing your Django Application.

### ☣️ ☣️  Installation:
~~~
pip install django-silk

conda install django-silk
~~~

### 🔌🔌 Configuration:
✅ Add "silk" to your "INSTALLED_APPS" in "settings.py":
~~~
INSTALLED_APPS = [
    ...
    'silk',
]
~~~
✅ Add "SilkMiddlware" to "MIDDLEWARE":
~~~
MIDDLEWARE = [
    ...
    'silk.middleware.SilkyMiddleware',
]
~~~
✅ Configure the url pattern for silk:
~~~
urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
~~~

✅ Run Migrations
~~~ 
python manage.py migrate silk
~~~

### 📊📊 Usage:
- Start Django Server.
- Go to "/silk/" to access the Silk Profiling Interface.


## 🏴‍☠️🏴‍☠️ Summary
- By using pytest for unit testing, Locust for performance testing, and Silk for profiling and optimization, you can ensure your Django application is well-tested, performs efficiently under load, and is optimized for performance.