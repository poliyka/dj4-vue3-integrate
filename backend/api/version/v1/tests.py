from base.models import Profile
from django.contrib.auth.models import User
from django.test import Client, TestCase, tag
from django.urls import reverse


@tag("api")
class UserDataTest(TestCase):
    def setUp(self) -> None:
        # create user
        username = "test_user"
        password = "test_password"
        email = "test_email@test.com"
        self.user = User.objects.create_user(username, email, password)
        self.user.save()
        profile = Profile(user=self.user)
        profile.save()

        # login
        self.c = Client()
        # self.c.login(username=username, password=password)

        # jwt login
        response = self.c.post(
            reverse("api:rest_login"),
            data={"username": username, "password": password},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json().get("access_token"))
        self.token = response.json().get("access_token")
        self.header = {"Authentication": f"Bearer {self.token}"}

    @tag("user_data")
    def test_get_user_data(self) -> None:
        """Test GET response"""
        response = self.c.get(reverse("api:user_data"), **self.header)

        # test status
        self.assertEqual(response.status_code, 200)

        # test data
        data = response.json()
        self.assertEqual(data["username"], "test_user")
        self.assertEqual(data["email"], "test_email@test.com")
