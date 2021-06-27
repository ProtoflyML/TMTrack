from scrappers.youtube_results_scrapper import YoutubeResultsScrapper
from scrappers.wiki_hot_100_scrapper import WikiHot100Scrapper
from config import OUTPUT_DIR, START_YEAR, END_YEAR
import pandas as pd
import os.path

yt_link_scrapper = YoutubeResultsScrapper()
wiki_scrapper = WikiHot100Scrapper(START_YEAR, END_YEAR)

song_data = wiki_scrapper.scrape_all_tables()
song_df = pd.DataFrame(song_data, columns=['year', 'artist', 'song'])
song_df = song_df.set_index('year')  

song_df['youtube_search_url'] = song_df.apply(yt_link_scrapper.get_first_result, axis=1)
song_df.to_csv(os.path.join(OUTPUT_DIR, 'billboard_top_100.csv'))
