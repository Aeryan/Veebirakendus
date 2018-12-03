from django.test import TestCase, tag
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from .models import raamatud


@tag('fast', 'baseline')
class BookTestCase(TestCase):
    """BookTestCase - Test raamatu korrektse lisamise kontrolliks"""
    def setUp(self):
        raamatud.objects.create(pealkiri="Testraamat", autor="Django test",
                                kirjastus="TestCase", ilmumisaasta=2018,
                                lehekülgi=10, keel="Python")

    def testBookExists(self):
        self.assertEquals("Python", raamatud.objects.get(pealkiri="Testraamat").keel)


@tag('fast', 'baseline')
class SignupTestCase(TestCase):
    """SignupTestCase - Test kasutaja loomise kontrolliks"""
    def setUp(self):
        user = User.objects.create_user("Testija", password="testib")
        user.save()

    @tag('fast')
    def testUserIsCreated(self):
        self.assertIsInstance(authenticate(username="Testija", password="testib"), User)


@tag('fast', 'baseline')
class LoginTestCase(TestCase):
    """LoginTestCase - Test sisselogimise kontrolliks, osaliselt SignupTestCase duplikaat"""
    # SignupTestCase'i meetodi setUp duplikaat
    def setUp(self):
        user = User.objects.create_user("Testija", password="testib")
        user.save()

    def testIncorrectPasswordDoesNotAllowLogin(self):
        self.assertEqual(None, authenticate(username="Testija", password="eitesti"))

    # SignupTestCase'i meetodi testUserIsCreated duplikaat
    def testCorrectPasswordAllowsLogin(self):
        self.assertIsInstance(authenticate(username="Testija", password="testib"), User)


@tag('long')
class SeleniumTestsFirefox(StaticLiveServerTestCase):
    """Seleniumi testid Firefoxile"""

    timeout = 2

    @classmethod
    def setUpClass(cls):
        # Kasutaja test_login tarbeks
        User.objects.create_user("rauno", password="jaaska")

        super().setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        """Test esilehelt sisse logimiseks"""
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.selenium.find_element_by_id("loginModalActivator").click()
        self.selenium.find_element_by_name('login_k_nimi').send_keys("rauno")
        self.selenium.find_element_by_name('login_parool').send_keys("jaaska")

        self.selenium.find_element_by_id('loginButton').click()
        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: driver.find_element_by_tag_name('body'))

        nimekirjad = self.selenium.find_element_by_xpath("/html/body/ul/li[3]/form/a")
        self.assertEqual("Minu Bookworm nimekirjad", nimekirjad.get_attribute('title'))

    def test_search(self):
        """Test raamatute otsimiseks"""

        # Raamatud test_search tarbeks
        for i in range(15):
            raamatud.objects.create(pealkiri="Raamat"+str(i), autor="selenium", kirjastus="django",
                                    ilmumisaasta=2018, lehekülgi=10, keel="Python")

        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.selenium.find_element_by_id('id_otsing').send_keys("aamat")
        self.selenium.find_element_by_id('searchButton').click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: driver.find_element_by_tag_name('body'))
        tekst = self.selenium.find_element_by_xpath('/html/body/div[1]/div/h2').text
        self.assertEqual(tekst, "Leiti 15 tulemust")


@tag('long')
class SeleniumTestsChrome(StaticLiveServerTestCase):
    """Seleniumi testid Chrome'ile"""

    timeout = 2

    @classmethod
    def setUpClass(cls):

        # Kasutaja test_login tarbeks
        User.objects.create_user("rauno", password="jaaska")

        super().setUpClass()
        cls.selenium = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        """Test esilehelt sisse logimiseks"""
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.selenium.find_element_by_id("loginModalActivator").click()
        self.selenium.find_element_by_name('login_k_nimi').send_keys("rauno")
        self.selenium.find_element_by_name('login_parool').send_keys("jaaska")

        self.selenium.find_element_by_id('loginButton').click()
        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: driver.find_element_by_tag_name('body'))

        # Chrome ei suuda rakenduse sisselogimisjärgset ümbersuunamist hallata,
        # lehe värskendamisel töötab viimane ootuspäraselt
        self.selenium.get('%s%s' % (self.live_server_url, '/'))

        nimekirjad = self.selenium.find_element_by_xpath("/html/body/ul/li[3]/form/a")
        self.assertEqual("Minu Bookworm nimekirjad", nimekirjad.get_attribute('title'))

    def test_search(self):
        """Test raamatute otsimiseks"""

        # Raamatud test_search tarbeks
        for i in range(15):
            raamatud.objects.create(pealkiri="Raamat"+str(i), autor="selenium", kirjastus="django",
                                    ilmumisaasta=2018, lehekülgi=10, keel="Python")

        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.selenium.find_element_by_id('id_otsing').send_keys("aamat")
        self.selenium.find_element_by_id('searchButton').click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: driver.find_element_by_tag_name('body'))
        tekst = self.selenium.find_element_by_xpath('/html/body/div[1]/div/h2').text
        self.assertEqual(tekst, "Leiti 15 tulemust")