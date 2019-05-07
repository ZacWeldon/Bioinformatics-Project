#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
from scipy.spatial import distance_matrix
import random

statelist = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiant',
'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'NewHampshire', 'NewJersey',
'NewMexico', 'NewYork', 'NorthCarolina', 'NorthDakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
'RhodeIsland', 'SouthCarolina', 'SouthDakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
'Washington', 'WestVirginai', 'Wisconsion', 'Wyoming']

def randomcoordsmatrix():
    coordslist = []

    for _ in range(len(statelist)):
        subcoordslist = []
        subcoordslist.append(round(random.uniform(0,90),4))
        subcoordslist.append(round(random.uniform(0,180),4))
        coordslist.append(subcoordslist)

    states = []
    locs = []
    for state in statelist:
        states.append(state)
    for coords in coordslist:
        locs.append(coords)

    randomcoordsdataframe = pd.DataFrame(locs, columns=['ncord', 'wcord'], index = states)
    randomcoordsmatrix = pd.DataFrame(distance_matrix(randomcoordsdataframe.values, randomcoordsdataframe.values), index=randomcoordsdataframe.index, columns = randomcoordsdataframe.index)
    return randomcoordsmatrix

x = randomcoordsmatrix()
print(x)

