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


Installation
============
Install from GitHub:
::
    pip install git+git://github.com/koorgoo/django-mail-utils.git#egg=django-mail-utils
::

Getting Started
===============
Import required mixins
::

    from mail_utils.messages import TemplateMessageMixin
    
    # ...
::

Use mixins to create your own emails:
::

    from django.core.mail import EmailMessage
    
    class RegistrationEmailMessage(TemplateMessageMixin, EmailMessage):
        # The template is used to render the email's body.
        template_name = 'emails/registration.html'       
::
