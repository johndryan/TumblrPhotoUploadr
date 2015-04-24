#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
TumblrPhotoUploadr

A simple tool for uploading all the photos in a directory to Tumblr. It posts them at the date and time they were created, and can add `#tags` to all posts if desired. 
"""

import readline, glob, os
from os.path import isdir,expanduser

def main():
	# !LET'S GET STARTED
	print ('=================================')
	print ('  __  __     __             __   ')
	print (' / / / /__  / /__  ___ ____/ /___')
	print ('/ /_/ / _ \/ / _ \/ _ `/ _  / __/')
	print ('\____/ .__/_/\___/\_,_/\_,_/_/   ')
	print ('    /_/                          ')
	print ('=================================')
	
	# !GET DIRECTORY
	num = 0
	while num <= 0:
		# !⚠️IDEA: Possible to add tab auto-completion
	    directory = raw_input('Directory to upload from: ')
	    directory = expanduser(directory)
	    # Check directory, try again if not.
	    if isdir(directory):
	    	# Check for images
	    	os.chdir(directory)
	    	# !⚠️TODO: Check for other image types
	    	num = len(glob.glob("*.JPG"))
	    	if num <= 0:
	    		print 'No images found. Try another directory.'
	    else:
	    	print 'That\'s not a directory! Please try again.'
	
	# !READY TO GO. YOU SURE?
	print ('----------------------------------')
	if raw_input('{} images to upload. Proceed? Y/N: '.format(num)).lower() != 'y':
		print ('----------------------------------')
		print 'Ok. Exiting without upload.'
		raise SystemExit
	
	# !CONNECT TO TUMBLR
	
	# !UPLOAD IMAGES
	print ('----------------------------------')
	for file in glob.glob("*.JPG"):
		print('Uploading {}...'.format(file))
		# !⚠️TODO: The uploading stuff!
	
	#blog = input('Which blog?: ')
	print ('----------------------------------')
	print ('THANKS!')
	print ('Uploaded {} files from \'{}\'.'.format(num, directory))
 
if __name__ == '__main__': main()