#Picture Forensics toolkit

This tool includes a view routes:

/exif_processing
/stego_processing

Eventually watermarking and a few other routes will be added.  Also facial recognition and picture matching is likely to be added.

The goal of this tool is to help investigators analyze pictures, looking for exif data (metadata), encrypt messages in order to prove a picture was reused (with stego and watermarking), and to find and compare pictures.

##Dependencies:

OpenCV - cv,cv2
ExifRead - exifread
PIL - Image
Flask 

##How to use:

Presently only the web server can be used, however there are plans to turn this into a library suite with easy to use high level interfaces.  Check back for more details here.

to run the server:

`python app.py`

Then pointer your browser here: [exif_processing](http://localhost:5000/exif_processing) or here: [stego_processing](http://localhost:5000/stego_processing).


