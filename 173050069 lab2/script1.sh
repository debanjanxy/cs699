#!/usr/bin/env bash

cd "$1"
if [ $(ls -1A test | wc -l) -gt 1 ];
then
cd ~/173050069\ lab2/"$1"/test
mv "$(ls -p | grep -v /)" ~/173050069\ lab2/"$1"/test/test_backup
cp -r test_backup ~/173050069\ lab2/"$1"/backup
else
echo "Nothing to do...." 
fi

