import re
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

def convert(f, t, bgc,txtc, qbg,fs,fo):
	#Toma la ruta del FileEntry
	root = f
	#Abre el archivo de la ruta
	try:
		md = open(root, "r")
	except FileNotFoundError:
		if root == "No selected":
			print("No seleccionado")
			messagebox.showinfo("md2html","No selected")
			return 1
		else:
			print("Archivo no encontrado")
			messagebox.showinfo("md2html","Not found")
			return 1
	#Lee el archivo
	crudeContent = md.read()
	#Cierra el archivo
	md.close()

	#Prepara una estructura abierta de HTML
	htmlContent = '''<html>
	<head>
		<title>'''+t+'''</title>
		<meta charset="uft-8">
		<style>
			body{
			background-color:'''+bgc+''';
			color:'''+txtc+''';
			font-size:'''+fs+''';
			font-family:'''+fo+''';
			}
			.code{
			color:white;
			background-color:#000;
			color:#FFF; 
			font-family:monospace; 
			border-left:4px solid #0F0; 
			padding:3px;
			}
			.blockquote{
			background:'''+qbg+'''; 
			font-style:italic; 
			padding:5px; 
			border-left:2px solid #000;
			}
		</style>
	</head>
	<body>
	'''
	#Separa el contenido por cada enter
	content = crudeContent.split("\n")
	
	enlista = False
	encodigo = False
	#Aca se procesa cada linea
	for linea in content:
		#Cosas que se definen al principio de la linea (Titulos, Blockquotes, Etc)
		
		###Titulos
		
		#Titulo 1
		if re.match(r"# ",linea):
			if enlista == True:
				print("---SE SALIO EN LA LISTA---")
				enlista = False
				htmlContent+="		</ul>\n"
			print("Detectado: <h1>")
			linea = re.sub(r"# ","",linea)
			htmlContent+="		<h1>"+linea+"</h1>\n"
	
		#Titulo 2
		elif re.match(r"## ",linea):
			if enlista == True:
				print("---SE SALIO EN LA LISTA---")
				enlista = False
				htmlContent+="		</ul>\n"
			print("Detectado: <h2>")
			linea = re.sub(r"## ","",linea)
			htmlContent+="		<h2>"+linea+"</h2>\n"
			
		#Titulo 3
		elif re.match(r"### ",linea):
			if enlista == True:
				print("---SE SALIO EN LA LISTA---")
				enlista = False
				htmlContent+="		</ul>\n"
			print("Detectado: <h3>")
			linea = re.sub(r"### ","",linea)
			htmlContent+="		<h3>"+linea+"</h3>\n"
			
		#Titulo 4
		elif re.match(r"#### ",linea):
			if enlista == True:
				print("---SE SALIO EN LA LISTA---")
				enlista = False
				htmlContent+="		</ul>\n"
			print("Detectado: <h4>")
			linea = re.sub(r"#### ","",linea)
			htmlContent+="		<h4>"+linea+"</h4>\n"
			
		#Titulo 5
		elif re.match(r"##### ",linea):
			if enlista == True:
				print("---SE SALIO EN LA LISTA---")
				enlista = False
				htmlContent+="		</ul>\n"
			print("Detectado: <h5>")
			linea = re.sub(r"##### ","",linea)
			htmlContent+="		<h5>"+linea+"</h5>\n"
			
		#Titulo 6
		elif re.match(r"###### ",linea):
			if enlista == True:
				print("---SE SALIO EN LA LISTA---")
				enlista = False
				htmlContent+="		</ul>\n"
			print("Detectado: <h6>")
			linea = re.sub(r"###### ","",linea)
			htmlContent+="		<h6>"+linea+"</h6>\n"
		
		###Separador
		elif re.match(r"---",linea):
			if enlista == True:
				print("---SE SALIO EN LA LISTA---")
				enlista = False
				htmlContent+="		</ul>\n"
			print("Detectado: <hr>")
			htmlContent+="		<hr>\n"
		
		#Blockquotes
		elif re.match(r"> ",linea):
			if enlista == True:
				print("---SE SALIO DE LA LISTA---")
				enlista = False
				htmlContent+="		</ul>\n"
			print("Detectado: <p> con estilo de blockquote")
			linea = re.sub(r"> ","",linea)
			htmlContent+="		<p class='blockquote'>"+linea+"</p>\n"
		
		###Lista desordenada
		elif re.match("\* ",linea):
			print("Detectado: <ul>")
			if enlista == False:
				print("---SE ENTRO EN LA LISTA---")
				enlista = True
				htmlContent+="		<ul>\n"
			print("Añadido <li>.")
			linea = re.sub("\* ","",linea)
			htmlContent+="		<li>"+linea+"</li>\n"
			
		###Bloque de codigo
		elif re.match("```",linea):
			print("Detectado: <div> con estilo de codigo")
			if encodigo == False:
				encodigo = True
				print("---SE ENTRO EN EL CODIGO---")
				htmlContent+="		<div class='code'>"
			else:
				encodigo = False
				print("---SE SALIO DE EL CODIGO---")
				htmlContent+="		</div>"
				
		
		#IMAGENES!!!!!!!!!!!!!!!!1
		elif re.match(r"\!\[.*\]\(.*\)",linea):
			if enlista == True:
				print("---SE SALIO EN LA LISTA---")
				enlista = False
				htmlContent+="		</ul>\n"
			print("Detectado: <img>")
			ruta = re.sub(r"\!\[.*\]\(","",linea)
			ruta = re.sub("\)","",ruta)
			
			alt = re.sub(r"\!\[","",linea)
			alt = re.sub("\]\(.*\)","",alt)
			
			htmlContent+="		<img src='"+ruta+"' alt='"+alt+"'>\n"
			
			
		#Links separados
		
		elif re.match(r"\[.*\]\(.*\)",linea):
			if enlista == True:
				print("---SE SALIO EN LA LISTA---")
				enlista = False
				htmlContent+="		</ul>\n"
			print("Detectado: <a>")
			ruta = re.sub(r"\[.*\]\(","",linea)
			ruta = re.sub("\)","",ruta)
			
			txt = re.sub(r"\[","",linea)
			txt = re.sub("\]\(.*\)","",txt)
			
			htmlContent+="		<a href='"+ruta+"'>"+txt+"</a>\n"
		
		###Cosas que se detectan en una linea.
		
		
		
		
		
		else:
			i = 0
			lineaaponer = ""
			algo = False
			ennegrita = False
			encursiva = False
			encodeline = False
			while i < len(linea):	
				#Cursivas
				if linea[i] == "_":
					print("Detectado: <i>")
					if encursiva == False:
						print("Abriendo <i>")
						lineaaponer +="<i>"
						encursiva = True
					elif encursiva == True:
						print("Cerrando <i>")
						lineaaponer +="</i>"
						encursiva = False
				#Lineas de codigo
				elif linea[i] == "`":
					print("Detectado: <span> con estilo de codigo")
					if encursiva == False:
						print("Abriendo <span>")
						lineaaponer +="<span style='background-color:#000;color:#FFF;font-family:monospace;padding:2px;'>"
						encursiva = True
					elif encursiva == True:
						print("Cerrando <span>")
						lineaaponer +="</span>"
						encursiva = False
				#Negritas
				elif linea[i] == "*" and linea[i+1] == "*":
					print("Detectado: <b>")
					i+=1
					if encursiva == False:
						print("Abriendo <b>")
						lineaaponer +="<b>"
						encursiva = True
					elif encursiva == True:
						print("Cerrando <b>")
						lineaaponer +="</b>"
						encursiva = False
				else:
					lineaaponer+=linea[i]
				i+=1
			if enlista == True:
				print("---SE SALIO EN LA LISTA---")
				enlista = False
				htmlContent+="		</ul>\n"
			print("Detectado: <p>")
			htmlContent+="		<p>"+lineaaponer+"</p>\n"
			
			
	#Cierra <body> y cierra <html>
	
	htmlContent+='''</body>
</html>'''
	
	#Ahora a guardar el archivo!!!
	
	saveRoot = filedialog.asksaveasfilename(filetypes=[('HTML file', '*.html *.htm'), ('Plain text file', '*.txt')])
	
	saveFile = open(saveRoot, "w")
	
	saveFile.write(htmlContent)
	
	saveFile.close()
	
	print("Archivo HTML guardado en {}".format(saveRoot))
	
	print("Fin del proceso.\n=====================================================")
	
	#Finish
	
	
def load():
	fileroot = filedialog.askopenfilename(filetypes = (("MarkDown file","*.md"),("Plain text file","*.txt")))
	print("Ruta del archivo a cargar: {}".format(fileroot))
	rootlabel["text"] = fileroot
	return fileroot
	
def save():
	print("Save")


	
def aboutPress(abt):
	print("About "+str(abt))

#Setting vars
about = ["Help","Credits"]
fonts = ["Georgia, serif",
"\"Palatino Linotype\", \"Book Antiqua\", Palatino, serif",
"\"Times New Roman\", Times, serif",
"Arial, Helvetica, sans-serif",
"\"Arial Black\", Gadget, sans-serif",
"\"Comic Sans MS\", cursive, sans-serif",
"Impact, Charcoal, sans-serif",
"\"Lucida Sans Unicode\", \"Lucida Grande\", sans-serif",
"Tahoma, Geneva, sans-serif",
"\"Trebuchet MS\", Helvetica, sans-serif",
"Verdana, Geneva, sans-serif",
"\"Courier New\", Courier, monospace",
"\"Lucida Console\", Monaco, monospace"]



print("Inicializando ventana")
root = Tk()

fileroot = StringVar()
fileroot.set("No selected")

print("Construyendo...")
root.geometry("300x500")
root.resizable(False,False)
root.title("md2html")

title = Label(root, text = "md2htmk", font=("Helvetica",30))
title.pack()

Frame(root, width=400, height=5).pack()
Frame(root, width=400, height=2, relief=SUNKEN, bd=1).pack()
Frame(root, width=400, height=5).pack()

Label(root,text="MarkDown file:").pack()

rootlabel = Label(root,text="No selected")
rootlabel.pack()

rootbutton = Button(root, text="Select File", command=lambda: fileroot.set(load()))
rootbutton.pack()

Frame(root, width=400, height=5).pack()
Frame(root, width=400, height=2, relief=SUNKEN, bd=1).pack()
Frame(root, width=400, height=5).pack()

Label(root,text="Options:", font=("Helvetica",20)).pack()

Label(root,text="Tab title:").pack()

tabtitleEntry = Entry(root)
tabtitleEntry.pack()

Label(root,text="Background color (in hexadecimal or english word):").pack()

bgcolorEntry = Entry(root)
bgcolorEntry.pack()

Label(root,text="Text color:").pack()

txtcolorEntry = Entry(root)
txtcolorEntry.pack()

Label(root,text="Font:").pack()

fEntry = StringVar()
fEntry.set("\"Palatino Linotype\", \"Book Antiqua\", Palatino, serif")

w = OptionMenu(root, fEntry, "Georgia, serif",
"\"Palatino Linotype\", \"Book Antiqua\", Palatino, serif",
"\"Times New Roman\", Times, serif",
"Arial, Helvetica, sans-serif",
"\"Arial Black\", Gadget, sans-serif",
"\"Comic Sans MS\", cursive, sans-serif",
"Impact, Charcoal, sans-serif",
"\"Lucida Sans Unicode\", \"Lucida Grande\", sans-serif",
"Tahoma, Geneva, sans-serif",
"\"Trebuchet MS\", Helvetica, sans-serif",
"Verdana, Geneva, sans-serif",
"\"Courier New\", Courier, monospace",
"\"Lucida Console\", Monaco, monospace")
w.pack()

Label(root,text="Font size:").pack()

fsizeEntry = Entry(root)
fsizeEntry.pack()

Label(root,text="Quotes background color:").pack()

qbgcolorEntry = Entry(root)
qbgcolorEntry.pack()

Frame(root, width=400, height=5).pack()
Frame(root, width=400, height=2, relief=SUNKEN, bd=1).pack()
Frame(root, width=400, height=5).pack()

convertbutton = Button(root, text="Convert", command = lambda: convert(fileroot.get(),tabtitleEntry.get(),bgcolorEntry.get(),txtcolorEntry.get(),qbgcolorEntry.get(),fsizeEntry.get(),fEntry.get()))
convertbutton.pack()

print("mainloop")
root.mainloop()