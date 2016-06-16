#!/bin/bash

# 切换工作目录
basepath=$(cd `dirname $0`; pwd)
cd $basepath

cat ./keywords | while read line; do
    ./search googleshopping "$line" 10
done
