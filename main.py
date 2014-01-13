import controller as con
import libtorrent as lt
import time
import sys
import subprocess


ses = lt.session()
ses.listen_on(6881,6891)

while True:
	input = raw_input("What now?")

	if (input == "Download"):
		target_torrent = raw_input("Enter name of torrent file: ")
		h = con.start_bitty(target_torrent, ses)

	if (input == "status"):
		con.get_status(ses, h)
