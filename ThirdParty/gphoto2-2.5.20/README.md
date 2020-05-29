# gphoto2

## What is gphoto2?
gphoto2 is a command-line frontend to libgphoto2.

## Where can I find more information?
Visit the gphoto project web site. It should always be found at least
at one of the following URLs:
 - http://www.gphoto.com/
 - http://www.gphoto.org/
 - http://gphoto.sourceforge.net/
 - https://github.com/gphoto/
 - http://sf.net/projects/gphoto

The man page is in the file doc/gphoto2.1

## How do I build it?
```
autoreconf -is  #If using SVN source
configure
make
make install
```

Out-of-tree builds are supported. `configure --help` may help.

To build gphoto2 you will need besides the common build tools:
- The libgphoto2 library.
- The popt libraries (for commandline option handling), package named popt-devel or popt-dev 

Optional:
- The EXIF library. (libexif-devel, libexif-dev or similar)
- The JPEG library. (libjpeg-devel, libjpeg-dev, or jpeg-dev or similar)
- The CDK library (for ncurses based configuration UI). (cdk-devel or similar)
- The AALIB library (for ascii art rendering of previews). (aalib-devel or similar)

## How do I test it?
```
make check
```

The test suite checks the installation and basic functionality of the gphoto2
program and the 'Directory Browse' libgphoto2 camera driver.
