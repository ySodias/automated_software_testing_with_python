from unittest import TestCase
from unittest.mock import patch

from section_3.blog import app
from section_3.blog.blog import Blog


class AppTest(TestCase):
    def setUp(self) -> None:
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

    def test_menu_prints_promp(self):
        with patch('builtins.input', return_value='q') as mocked_print:
            app.menu()
            mocked_print.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('section_3.blog.app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called_with()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- <Blog(Test, Test Author, [])')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blogs(self):
        with patch('builtins.input', return_value='Test'):
            with patch('section_3.blog.app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(app.blogs['Test'])
