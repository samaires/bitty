import libtorrent as lt
import time
import sys
import subprocess

def bitty(torrent, ses):

	e = lt.bdecode(open(torrent, 'rb').read())
	info = lt.torrent_info(e)

	h = ses.add_torrent(info, "./")

	print "Starting", h.name()

	while (not h.is_seed()):
		s = h.status()

		state_str = ['queued', 'checking', 'downloading metadata', \
					'downloading', 'finished', 'seeding', 'allocating']
		
		subprocess.call('clear', shell=True)
		
		print '%.2f%% complete (down: %.1f kb/s up: %1f kb/s peers: %d) %s' % \
			(s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
				s.num_peers, state_str[s.state])
		
		ses.save_state()

		time.sleep(1)

def get_status(ses):
	ses.get_status()