import os
import subprocess

def desativar_inicializacao_automatica():
    # Lista de programas para desativar a inicialização automática
    programas = ["programa1.exe", "programa2.exe", "programa3.exe"]

    for programa in programas:
        subprocess.run(["reg", "delete", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "/v", programa, "/f"])

def limpar_arquivos_temporarios():
    # Limpar arquivos temporários
    subprocess.run(["del", "/q", "C:\\Windows\\Temp\\*.*"], shell=True)
    subprocess.run(["del", "/q", "C:\\Users\\<Seu_Usuário>\\AppData\\Local\\Temp\\*.*"], shell=True)

def main():
    desativar_inicializacao_automatica()
    limpar_arquivos_temporarios()
    print("Tarefas de otimização concluídas.")

if __name__ == "__main__":
    main()