from unittest import TestCase

from section_3.blog.blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        blog = Blog('Test', 'Test Author')

        self.assertEqual('Test', blog.title)
        self.assertEqual('Test Author', blog.author)
        self.assertListEqual([], blog.posts)

    def test_repr(self):
        blog = Blog('Test', 'Test Author')
        expected = '<Blog(Test, Test Author, [])'

        self.assertEqual(expected, blog.__repr__())

    def tests_repr_multiple_posts(self):
        blog = Blog('Test', 'Test Author')
        blog.posts = ['Test', 'Test2']
        expected = "<Blog(Test, Test Author, ['Test', 'Test2'])"
        self.assertEqual(expected, blog.__repr__())

    def test_create_post_in_blog(self):
        blog = Blog('Test', 'Test Author')
        post = {'title': 'Test Post Title', 'content': 'Test Post Content'}
        blog.create_post(**post)

        self.assertEqual(len(blog.posts), 1)
        self.assertEqual(blog.posts[0].title, post['title'])
        self.assertEqual(blog.posts[0].content, post['content'])

    def test_json_no_post(self):
        blog = Blog('Test', 'Test Author')
        expected = {'title': 'Test', 'author': 'Test Author', 'posts': []}

        self.assertDictEqual(expected, blog.json())

    def test_json(self):
        blog = Blog('Test', 'Test Author')
        post = {'title': 'Test Post Title', 'content': 'Test Post Content'}
        blog.create_post(**post)
        expected = {'title': 'Test', 'author': 'Test Author', 'posts': [post]}

        self.assertDictEqual(expected, blog.json())
