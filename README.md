# Control Cameras using gphoto2
The script is based on the [libgphoto2](http://www.gphoto.org/) and [gphoto2](http://www.gphoto.org/proj/gphoto2/). gphoto2 is a command line frontend of libgphoto2. 

It is used to change parameters, clear cameras, download images. 

Notice: for Canon EOS 800D, the version of libgphoto2 >= 2.5.20.

## Dependency
install step by step:

### libgphoto2 and gphoto2
```
sudo apt-get install cmake libpopt-dev libtool libusb-dev libusb-1.0.0-dev

cd ThirdParty/
tar xzvf autoconf-2.65.tar.gz 
tar xzvf automake-1.16.tar.gz 
tar xzvf gphoto2-2.5.23.tar.gz 
tar xzvf libgphoto2-2.5.23.tar.gz
tar xzvf m4-1.4.13.tar.gz 
tar xzvf SDL2-2.0.9.tar.gz 
tar xzvf SDL2_image-2.0.4.tar.gz 

cd libgphoto2-2.5.23
./configure
make
sudo make install
sudo ldconfig

cd ../gphoto2-2.5.23
./configure
make
sudo make install
make check
```

### [SDL2](https://libsdl.org) and [SDL2_image](https://libsdl.org/projects/SDL_image) for gphoto-live-preview

```
sudo apt-get install libsdl2-dev libsdl2-image-dev
```
or

```
cd ../SDL2-2.0.9
mkdir build
cd build
cmake ..
make -j4 && sudo make install

cd ../../SDL2_image-2.0.4
./configure
make -j4 && sudo make install
```

### gphoto-live-preview
This example shows one of the ways you can stream live video feed from your DSLR camera. It simply reads MJPEG output by gPhoto2 frame-by-frame, parses it, and put up the frame buffer on the screen window.

```
cd ../../gphoto-live-preview/program
gcc main.c -o liveview -lSDL2 -lSDL2_image
./liveview
```

### python related
```
sudo apt install python-tk
sudo apt install python-pip
sudo pip install matplotlib serial threading2 easygui
```

## Usage
`python main.py`


## Camera Settings
For details, please refer to [gphoto2](http://gphoto.sourceforge.net/doc/manual/ref-gphoto2-cli.html) or the documents/ folders

gphoto2 --port "usb:$portname"
* --set-config          shutterspeed="1/100"
* --set-config          aperture=16
* --set-config          iso=100
* --set-config-index    imageformat=1   (1: JPEG, 7: RAW with large JPEG)
* --set-config-index    drivemode=0 (0: Single, 1: Continuous high speed)

* --set-config-index    evfmode=1 (#Choice 0: 1, #Choice 1: 0)

For unknown configuration choices: `--get-config [name]` or  `--get-config imageformat`

List all configuration: `gphoto2 --list-all-config`


## Problems during installation

#### if 'aclocal-1.16' is missing on your system.
```
cd ThirdParty/automake-1.16
./configure --prefix=/usr/
make -j4 && sudo make install

[check:aclocal --version]
change Makefile
doc/aclocal-$(APIVERSION).1: $(aclocal_script) lib/Automake/Config.pm
                $(update_mans) aclocal-$(APIVERSION)
doc/automake-$(APIVERSION).1: $(automake_script) lib/Automake/Config.pm
                $(update_mans) automake-$(APIVERSION) --no-discard-stderr


cd ThirdParty/autoconf-2.69
./configure --prefix=/usr/
make -j4 && sudo make install
/usr/bin/autoconf -V

cd ThirdParty/m4-1.4.13
./configure --prefix=/usr/
make -j4 && sudo make install

sudo apt-get install libtool

//cd libtool-1.3.5
//./configure --prefix=/usr/
//make -j4 && sudo make install
```

#### if can not mount cameras (important)
enter bios -> xhci: disabled



