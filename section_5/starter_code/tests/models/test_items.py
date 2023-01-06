from unittest import TestCase
from unittest.mock import patch
from section_5.starter_code.models.item import ItemModel


class ItemModelTest(TestCase):
    def setUp(self):
        self.item_model = ItemModel(name='Test', price=1.1)

    def test_create_item(self):
        item_model = ItemModel(name='Test', price=1.1)
        self.assertEqual(item_model.name, 'Test',
                         'The name of the item after creation does not equal the constructor argument')
        self.assertEqual(item_model.price, 1.1,
                         'The name of the item after creation does not equal the constructor argument') #Mensagem de erro

    def test_json(self):
        expected = {'name': 'Test', 'price': 1.1}
        self.assertDictEqual(expected, self.item_model.json())


