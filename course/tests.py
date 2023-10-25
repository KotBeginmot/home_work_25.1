from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from course.models import Course, Subscription
from lesson.models import Lesson
from users.models import User


class CourseTestCase(APITestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='name1',
            description='description1'
        )
        self.client = APIClient()
        self.user = User.objects.create(email="admin@test.com", password='12345')
        self.user.is_active = True
        self.user.is_staff = True
        self.user.is_superuser = True
        self.client.login(email="admin@test.com", password='12345')
        self.client.force_authenticate(user=self.user)

    def test_getting_course_list(self):
        url = 'http://127.0.0.1:8000/api/course/'
        response = self.client.get(
            url
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_course_create(self):
        url = 'http://127.0.0.1:8000/api/course/'
        data = {
            "name": "new test",
            "description": "new test",
        }
        response = self.client.post(
            url, data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_course_update(self):
        url = f'http://127.0.0.1:8000/api/course/{self.course.pk}/'

        data = {
            'name': 'new name',
            'description': 'new description',
        }
        response = self.client.patch(
            url, data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_course_detail(self):
        url = f'http://127.0.0.1:8000/api/course/{self.course.pk}/'

        data = {
            'name': 'new name',
            'description': 'new description',
        }
        response = self.client.get(
            url, data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_course_delete(self):
        url = f'http://127.0.0.1:8000/api/course/{self.course.pk}/'
        response = self.client.delete(
            url
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email="admin@test.com", password='12345')
        self.user.is_active = True
        self.user.is_staff = True
        self.user.is_superuser = True
        self.client.login(email="admin@test.com", password='12345')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='test', description='test')
        self.subscription = Subscription.objects.create(user=self.user, course=self.course, subscription=True)

    def test_subscription_create(self):
        url = 'http://127.0.0.1:8000/api/subscription/'
        user = User.objects.create(email="test@test.com", password='12345')
        course = Course.objects.create(name='fortest', description='fortest')

        data = {
            "user": user.id,
            "course": course.id,
        }

        response = self.client.post(
            url, data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_subscription_delete(self):
        url = f'http://127.0.0.1:8000/api/subscription/{self.subscription.pk}/'
        response = self.client.delete(
            url
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
