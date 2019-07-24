## Summary 

From 2007 to 2014 the number of reported crimes fell substantially in Oakland, California - a city commonly associated with violence and crime. This choropleth highlights how Oakland's crime rate evolved over this period, in each of the city's neighborhoods, for some of the most common types of crime. Through the broad 'lightening' of most neighborhoods across the city (aside from a 'darker' spike in 2012), the viewer can grasp the general decline in crime rates, while still being aware of crime's geographical distribution, and the uneven crime dynamics across neighborhoods, via the map's varied saturation.

The chart's neighborhoods are as defined in the GeoJson files kindly shared by Max Ogden [here](https://github.com/maxogden/oakland-boundaries-geojson). Crime incidents are taken from the [OpenOakland](www.openoakland.org) [database here](http://data.openoakland.org/dataset/crime-reports/resource/49bee847-a9b7-4e71-84d8-3f4cabb26cf0).

## Design

The chart incorporates a 'martini-glass' structure, with an initial author-driven narrative highlighted by changes in color saturation for each neighborhood corresponding to crime report frequency from 2007 to 2014. Once the chart animation reaches the most recent year in the data set, the user is free to construct his or her own narratives, and explore changes between various years for any given crime category. Similarly the user can compare neighborhood crime rates by hovering on any given neighborhood and seeing the number of incidents recorded for that type of crime in the currently selected year.

I chose to illustrate Oakland crime dynamics with an interactive chroropleth for its ability to preserve nuances from the dataset while still clearly conveying the primary conclusion that aggregate crime rates have significantly fallen in Oakland over the last few years.
In the choropleth, the viewer can see the substantial variation in crime frequency by geography within Oakland, as well as the persistently elevated crime rates in the busy downtown neighborhood, while simultaneously perceiving a substantial reduction in overall crime through the initial animation and toggling year selector boxes. While the aggregate reduction in crime over time could have been visible through a line graph, this would have also obscured underlying components of the trend, and restricted the viewer's ability to explore deeper insights from the dataset, including crime rates' geographical distribution.

After gathering user feedback on my initial visualization code (included in the [gist here](http://bl.ocks.org/burnssa/raw/d8e3eb30ae1a081bde39/)), I perceived that viewers might not be seeing the general reduction in crime from 2007 to 2014, or have a clear perception of the absolute rates in particular neighborhoods. To address these concerns, I added code allowing the viewer to select neighborhoods on mouseover and reveal exact crime incident counts for the neighborhood and category in a given year. Furthermore, I chose to highlight the first and last year buttons with more saturated backgrounds, as a way of 'nudging' users to toggle between these years and see the massive general drop in crime rates for the whole period. I also added references to the bottom of the chart to address specific user questions about data sources and categories. 

After a second round of feedback, I updated the annual selector buttons to show widths corresponding to the total number of incidents in the given year (for any selected category). With this additional visual cue, the broad decline in crime over the years - in every major category - is even more readily apparent to the viewer.

## Feedback

### Reviewer #1:

* What do you notice in the visualization? 
	* Crime has declined over time in all categories and most neighborhoods, but downtown Oakland. While crime was declining through 2012, there was a spike in 2012 and crime has been dropping again since. 
* What questions do you have about the data?
	* What is the data source? What is included in the "Other" category? 
* What relationships do you notice? 
	* Crime in the downtown area of Oakland is mostly driven by Assault, Court and Robbery incidents
* What do you think is the main takeaway from this visualization? 
	* Crime in Oakland has mostly declined over time.
* Is there something you don’t understand in the graphic? 
	* Which neighborhoods it refers to; it would useful to see the names of the different neighborhoods. 

### Reviewer #2

* What do you notice in the visualization?
	* Some neighborhoods are “hotspots”.  The pattern changes with time.
* What questions do you have about the data?
	* I like the visualization, but I think some questions are hard to access:
	1)  Is there a correlation between one type of crime and another.   I think tools for correlation analysis (scatterplots) would be cool. 2) In the Tufte book, the shows a table of crimes committed by people testifying in an organized crime case vs. person.  I think a similar table vs. neighborhood would be good.  I like the idea of a heatmap too, in which neighborhoods could be sorted in order of overall number of crimes and then itemized crimes represented too.  You might need to do some log transformations to show things like traffic violations and homicides on the same scale.
* What relationships do you notice?
	* Hard to see relationships between crime types (see above).  Multiple panels rather than a timecourse would be better for assessing temporal changes.
* What do you think is the main takeaway from this visualization?
	* Oakland is still coping with high crime rates.  Stats on crime per capita vs. other towns/cities should support this point, but I leave it to you.  Where is Oakland ranking now vs. e.g. Chicago?
* Is there something you don’t understand in the graphic?
	* I think a key or footnote explaining how the statistics are measured and collected (e.g. “quality of life”) would help.

### Reviewer #3

* What do you notice in the visualization?
	* Crime is concentrated in pockets
	* There is significant variance in crime rates across neighborhoods
	* East side had much less crime
* What questions do you have about the data?
	*	What does the scale represent?
	*	Can click into the neighborhoods?
	*	Which is the worst type of crime listed?
	*	What are included in the crime types?
* What relationships do you notice?
	*	Noticed higher level of criminal activity in areas close to port / west side
	* See that crime going down over time
* What do you think is the main takeaway from this visualization?
	* Chart is useful guide to the proper neighborhood for your needs, by crime rate. Need to be careful about living or investing in a neighborhood and this helps identify where crime is concentrated
* Is there something you don’t understand in the graphic?
	*	Initially didn't understand the scale
	*	Need to know what crime types are included in 'Other'


#### Post-feedback updates

After collecting reviewer feedback, I made the following changes to the visualization:
* Included ability to highlight specific neighborhoods with mouseover 
* Featured text with selected neighborhood name and neighborhood/category crime count for year (removed on year or category selection)
* Used pointer cursor for mouseover of year and category buttons indicating they are clickable
* Recentered scale legend
* Added explanation of some crime categories and data source reference in footnote
* Lightened saturation of buttons for interim years (between 2007 and 2014), guiding users to toggle between end and beginning years to see stark difference in period crime rates


##Resources and references
- http://bl.ocks.org/mbostock/4060606
- http://alignedleft.com/tutorials/d3/using-your-data
- http://synthesis.sbecker.net/articles/2012/07/09/learning-d3-part-2
- http://www.visualisingdata.com/references/
- https://github.com/PMSI-AlignAlytics/dimple/wiki
- http://stackoverflow.com/questions/25798096/how-to-add-data-labels-to-dimple-js-bar-charts
- http://stackoverflow.com/questions/18558045/dimple-js-add-data-labels-to-each-bar-of-the-bar-chart
- http://openrefine.org/
- http://datajournalismhandbook.org/1.0/en/getting_data_0.html
- http://datajournalismhandbook.org/1.0/en/getting_data_3.html
- http://bost.ocks.org/mike/join/
- https://www.dashingd3js.com/d3js-axes
- http://ben.balter.com/2013/06/26/how-to-convert-shapefiles-to-geojson-for-use-on-github/
- http://ogre.adc4gis.com/
- http://geojson.io/#map=2/20.0/0.0
- https://github.com/mbostock/d3/wiki/Arrays#-nest
- http://bl.ocks.org/phoebebright/raw/3176159/
- http://www.jeromecukier.net/blog/2012/07/16/animations-and-transitions/
- https://www.dashingd3js.com/svg-paths-and-d3js
- http://javascriptissexy.com/understand-javascripts-this-with-clarity-and-master-it/
- http://tomhicks.github.io/code/2014/08/11/some-of-this.html
- http://bost.ocks.org/mike/bubble-map/
- http://bost.ocks.org/mike/example/
- http://blog.newtonlabs.io/post/21964404793/positioning-and-scaling-maps-in-d3
- http://stackoverflow.com/questions/28141812/d3-geo-responsive-frame-given-a-geojson-object/28142611#28142611
- http://stackoverflow.com/questions/14492284/center-a-map-in-d3-given-a-geojson-object/14691788#14691788
- http://stackoverflow.com/questions/20987535/plotting-points-on-a-map-with-d3
- http://stackoverflow.com/questions/21743362/d3-js-reading-lat-long-coordinates-from-csv-into-google-map
- http://jsfiddle.net/Vjxpr/
- http://madewithenvy.com/ecosystem/articles/2015/local-maps-with-canvas-d3/
- http://www.digital-geography.com/d3-geodata-basics-a-map-overlay-can-have-many-faces/#.VndH9horKu4
- http://stackoverflow.com/questions/27543124/d3-jsmaps-svg-elements-not-appearing-when-adding-them-on-top-of-existing-svg-e
- http://stackoverflow.com/questions/1055367/how-can-i-overlay-svg-diagrams-on-google-maps
- https://developers.google.com/maps/documentation/javascript/3.exp/reference
- http://vitalflux.com/learn-r-append-rows-data-frame/
- http://gis.stackexchange.com/questions/79215/determine-if-point-is-within-an-irregular-polygon-using-python
- http://www.mhermans.net/geojson-shapely-geocoding.html
- http://igorsobreira.com/2010/09/16/difference-between-one-underline-and-two-underlines-in-python.html
- http://stackoverflow.com/questions/28297679/affective-method-of-handling-colour-on-dynamic-choropleth-legend-in-d3
- http://stackoverflow.com/questions/21323220/d3-change-elements-based-on-two-different-datasets
- http://stackoverflow.com/questions/17376626/keeping-order-in-d3-data
- http://d3js.org/
- http://stackoverflow.com/questions/20550840/how-to-get-quantize-values
- http://stackoverflow.com/questions/14525572/how-to-display-property-text-on-mouseover-in-d3-map
- http://stackoverflow.com/questions/21193305/javascript-d3-conditional-format-for-label
- http://bl.ocks.org/WilliamQLiu/292ef433e312ac69ef14
