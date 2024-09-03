from controllers.utils.ScrapperModule import Scrapper
from controllers.utils.classify_reviews import classify_reviews
from controllers.utils.summarise_reviews import summarise_reviews

scrapper = Scrapper()

async def review_brief(url: str):
    reviews =  await scrapper.scrap_reviews(url)
    classified_reviews = await classify_reviews(reviews)
    summarised_reviews = await summarise_reviews(classified_reviews)
    return summarised_reviews