

def encrypt(str):
	key = dict()
	dst = dict()
	i = 0
	for j in range(17):
		key[j] = 0
		dst[j] = 0
	nBytes = len(str)
	while (i < nBytes):
		key[i] = ord(str[i])
		dst[i] = key[i]
		i=i+1

	rslt = key[0] + key[1]*256 + key[2]*65536 + key[3]*16777216
	one = rslt * 213119 + 2529077
	one = one - int(one/ 4294967296) * 4294967296
	rslt = key[4] + key[5]*256 + key[6]*65536 + key[7]*16777216
	two = rslt * 213247 + 2529089
	two = two - int(two/ 4294967296) * 4294967296
	rslt = key[8] + key[9]*256 + key[10]*65536 + key[11]*16777216
	three = rslt * 213203 + 2529589
	three = three - int(three/ 4294967296) * 4294967296
	rslt = key[12] + key[13]*256 + key[14]*65536 + key[15]*16777216
	four = rslt * 213821 + 2529997
	four = four - int(four/ 4294967296) * 4294967296
	key[0] = one & 0xFF
	key[1] = (one >> 8) & 0xFF
	key[2] = (one >> 16) & 0xFF
	key[3] = (one >> 24) & 0xFF
	key[4] = two & 0xFF
	key[5] = (two >> 8) & 0xFF
	key[6] = (two >> 16) & 0xFF
	key[7] = (two >> 24) & 0xFF
	key[8] = three & 0xFF
	key[9] = (three >> 8) & 0xFF
	key[10] = (three >> 16) & 0xFF
	key[11] = (three >> 24) & 0xFF
	key[12] = four & 0xFF
	key[13] = (four >> 8) & 0xFF
	key[14] = (four >> 16) & 0xFF
	key[15] = (four >> 24) & 0xFF
	dst[0] = dst[0] ^ key[0]
	i=1
	while (i<16):
		dst[i] = dst[i] ^ dst[i-1] ^ key[i]
		i=i+1
	i=0
	while (i<16):
		if (dst[i] == 0):
			dst[i] = 102
		i=i+1
	encrypt = "0x"
	i=0
	while (i<16):
		if (dst[i] < 16):
			encrypt = encrypt + "0" + "%x" % dst[i]
		else:
			encrypt = encrypt + "%x" % dst[i]
		i=i+1


	return encrypt