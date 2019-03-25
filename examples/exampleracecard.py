import logging
import os

import betfairlightweight


# setup logging
logging.basicConfig(level=logging.INFO)  # change to DEBUG to see log all updates

# create trading instance
username = os.environ.get('username')
trading = betfairlightweight.APIClient(username)
trading.login()

# update
market_id = '1.133559518'

# race card login
trading.race_card.login()

# race card request (provide list / returns list)
race_cards = trading.race_card.get_race_card(
    market_ids=[market_id]
)


print(race_cards)
for race_card in race_cards:
    print(
        race_card,
        race_card.prize,
        race_card.timeform_123_text,
    )  # view resources or debug to see all values available

    for runner in race_card.runners:
        print(
            runner.name,
            runner.comment,
        )
