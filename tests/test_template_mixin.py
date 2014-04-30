from django.core.exceptions import ImproperlyConfigured
from django.core.mail import EmailMessage
from django.template import TemplateDoesNotExist
from django.test import TestCase

from mail_utils.messages import TemplateMixin


class TemplatelessMessage(TemplateMixin, EmailMessage):
    template_name = None


class Message(TemplateMixin, EmailMessage):
    template_context = {'reason': 'Test', 'sender': 'Dima Kurguzov'}
    template_name = 'email.html'


class TemplateMixinTestCase(TestCase):
    def test_exception_when_template_name_is_not_set(self):
        with self.assertRaises(ImproperlyConfigured):
            TemplatelessMessage()

    def test_exception_when_template_does_not_exist(self):
        with self.assertRaises(TemplateDoesNotExist):
            Message(template_name='does_not_exist')

    def test_content_subtype_is_plain_by_default(self):
        msg = Message(template_name='email.txt')
        self.assertEqual('plain', msg.content_subtype)

    def text_content_subtype_is_html_when_template_name_ends_with_html(self):
        msg = Message(template_name='email.html')
        self.assertEqual('html', msg.content_subtype)

    def test_use_passed_template_name_parameter(self):
        msg = Message(template_name='email.txt')
        self.assertEqual('email.txt', msg.template_name)

    def test_use_passed_body_parameter_instead_of_template(self):
        self.assertEqual('New message', Message(body='New message').body)

    def test_use_template_when_body_parameter_is_not_passed(self):
        self.assertIn('We are glad', Message(template_name='email.html').body)

    def test_update_template_context_with_passed_parameter(self):
        context = {'recipient': 'John Smith', 'sender': 'Dima Kurguzov'}
        msg = Message(template_context=context)
        self.assertEqual('Test', msg.template_context['reason'])
        self.assertEqual('Dima Kurguzov', msg.template_context['sender'])
        self.assertEqual('John Smith', msg.template_context['recipient'])

    def test_use_template_context_to(self):
        context = {'recipient': 'John Smith', 'sender': 'Dima Kurguzov'}
        msg = Message(template_context=context)
        self.assertIn('John Smith', msg.body)
        self.assertIn('Dima Kurguzov', msg.body)

    def test_instance_does_not_override_original_context(self):
        original = Message.template_context
        instance = Message(template_context={'extra': 'value'})
        self.assertNotEqual(original, instance.template_context)
