#!/usr/bin/env python
# coding: utf-8

# In[2]:

#import wordcloud
from wordcloud import WordCloud
#import matplotlib library.
import matplotlib.pyplot as plt

text = "sachin saurabh anurag dd vv vv vv vv vv vv vv vv vv vv vv vv vv vv vv vv vv vv ankita nisha neha surabhi suman vv lalit sachin sachin sachin sachin sachin sachin sachin sachin sachin sachin sachin sachin sachin sachin"

cloud = WordCloud(background_color="white").generate(text)

plt.imshow(cloud)
plt.axis('off')
plt.show();


#end



