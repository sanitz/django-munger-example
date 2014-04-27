from django.test import TestCase


class MungedTextTest(TestCase):

    def test_munging(self):
        response = self.client.post('/', {'content': '1234'})
        self.assertEquals(response.context['munged'], '1324')
