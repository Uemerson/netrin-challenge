from api.data.scraper import Scraper
from api.infra.utils.google_scraper import GoogleScraper
from api.infra.utils.logging import Logging
from api.presenters.controllers import ScraperController


def scraper_composer() -> ScraperController:
    """Composing Search Route
    :param - None
    :return - Object with Search Route
    """

    google_scraper = GoogleScraper()
    logging = Logging()
    use_case = Scraper(google_scraper, logging)
    scraper_route = ScraperController(use_case)

    return scraper_route
