#!/bin/bash
# This uses playlist index, which is often wrong or newest first
#alias yt-dlplaylist='yt-dlp --verbose -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" --yes-playlist --write-auto-subs --embed-subs --embed-chapters --embed-thumbnail -o "%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s" --embed-chapters'

yt-dlp --verbose -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" --yes-playlist --write-auto-subs --embed-subs --embed-chapters --embed-thumbnail -o "%(channel)s/Playlists/%(playlist_title)s/%(upload_date)s - %(title)s [%(id)s].%(ext)s" --embed-chapters $1

