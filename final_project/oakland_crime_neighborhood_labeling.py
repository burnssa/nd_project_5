#importing json
import json
from shapely.geometry import polygon, Point, shape

#importing csv tools
import csv
import glob
import itertools
import pandas as pd
import time

NEIGHBORHOOD_MAP = 'neighborhoods.geojson'
IN_CSV = "oakland_crimes_clean.csv"
OUT_CSV = "oakland_crimes_with_neighborhood.csv"

def add_neighborhood_labels(crime_csv, polygon_map):
# load GeoJSON file containing sectors
	with open(polygon_map, 'r') as f:
		hoods = json.load(f)

	# load crime records as dataframe
	crimes_df = pd.read_csv(crime_csv)

	def set_neighborhood_label(lng, lat):
		for feature in hoods['features']:
			polygon = shape(feature['geometry']).buffer(0)
			try:
				point = Point(float(lng),float(lat))
				if polygon.contains(point):
					print feature['properties']['NAME']
					return feature['properties']['NAME']
			except:
				return 'to_review'
	
	crimes_df['neighborhood'] = crimes_df.apply(lambda row: set_neighborhood_label(row['Lng'], row['Lat']), axis=1)
	print crimes_df
	crimes_df.to_csv(OUT_CSV)

start_time = time.clock()
add_neighborhood_labels(IN_CSV, NEIGHBORHOOD_MAP)
print time.clock() - start_time, "seconds"
