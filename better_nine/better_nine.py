import os
import json
import time
from datetime import datetime
from pytz import timezone
from libnine import scrapper, graphics
from libnine import metrics_analytics as ma

class BetterNine():
    """
    Use to generate a good instagram top nine
    """

    def __init__(self, usernames, scrapper_user, password, tz, limit_date):
        self.usernames = self.handle_usernames(usernames)
        self.tz = timezone(tz)
        self.scrapper = scrapper.IGScrapper(scrapper_user, password)
        self.limit_date = limit_date
        self.metrics = ma.MetricsAnalytics()
        self.graphics = graphics.Graphics()

    def handle_usernames(self, usernames):
        """
        Forces usernames to be of type list
        """
        if isinstance(usernames, list):
            return usernames
        else:
            usernames = [usernames]
            return usernames

    def extract_jpg(self, url):
        """
        Returns jpg filename from URL
        """
        jpg = url.split("?")[0].split("/")[-1]
        return jpg

    def better_nine(self, scrape_flag = True):
        """
        Generates a good instagram top nine image
        """
        for username in self.usernames:
            if scrape_flag:
                self.scrapper.scrape(username)
            print(f"Processing {username}")
            ts_list, like_list, filename_list = self.filter_content(username, self.limit_date)
            ts_peak, like_peak, filename_peak = self.metrics.find_top_nine_peaks(ts_list, 
                                                                                 like_list,
                                                                                 filename_list)
            
            self.graphics.graph_trendline(username, ts_list, like_list, ts_peak, like_peak)
            self.graphics.generate_image_matrix(username, filename_peak)

    def filter_content(self, username, limit_date):
        """
        Filters content by limit date
        """
        user_data_path = str(os.getcwd()) +f"/{username}/"
        meta_data_path = str(os.getcwd()) +f"/{username}/{username}.json"
        config_dict = json.load(open(meta_data_path))
        limit_ts = time.mktime(datetime.strptime(limit_date, "%Y-%m-%dT%H:%M:%S").timetuple())

        ts_list = []
        like_list = []
        filename_list = []
        for post in config_dict["GraphImages"]:
            filename = user_data_path+self.extract_jpg(post["urls"][0])
            if ".mp4" in filename:
                continue

            ts = datetime.fromtimestamp(post['taken_at_timestamp'], self.tz).isoformat()
            if post['taken_at_timestamp'] <= limit_ts:
                print(f"Exiting at {ts}")
                break

            likes = post['edge_media_preview_like']['count']
            ts_list.append(ts)
            like_list.append(likes)
            filename_list.append(filename)
    
        return ts_list, like_list, filename_list
        
