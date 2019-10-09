#! python

#https://docs.python.org/3.3/library/sys.html

import sys
import platform
#sys.stdout.write("Windows information: %s\n" % (sys.getwindowsversion(),))
#do if statement to translate abbreviation to a the actual system?
#linux=Linux; win32=Windows; cygwin=Windows/Cygwin;darwin= MAC OS X; os2=OS/2; os2emx=OS/2 EMX
print("Platform: %s\n" % (sys.platform))
print("Major: %s\n" % (sys.getwindowsversion()[0],))
print("Minor: %s\n" % (sys.getwindowsversion()[1],))
print("Build: %s\n" % (sys.getwindowsversion()[2],))

# 0=Win32s on Windows 3.1, 1=Windows 95/98/ME, 2=Windows NT/2000/XP/x64, 3=Windows CE
print("Platform: %s\n" % (sys.getwindowsversion()[3],))
print("Service Pack: %s\n" % (sys.getwindowsversion().service_pack,))
print("Service Pack Minor: %s\n" % (sys.getwindowsversion().service_pack_minor,))
print("Service Pack Major: %s\n" % (sys.getwindowsversion().service_pack_major,))
print("Suite Mask: %s\n" % (sys.getwindowsversion().suite_mask,))

#do if statement to translate the number to a word?
#1=the system is a workstation, 2 = domain controller, 3=server but not domain controller
print("Product Type: %s\n" % (sys.getwindowsversion().product_type,))

print("version: %s\n" % (sys.version))

print("Machine Type: %s\n" % (platform.machine()))
print("Computer Name: %s\n" % (platform.node()))


print("***End***")

