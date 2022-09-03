# rgenz
torrent upload helper

This tool is for Windows only. Use case is to simplify the process of uploading single video file on a private tracker. This will generate screenshots, torrent, and mediainfo for you. There are other uploader available that is specialized for other trackers so you can opt on using those instead if you are a heavy uploader.


Requirements:

- Latest Python3
- ffmpeg and mediainfo CLI (put them on your PATH - https://www.computerhope.com/issues/ch000549.htm)
- py3createtorrent (install via pip - https://pypi.org/project/py3createtorrent/)

Usage:
1. Edit the config.json file based on what you need. "tracker" field is for the announce URL, "ss_number" is to set how many screenshots you want to generate, "ss_gap" is the seconds between the generated screenshots, "pic_ext" is for the file extension for your screenshots. If you want lower file size/quality, use .jpg and if you want higher file size, use .png
2. Double-click the add_context_menu.bat to add the RGENZ-file to your context menu. Allow admin privilege. You can check the code if you have doubts.
3. Go to your video file, right-click and choose RGENZ-file on your context menu. The script will run and start the process.
4. Done. You can use the generated files to start your upload

The script is very limited in what it can do. It doesn't support Dolby Vision files.

Feel free to fork and improve. May or may not be updated.
