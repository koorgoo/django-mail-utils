=================
django-mail-utils
=================

Django mail mixins and utilities.

Contents
========
TemplateMixin
-------------
The mixin allows to create email body from a template (any text file).

| ``template_name`` - a path to a template in one of TEMPLATE_DIRs.
| ``template_context`` - a dictionary of variables passed to a template.

Both ``template_name`` and ``template_context`` can be set in inherited classes or
updated from constructor parameters.

Also you can pass the template string like the constructor's ``body`` parameter.
Then it will be used to render the real email's body.

EnvelopeMixin
-------------
The mixin allows to predefine email parameters in class fields.

| ``subject`` - string
| ``from_email`` - string
| ``to`` - string or list/tuple
| ``cc`` - string or list/tuple
| ``bcc`` - string or list/tuple

Parameters may be overridden during initialization.

ImagesMixin
-----------
The mixin allows to embed images into email via ``<img src="cid:<your image>">`` in HTML.
To enable this functionality set ``images`` and ``images_root`` class fields.

| ``images_root`` - a root path to resolve image paths (e.g. ``os.path.dirname(__file__)`` or ``os.getcwd()``)
| ``images`` - a list of paths to images (e.g. ``['logo.png']`` or ``['email_images/logo.png']``)

Installation
============
::

    pip install django-mail-utils
::


Examples
========

TemplateMixin
--------------------
::

    from mail_utils import TemplateMixin

    
    class RegistrationEmail(TemplateMixin, EmailMessage):
        template_name = 'emails/registration.html'       
        template_context = {'from': 'Acme Corporation'}
::

EnvelopeMixin
---------------------
::

    from mail_utils import EnvelopeMixin
    
    class NotificationEmail(EnvelopeMixin, EmailMessage):
        subject = 'Admin News'
        from_email = ADMIN_EMAIL
        to = COLLEGUES_EMAILS
        cc = CC_EMAILS
        bcc = BCC_EMAILS


    # Override `to` 
    NotificationEmail(to='me@example.com').send()
::

ImagesMixin
-----------
::

    from mail_utils import TemplateMixin, ImagesMixin

    class CoolEmail(ImagesMixin, TemplateMixin, EmailMessage):
        template_name = 'email.html'
        images_root = os.path.dirname(__file__)
        images = ['logo.png', 'phone_icon.png']
::

In HTML use ``<img src="cid:<path from images>">`` to embed an image.

::
       
    <img src="cid:logo.png" /> Company
       
    <img src="cid:phone_icon.png"> Call us
::
