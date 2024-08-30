'''import datetime
def dateweekdayclock():
    WeekDays = ['SUN','MON','THE','WED','THE','FRI','SAT']
    Now = datetime.datetime.now()
    formatdate = Now.strftime("%Y-%m-%d")
    nownumber = now.weekday()'''
import datetime
import time
import tkinter as tk

def formatar_data_hora():
    # Lista de abreviações personalizadas para os dias da semana
    abreviacoes_dias_semana = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    # Função para atualizar o relógio
    def atualizar_relogio():
        # Obter a data e hora atual
        agora = datetime.datetime.now()
        
        # Formatar a data no formato "YYYY-MM-DD"
        data_formatada = agora.strftime("%Y-%m-%d")
        
        # Obter o dia da semana como um número (0 = segunda-feira, 6 = domingo)
        dia_semana_numero = agora.weekday()
        
        # Obter a abreviação do dia da semana usando a lista personalizada
        dia_semana = abreviacoes_dias_semana[dia_semana_numero].upper()
        
        # Formatar a hora no formato de 12 horas com "AM" ou "PM"
        hora_formatada = agora.strftime("%I:%M:%S %p")
        
        # Combinar todas as partes formatadas em uma string
        relogio_formatado = f"{data_formatada} {dia_semana}\n{hora_formatada}"
        
        # Atualizar o texto na janela
        label_relogio.config(text=relogio_formatado)
        
        # Agendar a próxima atualização após 1 segundo
        janela.after(1000, atualizar_relogio)
    
    # Criar a janela
    janela = tk.Tk()
    janela.title("Relógio")
    
    # Criar um rótulo para exibir o relógio
    label_relogio = tk.Label(janela, font=("Arial", 14))
    label_relogio.pack(padx=10, pady=10)
    
    # Chamar a função para iniciar o relógio
    atualizar_relogio()
    
    # Iniciar o loop principal da janela
    janela.mainloop()

# Chamar a função para iniciar o relógio
formatar_data_hora()