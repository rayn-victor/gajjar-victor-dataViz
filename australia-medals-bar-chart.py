# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as plt
import numpy as np

countries = ('Gold', 'Silver', 'Bronze')
medals = np.arange(len(countries))
performance = (5, 3, 7)

plt.bar(medals, performance, align="center", color=('#F2D851', '#DBEBE9', '#DC7636'))
plt.xticks(medals, countries)
plt.ylabel("No. of Medals")
plt.xlabel("Countries")
plt.title("Australia Vs. Countries")
plt.show()
