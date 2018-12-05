# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as plt

labels = 'Gold', 'Silver', 'Bronze'
sizes = (5, 3, 7)
colors = ('#F2D851', '#DBEBE9', '#DC7636')
explode = (0, 0, 0.1)

plt.title("Amount of Each Medals in Australia")
plt.pie(sizes, explode=explode, labels=labels, colors=colors, shadow=True)
plt.show()
