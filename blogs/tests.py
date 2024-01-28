from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Avocats, Blog

class BlogCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_blog_post(self):
        lawyer = Avocats.objects.create(name='John Doe')

        self.client.force_authenticate(user=lawyer)

      
        blog_data = {
            'lawyer': lawyer.id,
            'title': 'Test Blog Post',
            'content': 'This is a test blog post content.',
        }

     
        response = self.client.post(reverse('create-blog'), data=blog_data, format='json')

       
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

       
        self.assertEqual(Blog.objects.count(), 1)

      
        self.assertEqual(Blog.objects.get().title, 'Test Blog Post')
