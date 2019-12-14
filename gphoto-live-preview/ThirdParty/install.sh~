#1. [GCC](https://gcc.gnu.org)
#2. [gPhoto2](http://www.gphoto.org/proj/gphoto2)

#3. [SDL2](https://libsdl.org)
#sudo apt-get install libsdl2-dev
cd SDL2-2.0.9
mkdir build
cd build
cmake ..
make -j4 && sudo make install

#[SDL2_image](https://libsdl.org/projects/SDL_image)    
#sudo apt-get install libsdl2-image-dev
cd ../../SDL2_image-2.0.4
./configure
make -j4 && sudo make install

#[error:'aclocal-1.16' is missing on your system.]
'''
wget https://ftp.gnu.org/gnu/automake/automake-1.16.tar.gz
tar -xzvf automake-1.16.tar.gz
cd automake-1.16
./configure --prefix=/usr/
make -j4 && sudo make install
#[check:aclocal --version]
#change Makefile
#doc/aclocal-$(APIVERSION).1: $(aclocal_script) lib/Automake/Config.pm
                $(update_mans) aclocal-$(APIVERSION)
#doc/automake-$(APIVERSION).1: $(automake_script) lib/Automake/Config.pm
                $(update_mans) automake-$(APIVERSION) --no-discard-stderr


wget ftp://ftp.gnu.org/gnu/autoconf/autoconf-2.65.tar.gz
tar zxvf autoconf-2.65.tar.gz
cd autoconf-2.69
./configure --prefix=/usr/
make -j4 && sudo make install
#[check: /usr/bin/autoconf -V]

wget ftp://ftp.gnu.org/gnu/m4/m4-1.4.13.tar.gz
tar m4-1.4.13.tar.gz
cd m4-1.4.13
./configure --prefix=/usr/
make -j4 && sudo make install

wget ftp://ftp.gnu.org/gnu/libtool/libtool-1.3.5.tar.gz
tar libtool-1.3.5.tar.gz
cd libtool-1.3.5
./configure --prefix=/usr/
make -j4 && sudo make install
'''
	

#5. DSLR Camera


