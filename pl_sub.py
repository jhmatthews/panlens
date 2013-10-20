'''
    PANLENS_SUB
    
    James Matthews, University of Southampton, October 2013
    
Synopsis:
    this routine contains lensing functions for calculating lensing rates
'''

import numpy as np
from constants import *
import pl_classes as pl



def individual_rate_calculation(superblink_class, lens_id):

    '''
	individual_rate_calculation calculates the rate of lensing events for a lens given a background density

	Arguments:
		superblink_class 		class object containing superblink data
		lens_id					superblink lens id e.g. PM_14529

	Returns:
		number of close approaches within an Einstein radius
	'''
    
    i_find = np.where(lens_id, superblink_class.id)     # where the star is in the list
    
    mass = superblink_class.mass[i_find]    # mass in solar masses
    distance = superblink_class.distance[i_find]    # distance in parsecs
    healpix = superblink_class.healpix[i_find]      # healpix string
    
    theta = theta_E (mass, distance)    # calculate Einstein angle of lens
    mu = superblink_class.mu[i_find]    # proper motion in as / yr

	source_filename = "boresight..."+healpix+"/"
	sources = np.loadtxt ( source_filename, dtype="string", comments = "#" )

	n = len(sources)	 / 3600.0		# number of sources per arcsecond, averaged across healpix

	rate = 2.0 * theta_E * n * mu	# rate of lensing events

    return rate		# number of close approaches within an Einstein radius
    
    
    
    
def theta_E(mass, distance):

	'''
	theta_E calculates the angular size of an einstein ring in units of arcseconds for a given lens

	Arguments:
		mass 		mass of lens in solar masses
		distance 	distance to lens in parsecs

	Returns:
		Einstein angle in units of arcseconds
	'''
    
    constants = 4.0 * G / C**2              # constant terms in expression
      
    d_l = distance * PC                  	# distance to lens
    d_s = SOURCE_DISTANCE                   	# default 8 kpc, bulge star
	d_ls = d_s - d_l
	M = mass * MSOL							# need mass in solar masses
    
    theta = np.sqrt( constants * M * (d_ls / (d_l * d_s) ) )     # Einstein angle in radians
    
    return theta * RADS_TO_AS   				# need to return in units of arcseconds 
        
        
def get_healpix(ra_array, dec_array):
    '''uses the binary raDec2directory_pix to work out what healpix the star lies in for 2 arrays of ra and dec'''
    
    healpix_array = []
    
    for i in range(len(ra_array)):
        
        # ra and dec are provided
        ra=ra_array[i]
        dec = dec_array[i]
        
        command='./raDec2directory_pix '+str(ra)+' '+str(dec)
    
        # run the command, get output and append to an array
        os.system(command)
        output=commands.getoutput(command)
        healpix_array.append(output)
        
        
    healpix_array = np.array(healpix_array)    
    return healpix_array 
	
