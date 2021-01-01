import os
from context import smart_nine

usernames = 'bodegadude'
scrapper_user='dummy'
password='1234'
year=1999
scrape=False
parser=None
os.chdir(os.getcwd()+"/tests")



def smart_nine_wrapper(usernames=usernames,
                       scrapper_user=scrapper_user,
                       password=password,
                       year=year,
                       scrape=scrape,
                       parser=parser):
    try:
        smart_nine.app.run_app(usernames=usernames,
                                scrapper_user=scrapper_user,
                                password=password,
                                year=year,
                                scrape=scrape,
                                parser=parser)
    except ValueError as result:
        print(result)

    