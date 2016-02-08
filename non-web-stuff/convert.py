import os,subprocess

def convert(k,v):
	for i,input in enumerate(v):
		output = '../assets/{}-{}.JPG'.format(k,i)
		#using imagemagick
		convert = ['convert',os.path.join(k,input), '-resize','2048',output]
		print convert[-1]
		# try:
		# 	print os.path.join(k,input),output
		# 	print subprocess.check_output(convert)
		# except subprocess.CalledProcessError, e:
		# 	print e

img_dir = 'images-raw'
places = [f for f in os.listdir(img_dir) if os.path.isdir(img_dir+'/'+f) ]
# print '{}/{}'.format(img_dir,places[0])
files = {p:os.listdir('{}/{}'.format(img_dir,p)) for p in places}

[convert(k,v)for k,v in(dict.iteritems(files))]