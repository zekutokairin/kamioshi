
#!/bin/bash

URL=$1

# Download Videos
echo "Downloading Videos..."
yt-dlp --verbose -f "bestvideo[vcodec!~='vp0?9'][height<=?1080]+bestaudio/best[height<=?1080]" --yes-playlist --write-auto-subs --embed-subs --embed-chapters --embed-thumbnail -o "%(channel)s/Videos/%(upload_date)s - %(title)s [%(id)s].%(ext)s" --embed-chapters --download-archive $CHANNEL_NAME.txt $URL

