import time
import sys

# Caminho padrão do sensor RAPL no Linux (CPU)
RAPL_PATH = "/sys/class/powercap/intel-rapl:0/energy_uj"

# --- CONFIGURAÇÃO ---
# Coloque aqui o valor do kWh da sua conta de luz (em Reais).
# A média no Brasil costuma ser em torno de R$ 0.85 a R$ 1.10 com taxas.
PRECO_KWH = 0.90 
# --------------------

def ler_energia_microjoules():
    try:
        with open(RAPL_PATH, 'r') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        print("\nErro: Sensor RAPL não encontrado.")
        print("Seu processador pode não suportar essa leitura ou o módulo não está carregado.")
        sys.exit(1)
    except PermissionError:
        print("\nErro: Sem permissão para ler o sensor.")
        print("Tente rodar o script como administrador usando: sudo python3 medidor_energia.py")
        sys.exit(1)

def main():
    print("Iniciando monitoramento de energia do Processador...")
    print(f"Tarifa configurada: R$ {PRECO_KWH:.2f} por kWh\n")
    print("Pressione Ctrl+C para parar.\n")
    
    ultima_energia = ler_energia_microjoules()
    total_kwh = 0.0

    try:
        while True:
            # Espera exatamente 1 segundo entre as leituras
            time.sleep(1) 
            energia_atual = ler_energia_microjoules()

            # O contador do Linux pode zerar quando atinge o limite máximo (wrap-around)
            if energia_atual < ultima_energia:
                delta_uj = energia_atual
            else:
                delta_uj = energia_atual - ultima_energia

            # 1 Joule = 1 Watt por segundo. 
            # Como a leitura é em microjoules e esperamos 1 segundo, a conversão direta é:
            watts_atuais = delta_uj / 1_000_000.0

            # 1 kWh = 3.6 * 10^12 microjoules
            kwh_neste_segundo = delta_uj / 3_600_000_000_000.0
            total_kwh += kwh_neste_segundo
            
            custo_total = total_kwh * PRECO_KWH

            # Atualiza a mesma linha no terminal para ficar limpo
            sys.stdout.write(f"\rConsumo Atual: {watts_atuais:5.2f} W | Acumulado: {total_kwh:.8f} kWh | Custo: R$ {custo_total:.6f}")
            sys.stdout.flush()

            ultima_energia = energia_atual

    except KeyboardInterrupt:
        print("\n\nMonitoramento encerrado.")
        print(f"Gasto final acumulado: {total_kwh:.6f} kWh (R$ {custo_total:.4f})")

if __name__ == "__main__":
    main()