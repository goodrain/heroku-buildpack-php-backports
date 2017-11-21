#!/usr/bin/env bash
# 安装php7需要依赖

OUT_PREFIX=$1

# fail hard
set -o pipefail
# fail harder
set -eux

DEFAULT_VERSION="6.1.0"
dep_version=${VERSION:-$DEFAULT_VERSION}
dep_dirname=gmp-${dep_version}
dep_archive_name=${dep_dirname}.tar.xz
dep_url=https://gmplib.org/download/gmp/${dep_archive_name}

echo "-----> before php7 configure. install gmp ${dep_version}..."

curl -L ${dep_url} | xz -d - | tar xvf -

echo "-----> down and  php7 configure. install gmp ${dep_version}..."


pushd ${dep_dirname}
./configure --prefix=${OUT_PREFIX}
make -s -j 9
make install-strip -s
popd

rm -rf ${OUT_PREFIX}/share/man ${OUT_PREFIX}/share/doc

echo "-----> Done."
https://gmplib.org/download/gmp/gmp-6.1.0.tar.xz