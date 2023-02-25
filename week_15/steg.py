# PIL module is used to extract and modify pixels of an image
from PIL import Image

# Convert message into 8-bit binary ASCII value
def getBin(data):

		# list of binary codes
		# of given data
		newd = []

		for i in data:
			newd.append(format(ord(i), '08b'))
		return newd

# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):

	binlist = getBin(data)
	lendata = len(binlist)
	imdata = iter(pix)

	for i in range(lendata):

		# Extracting 3 pixels at a time - needed for a single ASCII char
		pix = [value for value in imdata.__next__()[:3] +
								imdata.__next__()[:3] +
								imdata.__next__()[:3]]

		# Pixel value should be made
		# odd for 1 and even for 0
		for j in range(0, 8):
			if (binlist[i][j] == '0' and pix[j]% 2 != 0):
				pix[j] -= 1

			elif (binlist[i][j] == '1' and pix[j] % 2 == 0):
				if(pix[j] != 0):
					pix[j] -= 1
				else:
					pix[j] += 1
			

		# The last byte of the third pixel tells
		# whether to stop or continue.
		# 0 means keep reading; 1 means the
		# message is over.
		if (i == lendata - 1):
			if (pix[-1] % 2 == 0):
				if(pix[-1] != 0):
					pix[-1] -= 1
				else:
					pix[-1] += 1

		else:
			if (pix[-1] % 2 != 0):
				pix[-1] -= 1

		pix = tuple(pix)
		yield pix[0:3]
		yield pix[3:6]
		yield pix[6:9]

def encode_enc(newimg, data):
	w = newimg.size[0]
	(x, y) = (0, 0)

	for pixel in modPix(newimg.getdata(), data):

		# Putting modified pixels in the new image
		newimg.putpixel((x, y), pixel)
		if (x == w - 1):
			x = 0
			y += 1
		else:
			x += 1

# Encode data into image
def hide():
	img = input("Enter image name (without the extension): ")
	image = Image.open(img+".png", 'r')

	data = input("Enter message to be encoded: ")
	if (len(data) == 0):
		raise ValueError('Message is empty')

	newimg = image.copy()
	encode_enc(newimg, data)

	new_img_name = input("Enter the name of new image (without the extension): ")
	newimg.save(new_img_name+".png")

# Decode the data in the image
def reveal():
	img = input("Enter image name (without the extension): ")
	image = Image.open(img+".png", 'r')

	data = ''
	imgdata = iter(image.getdata())

	while (True):
		pixels = [value for value in imgdata.__next__()[:3] +
								imgdata.__next__()[:3] +
								imgdata.__next__()[:3]]

		# string of binary data
		binstr = ''

		for i in pixels[:8]:
			if (i % 2 == 0):
				binstr += '0'
			else:
				binstr += '1'

		data += chr(int(binstr, 2))
		if (pixels[-1] % 2 != 0):
			return data

print("Hiding Messages Using Steganography")
a = int(input("1. Hide a message\n2. Reveal hidden message\n"
                 "Please enter your choice: "))
if (a == 1):
	hide()
elif (a == 2):
	print("Decoded Message: " + reveal())
else:
	raise Exception("Please enter either 1 or 2")
