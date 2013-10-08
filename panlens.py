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

import numpy as no
import os




#What is your input filename of SUPERBLINK data?
lens_filename='lepine_large_feb13'



#What is your output filename for all stars within 200as?
out1='kepler_output_stars_200as_feb13'

#What is your output filename for the closest star to each lens?
#What is your search radius in arcseconds?


# get the lens data
superblink_lenses =  read_superblink (lens_filename)

# get the healpix values and place them in the class instance
superblink_lenses.healpix = get_healpix (superblink_lenses.ra, superblink_lenses.dec)


n_lenses = len (superblink_lenses.id)




def individual_rate_calculation(lens_id):
    '''This function calculates the rate of lensing events given a background density'''
    
    
def theta_E(mass, distance):
    '''calculates the angular size of an einstein ring in units of arcseconds for a given lens'''
    
    
  
  
  
    
   
    
    
