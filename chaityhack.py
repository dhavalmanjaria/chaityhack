import urllib2
import re
import time
import sys


# A few warnings: This particular code is fairly untested. Meaning I don't know how it 
# will react in a real error. Theoretically it should sleep for 30 seconds and retry.
# If it doesn't work, it'll probably destroy the internet as we know it for all I know.
# Secondly, If you modify the script to go backwards, modify the WHILE statement as well.
# Third. Run both this script and yours for safety.


def isNotValid(argv):
	"""Returns False if arguments pass validation"""
	fail_flag = False
	if len(sys.argv) != 6:
		print('Usage:')
		print('python chaityhack.py <first-name> <last-name> <dd> <mm> <yy>')
		fail_flag = True
	else:
		# We check the first name arguments
		if sys.argv[1].isalpha() is False:
			fail_flag = True
		if sys.argv[2].isalpha() is False:
			fail_flag = True
		
		# We check the date arguments
		if sys.argv[3].isdigit() is False:
			fail_flag = True
		if sys.argv[4].isdigit() is False:
			fail_flag = True
		if sys.argv[5].isdigit() is False:
			fail_flag = True

	return fail_flag
	

x = 0 # This defines X as a globally accessible variable. See bottom.
def hack(s, e): # Mind you the actual function is called at the bottom.
	global x
	x = int(start)
	i_end = int(end)
	tryCount = 0 # This is a counter that counts how many times we've tried one number
	maxRetries = 4
	while x < i_end:
		# 
		# Get the url we need
		#
		url = 'http://14.140.247.111/admitcard/wpadmitcard.asp?formno=14J'
		url += str(x)
		url += '&dd=' + args[2]
		url += '&mm=' + args[3]
		url += '&yy=' + args[4]
		url += '&verification=y1Gd71'

		# Open the Webpage
		try:
			response = urllib2.urlopen(url, timeout=1)
			htmlsrc = response.read()
		except (Exception) as e:
			print(e.args)
			print('We have an problem on a webpage. Trying again...')
			time.sleep(3)
			if maxRetries > tryCount:
				tryCount += 1
				continue
			else: # Try count is beyond max
				try:
					with open("failed_numbers.txt","a") as f:
						f.write(str(x) + '\n')
				except (IOError) as e:
					print("Error writing failed_numbers.txt")
					print(e.args)
					tryCount = 0

			x += 1
			continue

		# Search for our name in the source
		if(re.search(args[0] + ' ' + args[1],htmlsrc) is None):
			print str(x)+' not found. Still searching.'
			x += 1
			continue
			
		else:
			try:
				with open("admitcard.htm","w+") as f:
					print 'WE HAVE A WINNER:'+str(x)
					f.write(htmlsrc)
					f.close()
			except (IOError) as e:
				print('Problem writing the file')
				print('Form number is: ' + str(x))
				return

		sys.exit(0)


### MAIN BLOCK
if isNotValid(sys.argv) is False:	
	first_name = sys.argv[1].upper()
	last_name = sys.argv[2].upper()
	day = sys.argv[3]
	month = sys.argv[4]
	year = sys.argv[5]
	args = (first_name, last_name, day, month, year)

else:
	sys.exit(1)


print('Please enter the range you want to operate on: ')
start = raw_input()
end = raw_input()
hack(start, end)
# This is where you start the hack by calling the function.
