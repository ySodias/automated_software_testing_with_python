from unittest import TestCase

from section_3.blog.blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        blog = Blog('Test', 'Test Author')

        self.assertEqual('Test', blog.title)
        self.assertEqual('Test Author', blog.author)
        self.assertListEqual([], blog.posts)
