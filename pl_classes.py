'''
    PANLENS_SUB
    
    James Matthews, University of Southampton, October 2013
    
Synopsis:
    this routine contains classes whichs store properties for each star
    as well as some useful functions for 
'''

import numpy as np



class superblink_class:
	'''This is a class for superblink data, our lens catalog'''	
	def __init__(self, id1, ra1, dec1, pm1, pm_ra1, pm_dec1, mags1, mass1, dist1, healpix):
		self.id = id1
		self.ra = ra1
		self.dec = dec1
		self.pm = pm1 
		self.pm_ra = pm_ra1
		self.pm_dec = pm_dec1
        self.mags = mags1
        self.mass = mass1
        self.dist = dist1
        self.healpix = healpix1





def read_superblink ( filename ) :
    '''creates an array of lens data from an input superblink filename'''
    
    # initialise the class
	superblink = superblink_class ([],[],[],[],[],[], [], [], [], [], [], [])
    
    # now put data into numpy array
    lens_data = np.loadtxt(filename, unpack=True, dtype = 'string')
    
	superblink.id = lens_data[0]
	superblink.ra = lens_data[1]
	superblink.dec = lens_data[2]
	superblink.pm = lens_data[3] 
	superblink.pm_ra = lens_data[4]
	superblink.pm_dec = lens_data[5]
    superblink.mags = lens_data[6:14]
    superblink.mass = lens_data[16]
    superblink.dist = lens_data[14]
    
    return superblink
    
    
    
    
class panstarrs:
    '''Class for panstarrs stationary catalog data'''
    def __init__(self, fre, wave, emi, cen, dis, win, sca, hit, spe):
        self.id = fre
        self.ra = wave
        self.dec = emi
        self.mu = cen
        self.disk = dis
        self.wind = win
        self.scattered = sca
        self.hitSurf = hit
        self.spec = spe
        
        
	
