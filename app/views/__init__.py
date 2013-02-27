"""Views for news-here."""

import webapp2

import models
import view_utils


class MainPage(webapp2.RequestHandler):
    """Handler for landing page."""

    def get(self):
        """Show dummy page for now."""
        self.response.write(view_utils.render('base.html', {}))


class AddNewsItem(webapp2.RequestHandler):
    """Handler for adding links."""

    def get(self):
        """Show add page."""
        news_items = models.NewsItem.all()
        self.response.write(view_utils.render('add.html', {
            'news_items': news_items,
            }))

    def post(self):
        headline = self.request.get('headline', '')
        link = self.request.get('link', '')
        if headline and link:
            news_item = models.NewsItem()
            news_item.author = 'abhishek'
            news_item.headline = headline
            news_item.link = link
            news_item.put()
            self.response.write('Data saved successfully.')
        else:
            self.response.write('Some error occured while saving data.')
