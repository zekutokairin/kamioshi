# TODO: Pythonify this
#yt-dlp --dump-single-json --flat-playlist 'https://www.youtube.com/playlist?list=UUqyL0oB2jl-5GpSg-GWZ_gw' | jq '[.entries[] | select(.duration != null and .view_count != null) | (.view_count / .duration)] | add | floor'
