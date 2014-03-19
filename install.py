"""
Install GLPK

This script installs the binary library files for GLPK,
pre-compiled for OS X in the user's usr/local/lib directory,
and the glpsol file (the executable solver file) in the user's
usr/local/bin directory.

Author: William Usher
License: GNU Public License (see LICENSE file)
Copyright: William Usher 2014
E-mail: w.usher@ucl.ac.uk
Website: http://www.ucl.ac.uk/energy
"""

import os
import shutil
import stat
import subprocess

print "Starting Installation \n"
print "********************* \n"

# Check whether the glpk files are all present and correct
resources = [ 'libglpk.0.dylib','libglpk.a','libglpk.dylib','libglpk.la' ]
res_dir = os.getcwd()

# Copy the GLPK library files to the user's local library
dest_dir = '/usr/local/lib/'

# Check the destination directory exists
if os.path.exists(dest_dir):
    print 'Destination directory exists'
else:
    try:
        os.mkdir(dest_dir)
    except:
        print 'Could not make destination directory'

# Check if the library files already exist
for resource in resources:
    if os.path.isfile(dest_dir + resource) == True:
        print 'File ' + str(resource) + ' is already present'
    else:
        # If not, copy them to the destination directory
        shutil.copy2(res_dir + "/" + resource, dest_dir + resource)

# Copy glpsol to '/usr/local/bin'
glpsol = '/usr/local/bin/glpsol'

if os.path.exists('/usr/local/bin'):
    print 'Destination directory for glpsol exists'
else:
    try:
        os.mkdir('/usr/local/bin')
    except:
        print 'Could not make destination directory for glpsol'

# Check if glpsol already exists
if os.path.isfile('/usr/local/bin/glpsol') == True:
    print 'Glpsol already exists'
else:
    try:
        shutil.copy2(res_dir + '/glpsol', glpsol)
    except:
        print "Copying glpsol failed"

# Make glpsol executable
if os.access(glpsol, os.X_OK) == True:
    print "Glpsol is executable"
else:
    os.chmod(glpsol, stat.S_IEXEC)
    print "Made glpsol executable"

# Add glpsol to environment path
#command = 'PATH={$PATH}:/usr/local/bin'
#try:
#    subprocess.call([command])
#except:
#    print "Setting the environment variable failed"


# Copy the test files and run the test
test_files = ['model.txt', 'data.txt']
dest_dir = os.path.join(os.path.expanduser("~"), "Desktop/OSeMOSYS")
try:
    os.mkdir(dest_dir)
except:
    print "Error: Could not create OSeMOSYS folder on Desktop"
for file in test_files:
    try:
        shutil.copy2(res_dir + '/' + file, dest_dir + '/' + file)
    except:
        print "Copying file " + file + " failed"


print \
"""
********************* \n
Installation Complete \n

Further instructions:

    1. Setup your PATH variable using the command:

        PATH={$PATH}:/usr/local/bin

    2. Run OSeMOSYS using the command

        glpsol -m <modelfile> -d <datafile> -o <outputfile>
"""
