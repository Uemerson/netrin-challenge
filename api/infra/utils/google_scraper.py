import re
from typing import List

import requests

from api.data.interfaces import GoogleScraperInterface


class GoogleScraper(GoogleScraperInterface):
    def scraper(self, q: str) -> List[str]:
        url = f"https://www.google.com/search?q={q}"
        response = requests.get(url)
        pattern = r'<a href="\/url\?q=(.*?)&amp;'
        links = re.findall(pattern, response.text)
        pattern = r'<a href="\/url\?q=(.*?)&amp;'
        links = re.findall(pattern, response.text)
        return links[:5]
