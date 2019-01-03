import re
from appJar import gui

def convert():
	#Toma la ruta del FileEntry
	root = app.getEntry("MD_File")
	#Abre el archivo de la ruta
	md = open(root, "r")
	#Lee el archivo
	crudeContent = md.read()
	#Cierra el archivo
	md.close()

	#Prepara una estructura abierta de HTML
	htmlContent = '''<html>
	<head>
		<title>Title</title>
		<meta charset="uft-8">
	</head>
	<body>
	'''
	#Separa el contenido por cada enter
	content = crudeContent.split("\n")
	
	enlista = False
	#Aca se procesa cada linea
	for linea in content:
		#Cosas que se definen al principio de la linea (Titulos, Blockquotes, Etc)
		
		###Titulos
		
		#Titulo 1
		if re.match(r"# ",linea):
			print("Detectado: H1")
			linea = re.sub(r"# ","",linea)
			htmlContent+="		<h1>"+linea+"</h1>\n"
	
		#Titulo 2
		elif re.match(r"## ",linea):
			print("Detectado: H2")
			linea = re.sub(r"## ","",linea)
			htmlContent+="		<h2>"+linea+"</h2>\n"
			
		#Titulo 3
		elif re.match(r"### ",linea):
			print("Detectado: H3")
			linea = re.sub(r"### ","",linea)
			htmlContent+="		<h3>"+linea+"</h3>\n"
			
		#Titulo 4
		elif re.match(r"#### ",linea):
			print("Detectado: H4")
			linea = re.sub(r"#### ","",linea)
			htmlContent+="		<h4>"+linea+"</h4>\n"
			
		#Titulo 5
		elif re.match(r"##### ",linea):
			print("Detectado: H5")
			linea = re.sub(r"##### ","",linea)
			htmlContent+="		<h5>"+linea+"</h5>\n"
			
		#Titulo 6
		elif re.match(r"###### ",linea):
			print("Detectado: H6")
			linea = re.sub(r"###### ","",linea)
			htmlContent+="		<h6>"+linea+"</h6>\n"
		
		###Separador
		elif re.match(r"---",linea):
			print("Detectado: HR")
			htmlContent+="		<hr>\n"
			
		###Lista desordenada
		
		
		
		#No hay nada?? Es un texto plano
		else:
			htmlContent+="		<p>"+linea+"</p>\n"
			
			
	#Cierra <body> y cierra <html>
	
	htmlContent+='''</body>
</html>'''
	
	#Ahora a guardar el archivo!!!
	
	saveRoot = app.saveBox(title="Save...",fileName=None,dirName=None,fileExt=".html", fileTypes=[('HTML file', '*.html *.htm'), ('Plain text file', '*.txt')])
	
	saveFile = open(saveRoot, "w")
	
	saveFile.write(htmlContent)
	
	saveFile.close()
	
	#Finish
	
def save():
	print("Save")

def options(opt):
	if opt == "Convert":
		convert()
	if opt == "Save":
		save()
	
def aboutPress(abt):
	print("About "+str(abt))

about = ["Help","Credits"]

app = gui("md2html","300x150")

app.addMenuList("About", about, aboutPress)

app.addLabel("Title","Welcome to md2html")

app.addFileEntry("MD_File")

app.addHorizontalSeparator()

app.addButtons(["Convert","Exit"],options)

app.go()