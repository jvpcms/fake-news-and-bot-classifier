from web_scraping.models.factory import NewsSourcesCollection, get_news_sources
from web_scraping.scrapers.scraper import (
    AosFatosScraper,
    PiauiScraper,
    G1Scraper,
    EFarsasScraper,
    BoatosScraper,
    APublicaScraper,
    APublicaTrucoScraper,
    ChecamosScraper,
    G1EduScraper,
    G1EconomiaScraper,
    G1TechScraper,
)


class ScraperCollection:
    aos_fatos_scraper: AosFatosScraper
    piaui_scraper: PiauiScraper
    g1_scraper: G1Scraper
    e_farsas_scraper: EFarsasScraper
    boatos_scraper: BoatosScraper
    a_publica_scraper: APublicaScraper
    a_publica_truco_scraper: APublicaTrucoScraper
    checamos_scraper: ChecamosScraper
    g1_edu_scraper: G1EduScraper
    g1_economia_scraper: G1EconomiaScraper
    g1_tech_scraper: G1TechScraper

    def __init__(self, news_sources_collection: NewsSourcesCollection):
        self.aos_fatos_scraper = AosFatosScraper(news_sources_collection.aos_fatos)
        self.piaui_scraper = PiauiScraper(news_sources_collection.piaui)
        self.g1_scraper = G1Scraper(news_sources_collection.g1)
        self.e_farsas_scraper = EFarsasScraper(news_sources_collection.e_farsas)
        self.boatos_scraper = BoatosScraper(news_sources_collection.boatos)
        self.a_publica_scraper = APublicaScraper(news_sources_collection.a_publica)
        self.a_publica_truco_scraper = APublicaTrucoScraper(
            news_sources_collection.a_publica_truco
        )
        self.checamos_scraper = ChecamosScraper(news_sources_collection.checamos)
        self.g1_edu_scraper = G1EduScraper(news_sources_collection.g1_edu)
        self.g1_economia_scraper = G1EconomiaScraper(
            news_sources_collection.g1_economia
        )
        self.g1_tech_scraper = G1TechScraper(news_sources_collection.g1_tech)


def get_scrapers():
    news_sources_collection = get_news_sources()
    return ScraperCollection(news_sources_collection)
