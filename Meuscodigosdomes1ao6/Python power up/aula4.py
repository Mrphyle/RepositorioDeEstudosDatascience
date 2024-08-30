import flet as ft
import mysql.connector as sqc
#Titulo Registro de produto
def main(pag):
    #Titulo Registro de produto
    Title =ft.Text("Rigistro de produtos da Bookencadernadora")
    pag.add(Title)
    #Nome do produto
    ProdutoNome = ft.TextField(label="Nome do produto")
    ProdutoNome.value
    pag.add(ProdutoNome)
    #adicionar nova categoria
    Addcat = ft.TextField(label="Quer adicionar uma nova categoria?" )
    catlist = ['Album','Pendrive']
    catlist.append(Addcat.value)
    #categoria
    Categoria= ft.TextField(label="Categoria" )
    catlist = ['Album','Pendrive']
    #adicionar nova categoria
    catlist.append(Addcat.value)
    catlistp = ft.Text(catlist)
    pag.update()
    pag.add(Addcat)
    pag.add(catlistp,Categoria)
    #valor
    #enviar tudo para um banco de dados
    enviarbut = ft.ElevatedButton("Enviar")
    
ft.app(main)#,view=ft.WEB_BROWSER)