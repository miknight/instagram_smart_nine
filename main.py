import json
import better_nine.better_nine as bn

config_dict = json.load(open("config.json"))

better = bn.BetterNine(usernames=config_dict["usernames"],
                       scrapper_user=config_dict["scrapper_user"],
                       password=config_dict["password"],
                       tz=config_dict["tz"],
                       limit_date=config_dict["limit_date"])

better.better_nine(scrape_flag=False)