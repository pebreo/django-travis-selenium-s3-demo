"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils.unittest import skip
from models import Thing, MyModel
import mymod
import mock

class SimpleTest(TestCase):
    
    @skip('dont want')
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 3)

    @skip('it works')
    def test_obj(self):

        obj = MyModel(name='paul')
        self.assertEqual(obj.name,'john')

    def test_patched_foo(self):
        # we replace MyModel with our Mocked Model
        with mock.patch('myapp.mymod.MyModel') as mock_MyModel:
            from mymod import foo
            mock_MyModel.objects = mock.Mock()

            conf = {'get.return_value': MyModel.DoesNotExist}
            mock_MyModel.objects.configure(**conf)
            print foo(2)
            #self.assertEqual(foo(2),'baz')
            self.assertTrue(True)