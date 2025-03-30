# Kamioshi

An easy solution for archiving and preserving your favorite VTuber's work.

# Usage
`fullarchive.sh https://www.youtube.com/@SomeUser`

# What It Does

1. Saves filenames with upload dates YYYYMMDD for chronological order.
2. Saves filenames with video ID for deduping.
3. Use the yt-lp archive text file per-channel so you can resume archives.
4. Save Playlists to ChannelName/Playlistname directory for convenient watching.
5. Save Videos to ChannelName/Videos/ directory IF they not already present.
6. Save Shorts to a ChannelName/Shorts directory IF they not already present.

# Notes
If you want to download a bunch of single videos in a queue:
# Install taskspooler
# ts singledl <URL>
