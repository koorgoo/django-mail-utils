from django.test import TestCase
from .messages import Message


class MessageTestCase(TestCase):
    def setUp(self):
        self.msg = Message()

    def test_content_subtype_is_html_by_default(self):
        self.assertEqual('html', self.msg.content_subtype)
