#! /bin/sh
# Copyright (C) 1999-2018 Free Software Foundation, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Make sure '..' invalid in subdir .o's.

. test-init.sh

cat >> configure.ac << 'END'
_AM_DEPENDENCIES(GCJ)
AC_SUBST(GCJ)
END

cat > Makefile.am << 'END'
bin_PROGRAMS = convert
convert_SOURCES = x/../convert.java
END

$ACLOCAL
AUTOMAKE_fails
grep 'Makefile.am:.*\.\.' stderr
