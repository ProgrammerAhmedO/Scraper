from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from Base.models import ScrapedData  # Import your model

class Command(BaseCommand):
    help = 'Scrape data from a website'

    def handle(self, *args, **kwargs):
        url = 'https://cscfitness.online/'
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.find('title').get_text()
        
        # Check if the 'description' meta tag exists before trying to access its content
        description_meta = soup.find('meta', {'name': 'description'})
        description = description_meta['content'] if description_meta else "No description available"
        
        ScrapedData.objects.create(title=title, description=description)
        
        self.stdout.write(self.style.SUCCESS('Data scraped successfully'))

#Puffin
#hello@teampuffin.com
#puffinpuffin123