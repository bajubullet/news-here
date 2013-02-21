"""Views for news-here."""

import webapp2

import view_utils


class MainPage(webapp2.RequestHandler):
    """Handle for landing page."""

    def get(self):
        """Show dummy page for now."""
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(view_utils.render('base.html', {}))
