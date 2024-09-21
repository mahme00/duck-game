from deck import DeckOfCards
deck_of_cards = DeckOfCards()
#matplotlib inline
from pathlib import Path
path = Path('.').joinpath('card_images')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
figure, axes_list = plt.subplots(nrows=4, ncols=13)

# added next two statements to increase figure size in notebook
figure.set_figwidth(16)
figure.set_figheight(9)

for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

figure.tight_layout()