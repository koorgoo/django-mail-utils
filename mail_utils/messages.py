import os
import warnings

from email.MIMEImage import MIMEImage

from django.core.exceptions import ImproperlyConfigured
from django.template import loader, Context
from django.utils import six


class TemplateMixin(object):
    """ Email message mixin to provide template functionality.
        Must be inherited before EmailMessage class.
    """
    template_context = {}
    template_name = None

    def __init__(self, *args, **kwargs):
        self.template_name = kwargs.pop('template_name', self.template_name)
        self.template_context = self.template_context.copy()
        self.template_context.update(kwargs.pop('template_context', {}))
        self.content_subtype = self.get_content_subtype()
        kwargs['body'] = kwargs.pop('body', self.render_body())
        return super(TemplateMixin, self).__init__(*args, **kwargs)

    def render_body(self):
        template_name = self.get_template_name()
        context_data = self.get_template_context()
        return loader.render_to_string(template_name, Context(context_data))

    def get_template_name(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateMessageMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_name()'")
        else:
            return self.template_name

    def get_template_context(self):
        return self.template_context

    def get_content_subtype(self):
        template = self.get_template_name()
        return 'html' if template.endswith('.html') else 'plain'


class EnvelopeMixin(object):
    """ Email message mixin to provide predefined parameters.
    """
    subject = ''
    from_email = None
    to = None
    cc = None
    bcc = None

    def __init__(self, *args, **kwargs):
        types = tuple(list(six.string_types) + [list, tuple])

        def kwargs_or_self(key):
            return kwargs.get(key, getattr(self, key, None))

        to = kwargs_or_self('to')
        if to:
            assert isinstance(to, types), '"to" argument must be a string, a list or tuple'
            if isinstance(to, six.string_types):
                to = [to]

        cc = kwargs_or_self('cc')
        if cc:
            assert isinstance(cc, types), '"cc" argument must be a string, a list or tuple'
            if isinstance(cc, six.string_types):
                cc = [cc]

        bcc = kwargs_or_self('bcc')
        if bcc:
            assert isinstance(bcc, types), '"bcc" argument must be a string, a list or tuple'
            if isinstance(bcc, six.string_types):
                bcc = [bcc]

        kwargs.update({
            'subject': kwargs_or_self('subject'),
            'from_email': kwargs_or_self('from_email'),
            'to': to,
            'cc': cc,
            'bcc': bcc,
        })

        super(EnvelopeMixin, self).__init__(*args, **kwargs)


class ImagesMixin(object):
    """ Email message mixin to allow easy image embedding.
    """
    mixed_subtype = 'related'
    images_root = os.getcwd()
    images = []

    def __init__(self, *args, **kwargs):
        super(ImagesMixin, self).__init__(*args, **kwargs)

        for image in self.images:
            filepath = os.path.join(self.images_root, image)

            if not os.path.exists(filepath):
                raise ImproperlyConfigured("ImagesMixin could not find "
                   "a file: {}".format(filepath))

            content = open(filepath, 'rb').read()
            _, filename = os.path.split(image)
            _, ext = os.path.splitext(filename)

            img = MIMEImage(content, ext[1:])
            img.add_header('Content-ID', '<%s>' % image)

            self.attach(img)


# Legacy class names.
# Should be remove in future.

class TemplateMessageMixin(TemplateMixin):
    def __init__(self, *args, **kwargs):
        warnings.warn(
            "`TemplateMessageMixin` is deprecated, use `TemplateMixin` instead.",
            PendingDeprecationWarning
        )
        TemplateMixin.__init__(self, *args, **kwargs)


class EnvelopedMessageMixin(EnvelopeMixin):
    def __init__(self, *args, **kwargs):
        warnings.warn(
            "`EnvelopedMessageMixin` is deprecated, use `EnvelopeMixin` instead.",
            PendingDeprecationWarning
        )
        EnvelopeMixin.__init__(self, *args, **kwargs)
