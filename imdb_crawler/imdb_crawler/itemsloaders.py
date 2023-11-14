from itemloaders.processors import Compose, MapCompose, TakeFirst
from scrapy.loader import ItemLoader


class ImdbCrawlerLoader(ItemLoader):
    default_output_processor = TakeFirst()
    rank_in = MapCompose(str.strip, int)
    title_in = MapCompose(str.strip)
    stars_in = Compose(TakeFirst(), lambda x: float(x.replace(",", ".")))
    year_in = MapCompose(int)
    duration_in = MapCompose(str.strip)
