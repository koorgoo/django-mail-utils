from django.core.mail import EmailMessage
from mail_utils.messages import TemplateMessageMixin


class Message(TemplateMessageMixin, EmailMessage):
    pass
