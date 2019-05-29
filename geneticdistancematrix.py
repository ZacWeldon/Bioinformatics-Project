#Importing what we need and then reading a newick tree into dendropy
import pandas as pd
import dendropy

tree = dendropy.Tree.get(
    path =  r"nextstrain_flu_seasonal_h3n2_ha_3y_timetree.nwk",
    schema="newick")

# using dendropy to turn the newick tree into a distance matrix, and then
# into a data table
pdc = tree.phylogenetic_distance_matrix()
geneticdistancematrix = pdc.as_data_table()

# Now turn it into a csv file that we can more easily manipulate
geneticdistancematrix.write_csv('geneticdistancematrix.csv')
