from django.core.exceptions import ImproperlyConfigured
from django.core.mail import EmailMessage
from django.test import TestCase

from mail_utils import EnvelopeMixin


class Message(EnvelopeMixin, EmailMessage):
    to = 'to'
    cc = 'cc'
    bcc = 'bcc'
    subject = 'Test'
    from_email = 'from'


class EnvelopeMixinTestCase(TestCase):
    def test_subject(self):
        self.assertEqual('Test', Message().subject)

    def test_from_email(self):
        self.assertEqual('from', Message().from_email)

    def test_to(self):
        self.assertEqual(['to'], Message().to)

    def test_cc(self):
        self.assertEqual(['cc'], Message().cc)

    def test_bcc(self):
        self.assertEqual(['bcc'], Message().bcc)

    def test_override_subject(self):
        self.assertEqual('New', Message(subject='New').subject)

    def test_override_from_email(self):
        self.assertEqual('john', Message(from_email='john').from_email)

    def test_override_to(self):
        self.assertEqual(['jane'], Message(to=['jane']).to)

    def test_override_cc(self):
        self.assertEqual(['bob'], Message(cc=['bob']).cc)

    def test_override_bcc(self):
        self.assertEqual(['kate'], Message(bcc=['kate']).bcc)

    def test_accept_string_and_override_to(self):
        self.assertEqual(['jane'], Message(to='jane').to)

    def test_accept_string_and_override_cc(self):
        self.assertEqual(['bob'], Message(cc='bob').cc)

    def test_accept_string_and_override_bcc(self):
        self.assertEqual(['kate'], Message(bcc='kate').bcc)


import warnings
from mail_utils import EnvelopedMessageMixin


class OldMessage(EnvelopedMessageMixin, EmailMessage):
    pass


class EnvelopedMessageMixinTestCase(TestCase):
    def test_warning(self):
        warnings.simplefilter('always')
        with warnings.catch_warnings(record=True) as w:
            OldMessage()
            assert len(w) == 1
