#!/bin/bash
echo "Downloading Playlists..."
yt-dlp --verbose -f "bestvideo[vcodec!~='vp0?9'][height<=?1080]+bestaudio/best[height<=?1080]" --yes-playlist --write-auto-subs --embed-subs --embed-chapters --embed-thumbnail -o "%(channel)s/Playlists/%(playlist_title)s/%(upload_date)s - %(title)s [%(id)s].%(ext)s" --embed-chapters --download-archive $CHANNEL_NAME.txt $1

