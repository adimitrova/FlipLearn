from django import template
from cards.models import BOXES, Card

# NB! Here we will create the so called 'Inclusion tag' in order to feed data dynamically to the NAVIGATION template
#   This way we will display 5 boxes if there are 5, but if tomorrow we add 2 new boxes, it will display 7.
#   For this we use inclusion tags

register = template.Library()  # to register custom tags and logic..


@register.inclusion_tag("cards/box_links.html")
def boxes_as_links():
    # the template requires a dictionary with key "boxes" so we create that here...
    boxes = []
    for box_num in BOXES:
        card_count = Card.objects.filter(box=box_num).count()  # this is how we query,filter and aggregate in Django..
        boxes.append({
            "number": box_num,
            "card_count": card_count
        })
    return {"boxes": boxes}
