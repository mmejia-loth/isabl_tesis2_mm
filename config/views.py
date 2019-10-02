from django.views import generic


class FrontendView(generic.TemplateView):

    """Frontend template."""

    template_name = "frontend.html"

    def get_context_data(self, **kwargs):
        """Get custom context data."""
        context = super(FrontendView, self).get_context_data(**kwargs)
        return context
