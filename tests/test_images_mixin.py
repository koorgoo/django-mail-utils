import os.path

from django.core.exceptions import ImproperlyConfigured
from django.core.mail import EmailMessage
from django.test import TestCase

from mail_utils.messages import ImagesMixin


class InvalidMessage(ImagesMixin, EmailMessage):
    images = ['not_found']


class Message(ImagesMixin, EmailMessage):
    images = ['logo.png']
    images_root = os.path.dirname(__file__)


class ImagesMixinTestCase(TestCase):
    def test_subtype(self):
        msg = Message()
        self.assertEqual(msg.mixed_subtype, 'related')

    def test_raise_exception_when_image_not_found(self):
        with self.assertRaises(ImproperlyConfigured):
            InvalidMessage().send()

    def test_attached_images(self):
        msg = Message()
        self.assertEqual(len(msg.attachments), 1)
