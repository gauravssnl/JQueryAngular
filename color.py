code='c\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00@\x00\x00\x00s\x94\x00\x00\x00d\x00\x00Z\x00\x00d\x01\x00Z\x01\x00d\x02\x00Z\x02\x00d\x03\x00Z\x03\x00d\x04\x00Z\x04\x00d\x05\x00Z\x05\x00d\x06\x00Z\x06\x00d\x07\x00Z\x07\x00e\x05\x00Z\x08\x00e\x03\x00Z\t\x00e\x07\x00Z\n\x00d\x08\x00Z\x0b\x00d\t\x00Z\x0c\x00d\n\x00Z\r\x00d\x0b\x00Z\x0e\x00d\x0c\x00Z\x0f\x00d\r\x00Z\x10\x00d\x0e\x00Z\x11\x00d\x0f\x00Z\x12\x00d\x10\x00Z\x13\x00d\x11\x00Z\x14\x00d\x12\x00Z\x15\x00d\x13\x00Z\x16\x00d\x14\x00Z\x17\x00d\x15\x00S(\x16\x00\x00\x00t\x03\x00\x00\x0030mt\x03\x00\x00\x0031mt\x03\x00\x00\x0032mt\x03\x00\x00\x0033mt\x03\x00\x00\x0034mt\x03\x00\x00\x0035mt\x03\x00\x00\x0036mt\x03\x00\x00\x0037ms\x04\x00\x00\x00\x1b[0ms\x04\x00\x00\x00\x1b[0;s\x04\x00\x00\x00\x1b[1ms\x04\x00\x00\x00\x1b[1;s\x04\x00\x00\x00\x1b[2;s\x04\x00\x00\x00\x1b[4;s\x04\x00\x00\x00\x1b[7;s\x04\x00\x00\x00\x1b[9;s\x03\x00\x00\x00\x1b[As\x03\x00\x00\x00\x1b[Bs\x03\x00\x00\x00\x1b[Cs\x03\x00\x00\x00\x1b[Ds\x04\x00\x00\x00\x1b[2KN(\x18\x00\x00\x00t\x05\x00\x00\x00blackt\x03\x00\x00\x00redt\x05\x00\x00\x00greent\x05\x00\x00\x00brownt\x04\x00\x00\x00bluet\x07\x00\x00\x00magentat\x04\x00\x00\x00cyant\t\x00\x00\x00lightgrayt\x06\x00\x00\x00purplet\x06\x00\x00\x00yellowt\x05\x00\x00\x00whitet\x07\x00\x00\x00defaultt\x05\x00\x00\x00colort\x04\x00\x00\x00boldt\n\x00\x00\x00bold_colort\n\x00\x00\x00dark_colort\n\x00\x00\x00underlinest\x02\x00\x00\x00bgt\r\x00\x00\x00strikes_colort\n\x00\x00\x00move_abovet\n\x00\x00\x00move_undert\r\x00\x00\x00spacing_rightt\x0c\x00\x00\x00spacing_leftt\x05\x00\x00\x00erase(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x06\x00\x00\x00scriptt\x08\x00\x00\x00<module>\x04\x00\x00\x00s.\x00\x00\x00\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x02\x06\x01\x06\x01\x06\x02\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01'
import os
output_dir = os.path.join(os.getcwd(), "pyc")
if not os.path.exists(output_dir):
	os.mkdir(output_dir)
	print("Output path created to store pyc files.")
with open(output_dir + "/color.pyc", "wb") as f:
	f.write('\x03\xf3\x0d\x0a\0\0\0\0')
	f.write(code)
	
import marshal
data=marshal.loads(code)
exec data
