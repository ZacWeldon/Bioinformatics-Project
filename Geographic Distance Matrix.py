import pandas as pd
from scipy.spatial import distance_matrix

""" Coordinates of US states. The first number is degrees North, the second number is degrees West"""
statecoords = { 'Alabama' : [33.3182, 86.9023],
               'Alaska' : [64.2008, 149.4937],
               'Arizona' : [34.0489, 111.0937],
               'Arkansas' : [35.2010, 91.8318],
               'California' : [36.7783, 119.4179],
               'Colorado' : [39.5501, 105.7821],
               'Connecticut' : [41.6032, 73.0877],
               'Delaware' : [38.9108, 75.5277],
               'Florida' : [27.6648, 81.5158],
               'Georgia' : [32.1656, 82.9001],
               'Hawaii' : [19.8968, 155.5828],
               'Idaho' : [44.0682, 114.7420],
               'Illinois' : [40.6331, 89.3985],
               'Indiana' : [40.2672, 86.1349],
               'Iowa' : [41.8780, 93.0977],
               'Kansas' : [39.0119, 98.4842],
               'Kentucky' : [37.8393, 84.2700],
               'Louisiana' : [30.9843, 91.9623],
               'Maine' : [45.2538, 69.4455],
               'Maryland' : [39.0458, 76.6413],
               'Massachusetts' : [42.4072, 71.3824],
               'Michigan' : [44.3148, 85.6024],
               'Minnesota' : [46.7296, 94.6859],
               'Mississippi' : [32.3547, 89.3985],
               'Missouri' : [37.9643, 91.8318],
               'Montana' : [46.8797, 110.3626 ],
               'Nebraska' : [41.4925, 99.9018],
               'Nevada' : [38.8026, 116.4194],
               'New Hampshire' : [43.1939, 71.5724],
               'New Jersey' : [40.0583, 74.4057],
               'New Mexico' : [34.5199, 105.8701],
               'New York' : [43.2994, 74.2179],
               'North Carolina' : [35.7596, 79.0193],
               'North Dakota' : [47.5515, 101.0020],
               'Ohio' : [40.4173, 82.9071],
               'Oklahoma' : [35.0078, 97.0929],
               'Oregon' : [43.8041, 120.5542],
               'Pennsylvania' : [41.2033, 77.1945],
               'Rhode Island' : [41.5801, 71.4774],
               'South Carolina' : [33.8361, 81.1637],
               'South Dakota' : [43.9695, 99.9018],
               'Tennessee' : [35.5175, 86.5804],
               'Texas' : [31.9686, 99.9018],
               'Utah' : [39.3210, 111.0937],
               'Vermont' : [44.5588, 72.5778],
               'Virginia' : [37.4316, 78.6569],
               'Washington' : [47.7511, 120.7401],
               'West Virginia' : [38.5976, 80.4549],
               'Wisconsin' : [43.7844, 88.7879],
               'Wyoming' : [43.0760, 107.2903]
    }

areas = []
locs = []

for coords in statecoords.values():
    areas.append(coords)

for state in statecoords.keys():
    locs.append(state)

statesdf = pd.DataFrame(areas, columns=['ncord', 'wcord'], index=locs)
geomatrix = pd.DataFrame(distance_matrix(statesdf.values, statesdf.values), index=statesdf.index, columns=statesdf.index)

datadf = pd.read_csv('nextstrain_flu_seasonal_h1n1pdm_ha_3y_metadata.tsv', sep = '\t')
