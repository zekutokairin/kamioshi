#!/bin/bash

echo "Please MAKE SURE you're running this in the base directory of your archive! This is necessary for the archive.txt catalog to record what videos you've already downloaded!"

# Give it the URL to the playlists of the channel you want to archive
yt-dlp --verbose -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" --yes-playlist --write-auto-subs --embed-subs --embed-chapters --embed-thumbnail -o "%(channel)s/Playlists/%(playlist_title)s/%(upload_date)s - %(title)s [%(id)s].%(ext)s" --embed-chapters --download-archive archive.txt $1
