import better_nine.better_nine as bn

usernames = "bodegadude"
timezone = 'America/Los_Angeles'
limit_date = "2020-01-01T00:00:00"
scrapper_user = "ulizarra"
password = "silver97"

better = bn.BetterNine(usernames=usernames,
                       scrapper_user=scrapper_user,
                       password=password,
                       tz=timezone,
                       limit_date=limit_date)

better.better_nine(scrape_flag=False)