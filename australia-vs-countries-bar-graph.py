# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as plt
import numpy as np

countries = ('AUS', 'AUT', 'BEL', 'BLR', 'BUL', 'CAD', 'CHN', 'CRO', 'CZE0', 'DEN', 'ESP', 'EST', 'EUA', 'EUN', 'FIN', 'FRA', 'FRG', 'GBR', 'GDR', 'GER', 'HUN', 'ITA', 'JPN', 'KAZ', 'KOR', 'LAT', 'LIE', 'LUX', 'NED', 'NOR', 'NZL', 'POL', 'PRK', 'RUS', 'ROU', 'SLO', 'SUI', 'SVK', 'SWE', 'TCH', 'UKR', 'URS', 'USA', 'YUG', 'UZB')
medals = np.arange(len(countries))
performance = (15, 280, 13, 15, 6, 310, 82, 11, 75, 5, 2, 7, 21, 60, 434, 152, 94, 79, 162, 360, 12, 197, 63, 7, 87, 15, 9, 2, 122, 298, 1, 27, 2, 263, 2, 18, 285, 5, 433, 158, 11, 440, 653, 7, 1)

plt.bar(medals, performance, align="center")
plt.xticks(medals, countries)
plt.ylabel("No. of Medals")
plt.xlabel("Countries")
plt.title("Australia Vs. Countries")
plt.show()
