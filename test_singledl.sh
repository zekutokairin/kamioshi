#!/bin/bash

URL=$1

echo "Downloading Video..."
yt-dlp --embed-thumbnail --write-thumbnail --write-comments --add-metadata --write-info-json --write-description -o './[%(upload_date>%y%m%d)s] [%(id)s] %(title).50s[...]/%(uploader)s [%(upload_date>%y%m%d)s-%(timestamp>%H%M%S)s] %(title)s [%(id)s].%(ext)s' --sub-langs "en.*" --write-subs --write-auto-subs --cookies-from-browser firefox --concurrent-fragments 8  $URL
