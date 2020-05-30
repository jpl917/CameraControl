# Control Cameras using gphoto2
The script is based on the [libgphoto2](http://www.gphoto.org/) and [gphoto2](http://www.gphoto.org/proj/gphoto2/). gphoto2 is a command line frontend of libgphoto2. 

It is used to change parameters, clear cameras, download images. 

Notice: for Canon EOS 800D, the version of libgphoto2 >= 2.5.20.


## Dependency
`bash install.sh`

or [recommend] install step by step as follows:

### libgphoto2 and gphoto2
```
sudo apt-get install cmake libpopt-dev libtool

cd ThirdParty/
tar xzvf autoconf-2.65.tar.gz 
tar xzvf automake-1.16.tar.gz 
tar xzvf gphoto2-2.5.20.tar.gz 
tar xjvf libgphoto2-2.5.20.tar.bz2 
tar xzvf m4-1.4.13.tar.gz 
tar xzvf SDL2-2.0.9.tar.gz 
tar xzvf SDL2_image-2.0.4.tar.gz 

cd libgphoto2-2.5.20
./configure
make
sudo make install
ldconfig

cd ../gphoto2-2.5.20
./configure
make
sudo make install
make check
```

### [SDL2](https://libsdl.org) and [SDL2_image](https://libsdl.org/projects/SDL_image) for gphoto-live-preview

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
```
cd ../../gphoto-live-preview/program
mkdir build && cd build
cmake ..
make -j4
./liveview
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
* --set-config-index    drivemode=0 (0: Single, 1: Continuous high speed, 2: Continuous low speed)

For unknown configuration choices: `--get-config [name]` or  `--get-config imageformat`

List all configuration: `gphoto2 --list-all-config`


## Problems during installation
if error: 'aclocal-1.16' is missing on your system.
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


