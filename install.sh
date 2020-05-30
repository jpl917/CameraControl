#1. [gPhoto2](http://www.gphoto.org/proj/gphoto2)
sudo apt-get install cmake
sudo apt-get install libpopt-dev
sudo apt-get install libtool



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


#2. [SDL2](https://libsdl.org)
#sudo apt-get install libsdl2-dev
cd ../SDL2-2.0.9
mkdir build
cd build
cmake ..
make -j4 && sudo make install


#3. [SDL2_image](https://libsdl.org/projects/SDL_image)    
#sudo apt-get install libsdl2-image-dev
cd ../../SDL2_image-2.0.4
./configure
make -j4 && sudo make install


#4. gphoto-live-preview
cd ../../gphoto-live-preview/program
mkdir build && cd build
cmake ..
make -j4
