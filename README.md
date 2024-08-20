# Kamioshi

An easy solution for archiving and preserving your favorite VTuber's work.

Initially, I'd tried approaches that were using queues, a sqlite3 database, and so on.

I found that these overcomplicated the whole thing. Here's my new approach:

1. Save filenames with upload dates YYYYMMDD for chronological order.
2. Save filenames with video ID for deduping.
3. Use the yt-lp archive file per-channel in case the channel is still going.
4. Save Playlists to ChannelName/Playlistname directory for convenient watching.
5. Save Videos to Videos/ directory IF they are not already present.
6. Save Shorts to a Shorts directory IF they are not already present.
7. Create torrent from command line.

# Future Tasks
- Fix totalsize to work with livestreams if possible
