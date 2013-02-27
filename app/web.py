import webapp2

import views


app = webapp2.WSGIApplication([
    ('/', views.MainPage),
    ('/add', views.AddNewsItem),],
    debug=True)
