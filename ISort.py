#sudo apt-get install python-pyexiv2
import Image,os,glob,shutil,sys,pyexiv2
#./organizador.py PathOrigen PathDestino
carpetaOrigen = sys.argv[1]
carpetaDestino = sys.argv[2]

size = 100, 100

# Se crea los directorios por fecha
os.chdir(carpetaOrigen)
for file in glob.glob('*.*'):
	os.chdir(carpetaOrigen)
	metadata = pyexiv2.ImageMetadata(file)
	metadata.read()
	try:
		Datetime = metadata['Exif.Image.DateTime'].raw_value
		fecha = Datetime.split()
		fechaDir = fecha[0].split(':')
		nombreCarpeta = fechaDir[0]+'-'+fechaDir[1]+'-'+fechaDir[2]
		newDir = os.path.join(carpetaDestino,nombreCarpeta)
		if not os.path.isdir(newDir):
			os.mkdir(newDir)
			shutil.move(file,newDir)
		else:
			shutil.move(file,newDir)
	#Crea los tumbs por carpeta
		diresctorioThumbs = os.path.join(carpetaDestino+'/'+nombreCarpeta,'thumbs')
		if not os.path.isdir(diresctorioThumbs):
			os.mkdir(diresctorioThumbs)
		os.chdir(carpetaDestino+'/'+nombreCarpeta)
		for file in glob.glob('*.*'):
			os.chdir(carpetaDestino+'/'+nombreCarpeta)
			name,ex = os.path.splitext(file)
			im = Image.open(file)
			os.chdir(diresctorioThumbs)
			im.thumbnail(size,Image.ANTIALIAS)
			im.save(name+".thumbnail","JPEG")
	except KeyError:
		print "Error con la etiqueta de alguna de las fotos."

