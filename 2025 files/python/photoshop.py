from PIL import Image, ImageDraw, ImageFont
background= Image.new('RGB', (1345, 900), "white")
imginport1= Image.open(r"/home/mrphyle/Área de trabalho/RepositorioDeEstudosDatascience/2025 files/wetransfer-3f2d68/Mostruario 15 anos/Laminas festa/mostruario_30x30_01.jpg")
imginport2 = Image.open(r"/home/mrphyle/Área de trabalho/RepositorioDeEstudosDatascience/2025 files/wetransfer-3f2d68/Mostruario 15 anos/Laminas/mostruario__10.jpg")
resized_img1= imginport1.resize((300,200))
resized_img2= imginport2.resize((300,200))
background.paste(resized_img1, (1000, 250))
background.paste(resized_img2, (1000, 450))
background.show()