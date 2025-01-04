#!/bin/bash
echo "Downloading Playlists..."
yt-dlp --verbose --embed-metadata --parse-metadata "description:(?s)(?P<meta_comment>.+)" --yes-playlist --write-auto-subs --embed-subs --embed-chapters --embed-thumbnail --embed-metadata -o "%(channel)s/Playlists/%(playlist_title)s/%(upload_date)s - %(title)s [%(id)s].%(ext)s" --download-archive archive.txt $1

