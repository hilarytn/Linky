#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import Column, String, Text, LargeBinary
from models.base_model import BaseModel, Base
from models.engine import storage


class Blog(BaseModel, Base):
    __tablename__ = 'blog'

    article_title = Column(Text(1200), nullable=False)
    article_heading = Column(Text(1200), nullable=False)
    article_content = Column(Text(10000), nullable=False)
    #article_image_1= Column(LargeBinary)
    #article_image_2= Column(LargeBinary)

    def __init__(self, article_title=None, article_heading=None,
                  article_content=None): #article_image_1=None, #article_image_2=None):
        #self.id = str(uuid4())
        super().__init__()
        self.article_title = article_title
        self.article_heading = article_heading
        self.article_content = article_content
        #self.article_image_1 = article_image_1
        #self.article_image_2 = article_image_2

title = "My favorite food"
head = "A short Poem about my favourite food"
content="""Oh, my favorite food, a delightful creation,
A symphony of flavors, a heavenly sensation.
It's the dish that makes my taste buds dance,
A culinary masterpiece, a true romance.

From the first bite, my senses come alive,
A burst of pleasure, my cravings strive.
The aroma wafts, tempting and divine,
Each mouthful, pure bliss, a taste so fine.

Its texture delights, a perfect harmony,
A medley of ingredients, a culinary journey.
Whether sweet or savory, it never disappoints,
My favorite food, a feast that never fades nor annoys.

I savor every bite, indulging in its charms,
A culinary adventure that forever warms.
Oh, my favorite food, a true delight,
Forever cherished, morning, noon, and night."""

new_article = Blog(article_title=title, article_heading=head,article_content=content)
storage.new(new_article)
storage.save()
print("Saved Successfully!")
print(new_article.article_title)
print(new_article.article_heading)
print(new_article.article_content)




