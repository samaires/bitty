import controller as con
import libtorrent as lt
import time
import sys
import subprocess


ses = lt.session()
ses.listen_on(6881,6891)

#active_torrents = []

while True:

	ses.load_state(ses)

	input = raw_input("What now?")

	if (input == "d"):
		target_torrent = raw_input("Enter name of torrent file: ")
		con.start_bitty(target_torrent, ses)

	if (input == "status"):
		con.get_status(ses)

	if (input == "pause"):
		input = raw_input("Which torrent? ")
		con.pause_download(int(input))

	if (input == "resume"):
		input = raw_input("Which torrent? ")
		con.resume_download(int(input))

	if (input == "downl"):
		input = raw_input("Which torrent? ")
		input_limit = raw_input("Input limit: ")
		con.set_download_limit(int(input), int(input_limit))

	ses.save_state()



