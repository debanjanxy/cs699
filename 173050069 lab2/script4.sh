#!/bin/bash

clear
cd 
cd ~/173050069\ lab2/"$1"/books
echo "Available books are : "
ls
echo "#################################################"
echo Enter Book Name
read name
evince $name

