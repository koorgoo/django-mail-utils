from django.core.exceptions import ImproperlyConfigured
from django.core.mail import EmailMessage
from django.test import TestCase

from mail_utils.messages import EnvelopeMixin


class Message(EnvelopeMixin, EmailMessage):
    to = 'to'
    cc = 'cc'
    bcc = 'bcc'
    subject = 'Test'
    from_email = 'from'


class EnvelopedMessageMixinTestCase(TestCase):
    def test_use_subject_class_field(self):
        self.assertEqual('Test', Message().subject)

    def test_use_from_email_class_field(self):
        self.assertEqual('from', Message().from_email)

    def test_use_to_class_field(self):
        self.assertEqual(['to'], Message().to)

    def test_use_cc_class_field(self):
        self.assertEqual(['cc'], Message().cc)

    def test_use_bcc_class_field(self):
        self.assertEqual(['bcc'], Message().bcc)

    def test_use_subject_param_instead_of_field(self):
        self.assertEqual('New', Message(subject='New').subject)

    def test_use_from_email_param_instead_of_field(self):
        self.assertEqual('john', Message(from_email='john').from_email)

    def test_use_to_param_instead_of_field(self):
        self.assertEqual(['jane'], Message(to=['jane']).to)

    def test_overridden_params(self):
        self.assertEqual(['bob'], Message(cc=['bob']).cc)

    def test_overridden_params(self):
        self.assertEqual(['kate'], Message(bcc=['kate']).bcc)
