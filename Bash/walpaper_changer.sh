#!/bin/bash
###
# File: walpaper_changer.sh
# Created: Friday, 7th February 2020 2:05:55 am
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Friday, 7th February 2020 2:34:53 am
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

# DATA=$(curl -s https://api.unsplash.com/photos/random?client_id=31f0e3b7987a59c33b7f27719eaecd22e430ec4408f3667b9b604f57a5719db1 | grep -Po '"full":.*?[^\\]",')
# LINK=$(echo $DATA | cut -f4- -d'"')
# URL=$(echo $LINK | cut -d'"' -f'1')

ID="31f0e3b7987a59c33b7f27719eaecd22e430ec4408f3667b9b604f57a5719db1"
URL=$(curl -s https://api.unsplash.com/photos/random?client_id=${ID} | grep -Po '"full":.*?[^\\]",' | cut -f4- -d'"' | cut -d'"' -f'1')

wget $URL -O "desktop_back.jpeg"

function de () {
	# Desktop Environment Detector
	# Can detect 'xfce, kde, gnome and lxde'

	if [ "$XDG_CURRENT_DESKTOP" = "" ]; then
		desktop=$( echo "$XDG_DATA_DIRS" | tr '[A-Z]' '[a-z]' | sed 's/.*\(xfce\|kde\|gnome\|lxde\).*/\1/' )
	else
		desktop=$( echo "$XDG_CURRENT_DESKTOP" | tr '[A-Z]' '[a-z]' | sed 's/.*\(xfce\|kde\|gnome\|lxde\).*/\1/' )
	fi

	echo "$desktop" # Returns Current DE name
}

if [[ `de` == 'xfce' ]]; then
    xfconf-query -c xfce4-desktop --create -p /backdrop/screen0/monitor0/workspace0/last-image -s $URL
elif [[ `de` == 'gnome' ]]; then
    gsettings set org.gnome.desktop.background picture-uri $URL
fi