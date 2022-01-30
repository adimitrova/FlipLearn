CARDS = [
    {"user_id": 1,
        "cards": [
            {
                "collection": "Natural Languages",
                "stack": "Dutch",
                "category": "nature",
                "card": {
                    "front": "ijsvogel",
                    "back": "kingfisher"
                }
            },
            {
                "collection": "Natural Languages",
                "stack": "Dutch",
                "category": "nature",
                "card": {
                    "front": "roodboorstje",
                    "back": "robin"
                }
            },
            {
                "collection": "Natural Languages",
                "stack": "Dutch",
                "category": "nature",
                "card": {
                    "front": "hong",
                    "back": "dog"
                }
            },
            {
                "collection": "Natural Languages",
                "stack": "Dutch",
                "category": "nature",
                "card": {
                    "front": "egel",
                    "back": "hedgehog"
                }
            }
        ]
    },
    {"user_id": 2,
     "cards": [
         {
             "collection": "Programming languages",
             "stack": "Python",
             "category": "coding",
             "card": {
                 "front": "What is a class?",
                 "back": "A blueprint for creating objects"
             }
         },
         {
             "collection": "Programming languages",
             "stack": "Python",
             "category": "coding",
             "card": {
                 "front": "What is Jinja2?",
                 "back": "A templating solution allowing you to generate HTML and other documents dynamically."
             }
         },
         {
             "collection": "Programming languages",
             "stack": "Python",
             "category": "coding",
             "card": {
                 "front": "What is DDD?",
                 "back": "Domain Driven Design"
             }
         }
     ]
     }
]

if __name__ == '__main__':
    for card in CARDS:
        if card.get('user_id') == 2:
            user_cards = card.get('cards')

            side = user_cards[1]['card']['back']
            print(side)