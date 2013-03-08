This is the simplest possible Flask app that lists all the IP 
addresses that connect to it.

It uses mkdir() to store the list of IP addresses to avoid needing a 
database at all.

You might need this if, say, you are running a tutorial on web 
development and you want to give your attendees an easy way to see a 
list of IP addresses of their peers, even if you are all behind IPv4 
NAT.

Note that you will need to be on the same LAN as your students, and 
that you will need to figure out your own LAN IP address and share it 
with your students somehow. Also note that this code listens on port 
8100 by default.

License: WTFPL.

Author: Asheesh Laroia <asheesh@asheesh.org>

To run it:

 $ virtualenv .
 $ bin/pip install -r requirements.txt
 $ bin/python app.py
