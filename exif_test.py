
import piexif

file_name = "/media/taylor/curie/spherical/trail_images/GF024698.JPG"

exif_dict = piexif.load(file_name)
for line in exif_dict:
    print(line)
print(dir(exif_dict))

print(exif_dict['Exif'][piexif.ExifIFD.FocalLength])

exif_dict['Exif'][piexif.ExifIFD.BodySerialNumber] =  bytes('001', 'utf-8')
exif_dict['Exif'][piexif.ExifIFD.FocalLength] = (3,1)
print(exif_dict['Exif'][piexif.ExifIFD.FocalLength])


print(exif_dict['0th'][piexif.ImageIFD.DateTime])



exif_dict['0th'][piexif.ImageIFD.Make] = bytes('GoPro', 'utf-8')
exif_dict['0th'][piexif.ImageIFD.Model] = bytes('FUSION', 'utf-8')

# exif_bytes = piexif.dump(exif_dict)
# piexif.insert(exif_bytes, "foo.jpg")

print(exif_dict['Exif'][piexif.ExifIFD.BodySerialNumber].decode("utf-8") )

# for item in exif_dict:
#     print(dir(item))
