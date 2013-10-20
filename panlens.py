'''
    PANLENS
    
    James Matthews, University of Southampton, October 2013
    
Synopsis:

    panlens is a program which helps predict close passages between background stars
    in the PANSTARRS stationary catalog.
    
Usage:
    panlens.py [-r] [-f] []

Arguments:

'''

import numpy as np
import os
from constants import *
import pl_classes as cls
import pl_sub as sub

RADS_TO_AS = ((1.0 / PI) * 180.0 ) * 3600.0     #conver to degrees then multiply by 3600




#What is your input filename of SUPERBLINK data?
lens_filename='lepine_large_feb13'



#What is your output filename for all stars within 200as?
out1='kepler_output_stars_200as_feb13'

#What is your output filename for the closest star to each lens?
#What is your search radius in arcseconds?


# get the lens data and place in superblink class instance

superblink_lenses =  read_superblink (lens_filename)



# get the healpix values and place them in a superblink healpix entry

superblink_lenses.healpix = get_healpix (superblink_lenses.ra, superblink_lenses.dec)



n_lenses = len (superblink_lenses.id)   # total number of lenses




  
  
  
    
   
    
    
