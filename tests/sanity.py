from context import smart_nine

usernames='bodegadude'
scrapper_user='test'
password='test'
year=2020
scrape=False
parser=None

smart_nine.app.run_app(usernames=usernames,
                       scrapper_user=scrapper_user,
                       password=password,
                       year=year,
                       scrape=scrape,
                       parser=parser)