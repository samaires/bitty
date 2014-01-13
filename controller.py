import libtorrent as lt
import time
import sys
import subprocess

def start_bitty(torrent, ses):

	e = lt.bdecode(open(torrent, 'rb').read())
	info = lt.torrent_info(e)

	h = ses.add_torrent(info, "./")

	print "Starting", h.name()

	return h

def get_status(ses, torrent):
	s = torrent.status()
	
	state_str = ['queued', 'checking', 'downloading metadata', \
					'downloading', 'finished', 'seeding', 'allocating']
		
	subprocess.call('clear', shell=True)

	print '%.2f%% complete (down: %.1f kb/s up: %1f kb/s peers: %d) %s' % \
			(s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
				s.num_peers, state_str[s.state])