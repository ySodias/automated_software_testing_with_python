from section_7.starter_code.models.user import UserModel
from section_7.starter_code.tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('test', 'abcd')

            self.assertIsNone(UserModel.find_by_username('test'))
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test'))
            self.assertIsNotNone(UserModel.find_by_id(1))
            