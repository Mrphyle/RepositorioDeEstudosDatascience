import streamlit as st
import pandas as pd
import openpyxl as px
sheetinport = r"C:\Users\diego.sgoncalves10\Documents\GitHub\RepositorioDeEstudosDatascience\2025 files\vendaper vendedor\dados-normalizados.xlsx"
def read_exel_sheets():
    sheets1 = pd.read_excel(sheetinport, sheet_name="dEstado")
    sheet2 = pd.read_excel(sheetinport,sheet_name="fMovimentação")
    sheet3 = pd.read_excel(sheetinport,sheet_name="dVendedor")
    sheet4 = pd.read_excel(sheetinport,sheet_name="dProduto")
    return sheets1, sheet2, sheet3, sheet4
def redrect():
    dEstado, fMovimentacao, dVendedor, dProduto = read_exel_sheets()
    Estado = fMovimentacao['Codig_Estado'].map(dEstado.set_index('Codig_Estado')['Estado'])
    Vendedor = fMovimentacao['Codig_Vendedor'].map(dVendedor.set_index('Código_Vendedor')['Vemdedor'])
    Produto = fMovimentacao['Codig_'].map(dProduto.set_index('Codig_Produto')['Produto'])
    return fMovimentacao 
    