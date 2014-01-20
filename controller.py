import libtorrent as lt
import time
import sys
import subprocess

active_torrents = []

def start_bitty(torrent, ses):
	
	try:
		e = lt.bdecode(open(torrent, 'rb').read())
		info = lt.torrent_info(e)
		h = ses.add_torrent(info, "./")
		active_torrents.append(h)
		print "Starting", h.name()
	except Exception:
		print "FELLL"


def get_status(ses):

	state_str = ['queued', 'checking', 'downloading metadata', \
					'downloading', 'finished', 'seeding', 'allocating', 'paused']
	subprocess.call('clear', shell=True)


	for i in active_torrents:
		s = i.status()
		print '%.2f%% complete (down: %.1f kb/s up: %1f kb/s peers: %d) %s' % \
				(s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
					s.num_peers, state_str[s.state])

def pause_download(torrent):
	active_torrents[torrent].auto_managed(0)
	active_torrents[torrent].pause(1)

def resume_download(torrent):
	active_torrents[torrent].resume()
	active_torrents[torrent].auto_managed(1)

def set_download_limit(torrent, limit):
	l = limit * 1000
	active_torrents[torrent].set_download_limit(l)

def set_upload_limit(torrent, limit):
	l = limit * 1000
	active_torrents[torrent].set_upload_limit(l)

def get_tracker_url(torrent):
	s = active_torrents[torrent].status()
	print s.current_tracker

def get_peer_download(torrent):
	rgrggr
	for i in active_torrents:
		s = i.get_peer_info()

		s.down_speed