=================
django-mail-utils
=================

Django mail mixins and utilities.

Contents
========
TemplateMessageMixin
--------------------
The mixin allows to create email body from a template (any text file).

| ``template_name`` - a path to a template in one of TEMPLATE_DIRs.
| ``template_context`` - a dictionary of variables passed to a template.

Both ``template_name`` and ``template_context`` can be set in inherited classes or
updated from constructor parameters.

Also you can pass the template string like the constructor's ``body`` parameter.
Then it will be used to render the real email's body.

EnvelopedMessageMixin
---------------------
The mixin allows to predefine email parameters ``subject``, ``from_email``, ``to``,
``cc`` and ``bcc``.

Parameters may be overridden via ``__init__``.


Installation
============
Install from GitHub:
::
    pip install git+git://github.com/koorgoo/django-mail-utils.git#egg=django-mail-utils
::


Examples
========

TemplateMessageMixin
--------------------
::

    from mail_utils.messages import TemplateMessageMixin
    
    class RegistrationEmailMessage(TemplateMessageMixin, EmailMessage):
        # The template is used to render the email's body.
        template_name = 'emails/registration.html'       
        template_context = {'from': 'Acme Corporation'}
::

EnvelopedMessageMixin
---------------------
::

    from mail_utils.messages import EnvelopedMessageMixin
    
    class NotificationEmailMessage(EnvelopedMessageMixin, EmailMessage):
        subject = 'Admin News'
        from_email = ADMIN_EMAIL
        to = COLLEGUES_EMAILS
        # cc = [...]
        # bcc = [...]
::
