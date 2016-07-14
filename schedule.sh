#!/usr/bin/bash

current_dir=`pwd`
current_user='root'
current_command="$current_dir/search.sh"

if [ $# > 6 -a $# < 1 ]; then
    echo "You give $# time~~~~~"
    echo 'You must give less than 6 And more than 1!'
    exit 1
fi

sed -i.bak -e "/$current_command/d" /etc/crontab

for time in $@; do
    min=`echo $time | cut -d : -f 2`
    hour=`echo $time | cut -d : -f 1`
    #echo $hour:$min
    message="$min $hour * * * $current_user . /etc/profile; . ~/.bash_profile; $current_command"
    set -f
    #echo $message
    echo $message >> /etc/crontab
    set +f
done

cat /etc/crontab | grep $current_command
