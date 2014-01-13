import libtorrent as lt
import time
import sys
import subprocess

active_torrents = []

def start_bitty(torrent, ses):
	e = lt.bdecode(open(torrent, 'rb').read())
	info = lt.torrent_info(e)
	h = ses.add_torrent(info, "./")
	active_torrents.append(h)
	print "Starting", h.name()
	

def get_status(ses):
	state_str = ['queued', 'checking', 'downloading metadata', \
					'downloading', 'finished', 'seeding', 'allocating']
	subprocess.call('clear', shell=True)

	for i in active_torrents:
		s = i.status()
		print '%.2f%% complete (down: %.1f kb/s up: %1f kb/s peers: %d) %s' % \
				(s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
					s.num_peers, state_str[s.state])
