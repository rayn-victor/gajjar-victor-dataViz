# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as plt
import numpy as np

gender = ('Men', 'Women')
medals = (7, 7)

plt.bar(medals, gender, color=('red', 'blue'))
plt.xticks(medals, gender)
plt.ylabel("No. of Medals")
plt.xlabel("Gender")
plt.title("Australia Winners Men Vs. Women")
plt.show()
