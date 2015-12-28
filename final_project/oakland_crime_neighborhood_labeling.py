#importing json
import json
from shapely.geometry import polygon, Point, shape

#importing csv tools
import csv
import glob
import itertools
import pandas as pd
import numpy as np
import time

NEIGHBORHOOD_MAP = 'neighborhoods.geojson'
IN_CSV = "oakland_crimes_clean.csv"
OUT_CSV = "oakland_crimes_with_neighborhood.csv"
GROUPED_CSV = "oakland_crimes_grouped.csv"

# load GeoJSON file containing sectors
with open(NEIGHBORHOOD_MAP, 'r') as f:
	hoods = json.load(f)

# load crime records as dataframe
crimes_df = pd.read_csv(IN_CSV)

def add_neighborhood_labels(crimes_df, polygon_map):
	
	def set_neighborhood_label(lng, lat):
		for feature in polygon_map['features']:
			polygon = shape(feature['geometry']).buffer(0)
			try:
				point = Point(float(lng),float(lat))
				if polygon.contains(point):
					print feature['properties']['NAME']
					return feature['properties']['NAME']
			except:
				return 'to_review'
	
	crimes_df['neighborhood'] = crimes_df.apply(lambda row: set_neighborhood_label(row['Lng'], row['Lat']), axis=1)
	crimes_df.to_csv(OUT_CSV)

start_time = time.clock()
add_neighborhood_labels(crimes_df, hoods)

def create_neighborhood_crimes_df(csv):
	nb_crimes_df = pd.read_csv(csv)
	nb_crimes_df['year'] = nb_crimes_df['date_format'].apply(lambda x: x[:4])
	group_columns = ['mainCat','neighborhood','year']
	grouped_crimes_df = pd.DataFrame({'count': nb_crimes_df.groupby(group_columns).size()}).reset_index()
	
	for neighborhood in set(nb_crimes_df['neighborhood']):
		for year in set(nb_crimes_df['year']):
			yearly_total = len(nb_crimes_df[(nb_crimes_df['neighborhood'] == neighborhood) & (nb_crimes_df['year'] == year)])
			grouped_crimes_df = grouped_crimes_df.append(pd.DataFrame({'mainCat': 'All Categories', 'neighborhood': [neighborhood], 'year':[year], 'count':[yearly_total]}), ignore_index=True)
	# print grouped_crimes_df[grouped_crimes_df['mainCat'] == 'All Categories']
	grouped_crimes_df.to_csv(GROUPED_CSV)

# create_neighborhood_crimes_df(OUT_CSV)

print time.clock() - start_time, "seconds"