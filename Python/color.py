#
#
# This file by @ffrandias @ him if you have a question.
# you're free to do as you like with this
#
#
# Content heavily influenced by Nathan Yau @ flowingdata.com
# Specifically his tutorial:
# http://flowingdata.com/2009/11/12/how-to-make-a-us-county-thematic-map-using-free-tools/
#
#
# Great place to keep going:
# http://www.infochimps.com/tags/fips
# http://quickfacts.census.gov/qfd/download_data.html
#
#
########################## Get on with it ###############################


# if you do not have Beatiful soup already installed you can install it by
# using "pip install beautifulsoup4" or "easy_install beautifulsoup4" in
# terminal. You may need to use sudo.

# To run just type python color.py in terminal when in the same directory
# as color.py.


import csv
from bs4 import BeautifulSoup

#name your map
newfileName = "newmap"

# Map colors
colors = ["#f9e682", "#ffe200", "#ffd400", "#fdb813", "#f89c1b", "#f5821f"]  # less Saturated -> more saturation

# County style
path_style = 'font-size:12px; stroke:#FFFFFF; stroke-opacity:1; stroke-width:0.1; stroke-miterlimit:4; stroke-dasharray:none; stroke-linecap:butt; marker-start:none; stroke-linejoin:bevel; fill-rule:nonzero; fill:'  # Fill is left open so we can easily just append to it.


# Read in unemployment rates
unemployment = {}
min_value = 100
max_value = 0

# SAMPLE CSV DATA (yeah, Boston)
# unique county id, 	state number,   county number,  county (plane text),    state, 	year,   total population,   employed, 	unemployed,	percent unemployed
# CN250250,				25,				025,			"Suffolk County",    	"MA",  	2009,   "361,350", 		    "327,847",	"33,503", 	9.3

reader = csv.reader(open('../commonFiles/unemployment09.csv'), delimiter=",")
for row in reader:
    try:
        full_fips = row[1] + row[2]	 # creates the FIPS number by conact Suffolk is 25025
        rate = float(row[8].strip())  # grabs out unemployment rate and converts it to a float
        unemployment[full_fips] = rate  # sets the unemployment index of the FIPS number to the unemployment rate
    except:
        pass


svg = open('../commonFiles/unemployment.svg', 'r').read()  # Load the SVG map
soup = BeautifulSoup(svg)  # Load into Beautiful Soup
paths = soup.findAll('path')  # Find counties
notCounties = ["State_Lines", "separator"]  # Things that aren't counties

# Color the counties based on unemployment rate

def colors
for path in paths:
    if path['id'] not in notCounties:
        # pass
        try:
            rate = unemployment[path['id']]  # Match the SVG FIPS number to the hashtable we made earlier where we made FIPS numbers & set the unemployment rate.
        except:
            continue

        if rate > 15:
            color = colors[5]  # Remember those colors we defined up at the top?
        elif rate > 12:
            color = colors[4]
        elif rate > 9:
            color = colors[3]
        elif rate > 6:
            color = colors[2]
        elif rate > 3:
            color = colors[1]
        else:
            color = colors[0]

        path['style'] = path_style + color + ";"  # Actually write over the path style attribute here


#Lets shove this into a file.
newmap = str(soup.prettify())
file = open(newfileName + '.svg', 'w')
file.write(newmap)
file.close
