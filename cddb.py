#!/usr/bin/python
# vim: fileencoding=utf-8

import CDDB, DiscID

cdrom = DiscID.open()
disc_id = DiscID.disc_id(cdrom)
#disc_id = [2417058606, 46, 150, 7370, 13269, 19460, 25947, 32305, 39009, 46232, 52252, 57642, 65161, 71936, 78422, 84966, 92375, 99055, 108136, 114731, 119543, 126023, 134664, 141327, 150150, 160145, 167527, 175022, 181651, 186421, 195267, 202583, 209452, 216932, 222989, 225177, 227313, 232838, 240578, 247447, 258438, 264953, 269940, 277132, 286799, 296798, 305398, 310924, 4453]

(query_status, query_info) = CDDB.query(disc_id)
category = query_info['category']
discid = query_info['disc_id']

(read_status, read_info) = CDDB.read(category, discid)
print read_info
exit(0)
(category, disc_title) = read_info['DTITLE'].split(' / ')
year = read_info['DYEAR']
genre = read_info['DGENRE']
for i in range(disc_id[1]):
	(title, vocal) = read_info['TTITLE' + `i`].split(' / ')
	print "%.02d|%s|%s|%s|%s|%s" % (i+1, title, vocal,disc_title,year,genre)

