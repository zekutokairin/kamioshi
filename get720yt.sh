#!/bin/bash

echo "Downloading 720p version of video..."
yt-dlp --verbose -f "bestvideo[vcodec!~='vp0?9'][height<=?720]+bestaudio/best[height<=?720]" --yes-playlist --write-auto-subs --embed-subs --embed-chapters --embed-thumbnail -o "%(channel)s/(upload_date)s - %(title)s [%(id)s].%(ext)s" --embed-chapters $1

