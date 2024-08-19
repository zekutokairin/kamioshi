#!/bin/bash

URL="https://www.youtube.com/@KunaiNakasato"
#URL="https://www.youtube.com/@HizakiGamma"
#URL="https://www.youtube.com/@ZekuTokairin"

DOMAIN=$(echo ${URL} | awk -F'/' '{print $1FS$2FS$3}')    
CHANNEL_NAME=$(echo ${URL} | awk -F'/@' '{print $2}')    

# This script is for if you've somehow downloaded a bunch of videos in the right
# format, but haven't been added to the archive file
find . | awk -F'[][]' '{print $2}' | xargs -I {} echo "youtube {}" >> $CHANNEL_NAME.txt

