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




def individual_rate_calculation(superblink_class, lens_id):
    '''This function calculates the rate of lensing events given a background density'''
    
    i_find = np.where(lens_id, superblink_class.id)     # where the star is in the list
    
    mass = superblink_class.mass[i_find]    # mass in solar masses
    distance = superblink_class.distance[i_find]    # distance in parsecs
    healpix = superblink_class.healpix[i_find]      # healpix string
    
    theta = theta_E (mass, distance)    # calculate Einstein angle of lens
    mu = superblink_class.mu[i_find]    # proper motion in as/yr
    # need to finish
    
    
    
    
def theta_E(mass, distance):
    '''calculates the angular size of an einstein ring in units of arcseconds for a given lens'''
    
    constants = 4.0 * G / C**2              # constant terms in expression
    d_ls = distance - SOURCE_DISTANCE   
    d_l = distance                          # distance to lens
    d_s = SOURCE_DISTANCE                   # default 8 kpc, bulge star
    
    theta = np.sqrt( constants * mass * (d_ls / (d_l * d_s) ) )     # Einstein angle in radians
    
    return theta * RADS_TO_AS   # need to return in units of arcseconds 
    
  
  
  
    
   
    
    
