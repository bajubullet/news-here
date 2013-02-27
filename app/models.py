"""Models for news-here."""

from google.appengine.ext import db


class NewsItem(db.Model):
    """Model for news items."""
    author = db.StringProperty()
    headline = db.StringProperty()
    link = db.LinkProperty()
    views = db.IntegerProperty(default=0)
    timestamp = db.DateTimeProperty(auto_now_add=True)
