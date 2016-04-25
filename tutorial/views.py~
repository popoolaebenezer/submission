import sys
from . import scrap_wiki as s
from pyramid.view import (
    view_config,
    view_defaults
    )
from pyramid.response import Response


@view_defaults(route_name='home')
class TutorialViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'TutorialViews'

    # Retrieving the home page by default
    @view_config(renderer='home.pt')
    def home(self):
        return {'page_title': 'Hello View'}

    # Scrapping the wiki url submitted and Posting the response when the "Go" button is clisked.
    # The response page is "scraped.pt"
    @view_config(request_method='POST', renderer='scraped.pt')
    def scraping(self):
        from bs4 import BeautifulSoup
        new_name = self.request.params['new_name']
        table = s.scrap(new_name)
        
        return {'content': table}
       
        

# Resetting the web page by returning the home view when the "back" button is clicked
    @view_config(request_method='POST', request_param='form.reset',
                 renderer='home.pt')
    def back(self):
        return self.home()
