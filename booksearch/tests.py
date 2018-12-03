from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import raamatud


class BookTestCase(TestCase):
    def setUp(self):
        raamatud.objects.create(pealkiri="Testraamat", autor="Django test",
                                kirjastus="TestCase", ilmumisaasta=2018,
                                lehekülgi=10, keel="Python")

    def testBookExists(self):
        self.assertEquals("Python", raamatud.objects.get(pealkiri="Testraamat").keel)


class SignupTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user("Testija", password="testib")
        user.save()

    def testUserIsCreated(self):
        self.assertIsInstance(authenticate(username="Testija", password="testib"), User)


# Partially a duplicate of SignupTestCase
class LoginTestCase(TestCase):
    # Duplicate of setUp in SignupTestCase
    def setUp(self):
        user = User.objects.create_user("Testija", password="testib")
        user.save()

    def testIncorrectPasswordDoesNotAllowLogin(self):
        self.assertEqual(None, authenticate(username="Testija", password="eitesti"))

    # Duplicate of testUserIsCreated in SignupTestCase
    def testCorrectPasswordAllowsLogin(self):
        self.assertIsInstance(authenticate(username="Testija", password="testib"), User)
