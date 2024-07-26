#!/bin/bash
# Give it the URL to the playlists of the channel you want to archive
yt-dlp --verbose -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" --yes-playlist --write-auto-subs --embed-subs --embed-chapters --embed-thumbnail -o "%(channel)s/Playlists/%(playlist_title)s/%(upload_date)s - %(title)s [%(id)s].%(ext)s" --embed-chapters $1
