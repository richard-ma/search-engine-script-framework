#!/usr/bin/bash

current_dir=`pwd`
current_user='root'
current_command=$current_dir/search.sh

if [ $# != 3 ]; then
    echo "You give $# time~~~~~"
    echo 'You must give 3 time!'
    exit 1
fi

for time in $@; do
    min=`echo $time | cut -d : -f 2`
    hour=`echo $time | cut -d : -f 1`
    echo $hour:$min
    message="$min $hour * * * $current_user $current_command"
    set -f
    echo $message
    echo $message >> /etc/crontab
    set +f
done

cat /etc/crontab | grep $current_command
