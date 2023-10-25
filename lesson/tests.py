from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from lesson.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.lesson = Lesson.objects.create(
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

    def test_getting_lesson_list(self):
        url = reverse('lesson:lesson_list')
        response = self.client.get(
            url
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_create(self):
        url = reverse('lesson:lesson_create')
        data = {
            "name": "test",
            "description": "test",
            "video_link": "http://youtube.com/"
        }
        response = self.client.post(
            url, data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {
                'id': self.lesson.pk+1,
                'video_link': 'http://youtube.com/',
                'name': 'test',
                'description': 'test',
                'preview': None
            }

        )

    def test_lesson_update(self):
        url = reverse('lesson:lesson_update', args=[self.lesson.pk])
        data = {
            'name': 'new test',
            'description': 'new description',
        }
        response = self.client.patch(
            url, data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json()['name'],
            'new test'
        )

    def test_lesson_delete(self):
        url = reverse('lesson:lesson_destroy', args=[self.lesson.pk])
        response = self.client.delete(
            url
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
