#charles.leerink@outlook.com
#get some info on m3u8 files

#
#example:
#'http://itsliveradiobackup.apple.com/streams/hub02/session02/256k/prog.m3u8'

import m3u8
import os


os.system('clear')
print "M3u8 info\n"
print "Stream URI: "
streamuri = raw_input()
m3u8_obj = m3u8.load(streamuri)  #load stream



print "\n"
print "Playlist Base URI:", m3u8_obj.base_uri
print "HLS Version: ", m3u8_obj.version
print "Playlist Type: ", m3u8_obj.playlist_type
print "Playlist Encryption Info: ", m3u8_obj.key
print "Segment Playtime in seconds: ", m3u8_obj.target_duration
print "\nSegements in Playlist:\n", m3u8_obj.segments
print "\n"
