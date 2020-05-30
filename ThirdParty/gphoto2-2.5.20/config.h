/* config.h.  Generated from config.h.in by configure.  */
/* config.h.in.  Generated from configure.ac by autoheader.  */

/* Define to 1 if translation of program messages to the user's native
   language is requested. */
#define ENABLE_NLS 1

/* The gettext domain we're using */
#define GETTEXT_PACKAGE "gphoto2"

/* whether we use aalib */
/* #undef HAVE_AA */

/* The C compiler we're using */
#define HAVE_CC "gcc"

/* whether we have CDK */
/* #undef HAVE_CDK */

/* whether we have old CDK */
/* #undef HAVE_CDK_20010421 */

/* Define if the GNU dcgettext() function is already present or preinstalled.
   */
#define HAVE_DCGETTEXT 1

/* Define to 1 if you have the declaration of `SIGHUP', and to 0 if you don't.
   */
#define HAVE_DECL_SIGHUP 1

/* Define to 1 if you have the declaration of `SIGINT', and to 0 if you don't.
   */
#define HAVE_DECL_SIGINT 1

/* Define to 1 if you have the declaration of `SIGTERM', and to 0 if you
   don't. */
#define HAVE_DECL_SIGTERM 1

/* Define to 1 if you have the declaration of `SIGUSR1', and to 0 if you
   don't. */
#define HAVE_DECL_SIGUSR1 1

/* Define to 1 if you have the declaration of `SIGUSR2', and to 0 if you
   don't. */
#define HAVE_DECL_SIGUSR2 1

/* Define to 1 if you have the <dlfcn.h> header file. */
#define HAVE_DLFCN_H 1

/* Define to 1 if you have the <fcntl.h> header file. */
#define HAVE_FCNTL_H 1

/* Define if the GNU gettext() function is already present or preinstalled. */
#define HAVE_GETTEXT 1

/* Define if you have the iconv() function. */
#define HAVE_ICONV 1

/* Define to 1 if you have the <inttypes.h> header file. */
#define HAVE_INTTYPES_H 1

/* whether we use libjpeg */
/* #undef HAVE_JPEG */

/* whether we compile with libexif support */
/* #undef HAVE_LIBEXIF */

/* whether libexif has exif-ifd.h (>= 0.5.3) */
/* #undef HAVE_LIBEXIF_IFD */

/* whether libexif has exif-log.h (>= 0.6.9) */
/* #undef HAVE_LIBEXIF_LOG */

/* whether we compile with libgphoto2 support */
#define HAVE_LIBGPHOTO2 1

/* Define to 1 if you have the `m' library (-lm). */
#define HAVE_LIBM 1

/* Define to 1 if you have the <memory.h> header file. */
#define HAVE_MEMORY_H 1

/* Define to 1 if you have the `pause' function. */
#define HAVE_PAUSE 1

/* whether the popt library is available */
#define HAVE_POPT 1

/* Define to 1 if you have the <process.h> header file. */
/* #undef HAVE_PROCESS_H */

/* Define if we use pthread.h. */
#define HAVE_PTHREAD 1

/* whether we use readline */
/* #undef HAVE_RL */

/* Define to 1 if you have the `signal' function. */
#define HAVE_SIGNAL 1

/* Define to 1 if you have the <signal.h> header file. */
#define HAVE_SIGNAL_H 1

/* Define to 1 if you have the `sleep' function. */
#define HAVE_SLEEP 1

/* Define to 1 if you have the `spawnve' function. */
/* #undef HAVE_SPAWNVE */

/* Define to 1 if you have the <stdint.h> header file. */
#define HAVE_STDINT_H 1

/* Define to 1 if you have the <stdlib.h> header file. */
#define HAVE_STDLIB_H 1

/* Define to 1 if you have the <strings.h> header file. */
#define HAVE_STRINGS_H 1

/* Define to 1 if you have the <string.h> header file. */
#define HAVE_STRING_H 1

/* Define to 1 if you have the `strptime' function. */
#define HAVE_STRPTIME 1

/* Define to 1 if you have the <sys/stat.h> header file. */
#define HAVE_SYS_STAT_H 1

/* Define to 1 if you have the <sys/time.h> header file. */
#define HAVE_SYS_TIME_H 1

/* Define to 1 if you have the <sys/types.h> header file. */
#define HAVE_SYS_TYPES_H 1

/* Define to 1 if you have the <sys/wait.h> header file. */
#define HAVE_SYS_WAIT_H 1

/* Define to 1 if you have the <unistd.h> header file. */
#define HAVE_UNISTD_H 1

/* Define as const if the declaration of iconv() needs const. */
#define ICONV_CONST 

/* Define to the sub-directory where libtool stores uninstalled libraries. */
#define LT_OBJDIR ".libs/"

/* gphoto development mailing list */
#define MAIL_GPHOTO_DEVEL "<gphoto-devel@lists.sourceforge.net>"

/* gphoto translation mailing list */
#define MAIL_GPHOTO_TRANSLATION "<gphoto-translation@lists.sourceforge.net>"

/* gphoto user mailing list */
#define MAIL_GPHOTO_USER "<gphoto-user@lists.sourceforge.net>"

/* Name of package */
#define PACKAGE "gphoto2"

/* Define to the address where bug reports for this package should be sent. */
#define PACKAGE_BUGREPORT "gphoto-devel@lists.sourceforge.net"

/* Define to the full name of this package. */
#define PACKAGE_NAME "gphoto2 command line interface"

/* Define to the full name and version of this package. */
#define PACKAGE_STRING "gphoto2 command line interface 2.5.20"

/* Define to the one symbol short name of this package. */
#define PACKAGE_TARNAME "gphoto2"

/* Define to the home page for this package. */
#define PACKAGE_URL ""

/* Define to the version of this package. */
#define PACKAGE_VERSION "2.5.20"

/* SIGHUP replacement */
/* #undef SIGHUP */

/* SIGINT replacement */
/* #undef SIGINT */

/* SIGTERM replacement */
/* #undef SIGTERM */

/* SIGUSR1 replacement */
/* #undef SIGUSR1 */

/* SIGUSR2 replacement */
/* #undef SIGUSR2 */

/* Define to 1 if you have the ANSI C header files. */
#define STDC_HEADERS 1

/* camera list with support status */
#define URL_DIGICAM_LIST "http://www.teaser.fr/~hfiguiere/linux/digicam.html"

/* gphoto project home page */
#define URL_GPHOTO_HOME "http://www.gphoto.org/"

/* gphoto github project page */
#define URL_GPHOTO_PROJECT "https://github.com/gphoto"

/* jphoto home page */
#define URL_JPHOTO_HOME "http://jphoto.sourceforge.net/"

/* information about using USB mass storage */
#define URL_USB_MASSSTORAGE "http://www.linux-usb.org/USB-guide/x498.html"

/* Version number of package */
#define VERSION "2.5.20"

/* Number of bits in a file offset, on hosts where this is settable. */
/* #undef _FILE_OFFSET_BITS */

/* Define for large files, on AIX-style hosts. */
/* #undef _LARGE_FILES */
