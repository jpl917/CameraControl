### How to install libgphoto2 and gphoto2. (gphoto2 is a command line frontend of libgphoto2)

[gphoto2] http://gphoto.sourceforge.net/doc/manual/ref-gphoto2-cli.html
[Notice] For Canon EOS 800D, the version of libgphoto2 >= 2.5.20.

$ sudo apt-get install libpopt-dev
$ sudo apt-get install libtool

$ cd libgphoto2-2.5.20
$ ./configure
$ make
$ sudo make install
$ ldconfig

$ cd gphoto2-2.5.20
$ ./configure
$ make
$ sudo make install
$ make check






