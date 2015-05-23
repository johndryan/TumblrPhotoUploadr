#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
TumblrPhotoUploadr

A simple tool for uploading all the photos in a directory to Tumblr. It posts them at the date and time they were created, and can add `#tags` to all posts if desired. 
"""

import readline, glob, os, tumblr, pytumblr, yaml, time
from os.path import isdir,expanduser,getctime
from utils.getcreationdate import get_osx_creation_time

# !SET VARIABLES
FILETYPES = ['*.jpg','*.jpeg','*.JPG','*.JPEG','*.png','*.PNG','*.gif','*.GIF']


def main():
	# !LET'S GET STARTED
	print ('=================================')
	print ('  __  __     __             __   ')
	print (' / / / /__  / /__  ___ ____/ /___')
	print ('/ /_/ / _ \/ / _ \/ _ `/ _  / __/')
	print ('\____/ .__/_/\___/\_,_/\_,_/_/   ')
	print ('    /_/                          ')
	print ('=================================')
	
	# !⚠️TODO: Move Tumblr API up front, so fail exits
	
	# !GET DIRECTORY
	num = 0
	files = []
	while num <= 0:
		# !⚠️IDEA: Possible to add tab auto-completion
	    directory = raw_input('Directory to upload from: ')
	    directory = expanduser(directory)
	    # Check directory, try again if not.
	    if isdir(directory):
	    	# Check for images
	    	os.chdir(directory)
	    	# !⚠️TODO: Check for other image types
	    	for types in FILETYPES:
	    		files += glob.glob(types)
	    	num = len(files)
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
	apikeys = yaml.load(open(expanduser('~/.tumblr')))
	client = pytumblr.TumblrRestClient(
	    apikeys['consumer_key'],
	    apikeys['consumer_secret'],
	    apikeys['oauth_token'],
	    apikeys['oauth_token_secret'],
	)

	# !⚠️TODO: Add try/fail for connection
	json = client.info()
	username = json['user']['name']
	blogs = json['user']['blogs']
	
	# !SELECT BLOG
	print ('----------------------------------')
	print 'Choose a blog to post to:'
	for index, blog in enumerate(blogs):
		print '[{}] {}'.format(index, blog['title'])
	# !⚠️TODO: Try/fail inputs gracefully
	blogId = int(raw_input('Enter number: '))
	blog = blogs[blogId]
	
	# !CREATE DIR FOR UPLOADED IMAGES
	uploadedfolder = os.path.join(directory, '_uploaded')
	if not os.path.exists(uploadedfolder):
		os.makedirs(uploadedfolder)
    
	# !UPLOAD IMAGES
	print ('----------------------------------')
	print ('UPLOADING to {}'.format(blog['title']))
	for index, file in enumerate(files):
		# !⚠️TODO: Uploading error handling
		print('Uploading {}...'.format(file))
		client.create_photo(
			blog['name'],
			state="published",
			data=os.path.join(directory, file),
			date=time.ctime(os.path.getmtime(file)),
			slug=file
		)
		# Move to subfolder
		os.rename(os.path.join(directory, file), os.path.join(uploadedfolder, file))
		# !⚠️TODO: Add delay between uploads?
	
	#blog = input('Which blog?: ')
	print ('----------------------------------')
	print ('SUCCESS!')
	print ('Uploaded {} files from \'{}\' to {}.'.format(num, directory, blog['title']))
 
if __name__ == '__main__': main()