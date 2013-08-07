from django.core.exceptions import ImproperlyConfigured
from django.template import loader, Context


class TemplateMessageMixin(object):
    """ Email message mixin to provide template functionality.
        Must be inherited before EmailMessage class.
    """
    template_context = {}
    template_name = None

    def __init__(self, *args, **kwargs):
        self.template_name = kwargs.pop('template_name', self.template_name)
        self.template_context.update(kwargs.pop('template_context',
                                                self.template_context))
        self.content_subtype = self.get_content_subtype()
        kwargs['body'] = kwargs.pop('body', self.render_body())
        return super(TemplateMessageMixin, self).__init__(*args, **kwargs)

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
