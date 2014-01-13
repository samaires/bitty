import controller as con
import libtorrent as lt
import time
import sys
import subprocess


ses = lt.session()
ses.listen_on(6881,6891)

#active_torrents = []

while True:
	

	input = raw_input("What now?")


	if (input == "d"):
		target_torrent = raw_input("Enter name of torrent file: ")
		con.start_bitty(target_torrent, ses)

	if (input == "status"):
		con.get_status(ses)



	ses.save_state()
