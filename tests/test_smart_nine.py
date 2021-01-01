import os
import pytest
from context import smart_nine
os.chdir(os.getcwd()+"/tests")

@pytest.mark.parametrize ("usernames,scrapper_user,password,year,scrape,parser,output",
[

#TC01.0: Simple success
('bodegadude', 'dummy', '1234', 2020, False, None, 'Success'),
#TC01.1: Simple success for year: All
('bodegadude', 'dummy', '1234', 'All', False, None, 'Success'),

#TC02: Year must be greater than 2000
('bodegadude', 'dummy', '1234', 1999, False, None, 'Year must be greater than 2000'),
#TC03: No scraping password
('bodegadude', 'dummy', None, 2020, False, None, 'Must provide login user AND password'),
#TC04: No scraping username
('bodegadude', None, None, 2020, False, None, 'Must provide login user AND password'),
#TC05: No scraping password
('bodegadude', None, '1234', 2020, False, None, 'Must provide login user AND password'),
#TC06: No scraping password
(None, None, '1234', 2020, False, None, 'Must provide username(s) OR a file containing a list of username(s) OR pass --followings-input'),
#TC07: Incorrect String option for year
('bodegadude', 'dummy', '1234', 'Nonsense', False, None, 'Incorrect String option for (--year/-y), try: "All"'),

])

def test_smart_nine(usernames,scrapper_user,password,year,scrape,parser,output):
    result = None
    try:
        result = smart_nine.app.run_app(usernames=usernames,
                                        scrapper_user=scrapper_user,
                                        password=password,
                                        year=year,
                                        scrape=scrape,
                                        parser=parser)
    except ValueError as error_msg:
        result = error_msg

    assert(str(result) == output)

    