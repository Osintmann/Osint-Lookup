import requests
import os
import time
import json
import shutil
from colorama import Fore, Style, init

init(autoreset=True)

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")  # Funciona em Windows e Linux/Termux

def centralizar_arte(arte):
    """Centraliza qualquer arte ASCII em qualquer terminal"""
    # Pega o tamanho atual do terminal
    tamanho = shutil.get_terminal_size()
    largura = tamanho.columns
    
    # Divide a arte em linhas
    linhas = arte.strip("\n").split("\n")
    
    # Se o terminal for muito pequeno, mostra sem centralizar
    if largura <= 50:  # Largura mínima razoável
        for linha in linhas:
            print(linha)
        return
    
    # Calcula o espaçamento para centralizar cada linha
    for linha in linhas:
        espacos = (largura - len(linha)) // 2
        print(" " * max(0, espacos) + Fore.RED + linha)

# Arte com a URL já incluída
abertura = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⡶⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⠶⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⡿⣿⣦⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⣿⢏⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢎⠻⣿⣷⡄⠀⠀
⠀⠀⠀⠀⠀⣰⣿⣻⠃⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⢹⣿⣿⡄⠀
⠀⠀⠀⠀⢰⣿⣟⡗⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠐⣛⣿⣿⠀
⠀⠀⠀⠀⢸⣿⣿⡓⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠠⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠇⠐⣻⣿⣿⡆
⠀⠀⠀⠀⢸⣿⣿⡷⠖⠋⠻⣄⠀⠀⣀⣤⠶⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢦⣄⡀⠀⢀⣴⠏⠈⠲⢿⣿⣿⠇
⠀⠀⠀⠀⠸⣿⣿⣿⣧⠞⠁⠈⠻⢾⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣻⡷⠋⡁⠈⢦⣾⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠹⣿⣿⣷⣷⡴⠃⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠱⣴⣷⣯⣿⡿⠃⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣿⣯⣾⣿⢗⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⢾⣿⣮⣿⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠳⣽⣿⣿⡍⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢸⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠘⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⢄⣿⡰⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⢸⣇⠀⢀⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣾⣿⠇⠹⣶⣤⣀⣀⠀⠙⢶⣤⡀⠀⠀⠀⣠⣴⠖⠉⢀⣀⣠⣴⡾⠁⢿⣿⡆⢸⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⣿⠏⢠⣾⣿⣿⣿⣿⣿⣦⡀⠹⡿⠀⠀⠸⡿⠁⣤⣾⣿⣿⣿⣿⣷⣦⠀⢿⡇⡸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⢿⡀⢸⣿⣿⣿⣿⣿⣿⣿⡟⠆⠀⠀⠀⠀⠀⠞⣿⣿⣿⣿⣿⣿⣿⣿⠀⣸⢧⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢈⡷⠈⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣠⣤⡀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠃⠀⣏⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⠀⠀⠀⠙⠻⠿⠿⠿⠟⠁⠀⢠⣿⣿⣧⠀⠀⠙⠿⠿⠿⠿⠛⠁⠀⠀⠀⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⢻⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⡿⢸⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⢛⣿⣿⣿⡖⠦⡀⠀⠀⠉⠁⠀⠉⠁⠀⠀⢠⠖⣾⣿⣿⣿⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⣿⢻⣿⣴⣠⢀⠀⡄⠀⡀⢀⡄⢀⣀⣼⣼⣿⠹⡇⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠧⡇⢸⣿⣿⡇⢹⠒⡟⠙⡟⠉⡗⢹⠁⣿⣿⣿⠀⡧⠇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠘⢿⣹⠛⠼⣦⣿⣄⣧⣀⣷⣾⠴⢻⣸⠟⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⡀⠀⠀⠊⠳⠧⣼⣠⣤⣧⣱⣸⡦⠷⠚⠃⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⣤⡀⠀⠀⠀⠈⠀⠀⠈⠀⠀⠀⠀⣠⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⣄⣠⣴⣶⣤⣄⣰⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠀⠀⠀⠀⠀⠀⠀⠀
                           https://github.com/Osintmann
"""

def logo():
    print(Fore.RED + r"""   ____       _       __        __            __             
  / __ \_____(_)___  / /_      / /___  ____  / /____  ______ 
 / / / / ___/ / __ \/ __/_____/ / __ \/ __ \/ //_/ / / / __ \
/ /_/ (__  ) / / / / /_/_____/ / /_/ / /_/ / ,< / /_/ / /_/ /
\____/____/_/_/ /_/\__/     /_/\____/\____/_/|_|\__,_/ .___/ 
                                                    /_/       by: OSINTMANN""")

def menu():
    print(Fore.RED + r"""==============================================
               OSINT-LOOKUP
==============================================
- 1 - IP LOOKUP (IP Lookup)
- 2 - Buscar CEP (Search ZIP Code)
- 3 - SOBRE A FERRAMENTA (About)
- 0 - SAIR (Exit)
==============================================
""")

if __name__ == "__main__":

    limpar_tela()
    centralizar_arte(abertura)  # Caveira centralizada em qualquer dispositivo!
    time.sleep(3.1)

    while True:
        limpar_tela()
        time.sleep(2.1)
        logo()
        time.sleep(2.1)
        menu()
        
        try:
            opc = int(input(Fore.RED + r"""┌──[🌐 OSINTMANN@MENU]─[~]
└─$: """))
        except ValueError:
            print(Fore.RED + "❌ Opção inválida! Digite apenas números.")
            time.sleep(2)
            continue

        if opc == 1:
            limpar_tela()
            time.sleep(2.1)
            print(Fore.RED + r"""╔══════════════════════════════════════════╗
║         🔍 CONSULTA DE IP                ║
╚══════════════════════════════════════════╝""")

            ip_usuario = input(Fore.RED + r"""┌──[🌐 OSINTMANN@IP-LOOKUP]─[~]
└─$ Digite o IP alvo (Enter para auto-detecção): """)
            
            if ip_usuario.strip() == "":
                ip_usuario = ""  # IP vazio = IP da própria conexão
            
            print(Fore.RED + 'Buscando...🔎')
            time.sleep(2)

            url = f"https://ipinfo.io/{ip_usuario}/json"

            try:
                response = requests.get(url)
                response.raise_for_status()
                dados = response.json()

                print(Fore.RED + f"\n📍 INFORMAÇÕES DO IP: {ip_usuario if ip_usuario else 'SEU IP'}")
                print(Fore.RED + "-" * 50)
                print(Fore.RED + f"IP: {dados.get('ip', 'N/A')}")
                print(Fore.RED + f"Hostname: {dados.get('hostname', 'N/A')}")
                print(Fore.RED + f"Cidade: {dados.get('city', 'N/A')}")
                print(Fore.RED + f"Região: {dados.get('region', 'N/A')}")
                print(Fore.RED + f"País: {dados.get('country', 'N/A')}")
                print(Fore.RED + f"Localização (lat,lon): {dados.get('loc', 'N/A')}")
                print(Fore.RED + f"Organização: {dados.get('org', 'N/A')}")
                print(Fore.RED + f"CEP: {dados.get('postal', 'N/A')}")
                print(Fore.RED + f"Timezone: {dados.get('timezone', 'N/A')}")

            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"❌ Erro na requisição: {e}")
            except json.JSONDecodeError as e:
                print(Fore.RED + f"❌ Erro ao decodificar JSON: {e}")

            # CONTINUA FORA DO TRY/EXCEPT
            continua = input(Fore.RED + '\nDeseja continuar (S/N): ').strip().upper()
            if continua == 'S':
                continue
            elif continua == 'N':
                break
            else:
                print(Fore.RED + 'Opção inválida')
                time.sleep(1)
                continue

        elif opc == 2:
            limpar_tela()
            time.sleep(2.1)

            print(Fore.RED + r"""╔══════════════════════════════════════════╗
║         📮 CONSULTA DE CEP               ║
╚══════════════════════════════════════════╝""")

            cep = input(Fore.RED + r"""┌──[📮 OSINTMANN@CEP-LOOKUP]─[~]
└─$ Digite o CEP (Enter = 01452924): """)

            # Se vazio, usa exemplo
            if cep.strip() == "":
                cep = "01452924"
                print(Fore.RED + "[i] Usando CEP de exemplo")

            # Remove caracteres não numéricos
            cep = ''.join(filter(str.isdigit, cep))

            # Valida tamanho do CEP
            if len(cep) != 8:
                print(Fore.RED + f"\n❌ CEP inválido! Deve ter 8 dígitos (você digitou {len(cep)})")
                continua = input(Fore.RED + 'Deseja continuar (S/N): ').strip().upper()
                if continua == 'S':
                    continue
                elif continua == 'N':
                    break
                else:
                    print(Fore.RED + 'Opção inválida')
                    time.sleep(1)
                    continue

            print(Fore.RED + "[✓] Buscando endereço... 🔎")
            time.sleep(2)

            url = f"https://viacep.com.br/ws/{cep}/json/"

            try:
                response = requests.get(url)
                data = response.json()

                if "erro" in data:
                    print(Fore.RED + "\n❌ CEP não encontrado ou inválido!")
                else:
                    # APENAS A FORMA LIMPA (sem o JSON bruto)
                    print(Fore.RED + "\n" + "="*40)
                    print(Fore.RED + "📋 DADOS DO ENDEREÇO:")
                    print(Fore.RED + "="*40)
                    print(Fore.RED + f"Logradouro: {data.get('logradouro', 'N/A')}")
                    print(Fore.RED + f"Bairro: {data.get('bairro', 'N/A')}")
                    print(Fore.RED + f"Cidade: {data.get('localidade', 'N/A')}")
                    print(Fore.RED + f"Estado: {data.get('uf', 'N/A')}")
                    print(Fore.RED + f"CEP: {data.get('cep', 'N/A')}")
                    print(Fore.RED + f"DDD: {data.get('ddd', 'N/A')}")
                    print(Fore.RED + f"IBGE: {data.get('ibge', 'N/A')}")
                    print(Fore.RED + "="*40)

            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"\n❌ Erro na requisição: {e}")
            except Exception as e:
                print(Fore.RED + f"\n❌ Erro inesperado: {e}")

            # CONTINUA FORA DO TRY/EXCEPT
            continua = input(Fore.RED + '\nDeseja continuar (S/N): ').strip().upper()
            if continua == 'S':
                continue
            elif continua == 'N':
                break
            else:
                print(Fore.RED + 'Opção inválida')
                time.sleep(1)
                continue

        elif opc == 3:
            limpar_tela()
            time.sleep(2.1)
            print(Fore.RED + r"""┌────────────────────────────────────────────────────────────┐
│                  SOBRE A FERRAMENTA                        │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  OSINT-LOOKUP é uma ferramenta de consulta OSINT           │
│  (Open Source Intelligence) desenvolvida em Python,        │
│  focada em fornecer informações rápidas e precisas         │
│  através de APIs públicas gratuitas.                       │
│                                                            │
│  📌 FUNCIONALIDADES:                                       │
│  • Consulta de endereços IP com dados de geolocalização,   │
│    provedor e organização                                  │
│  • Busca de CEP com informações completas de endereço,     │
│    bairro, cidade e estado                                 │
│                                                            │
│  🛠️ TECNOLOGIAS UTILIZADAS:                                │
│  • Python 3                                                │
│  • Requests                                                │
│  • Colorama                                                │
│  • APIs gratuitas (ipinfo.io e ViaCEP)                     │
│                                                            │
│  🎯 OBJETIVO:                                              │
│  Oferecer uma solução simples, eficiente e de fácil        │
│  utilização para consultas OSINT, sem complicações ou      │
│  necessidade de cadastros.                                 │
│                                                            │
│  👨‍💻 DESENVOLVEDOR:                                         │
│  GitHub: https://github.com/Osintmann                      │
│                                                            │
│  📅 VERSÃO: 1.0.0                                          │
│                                                            │
│  ⭐ Se gostou da ferramenta, deixe uma estrela no           │
│     repositório!                                           │
│                                                            │
└────────────────────────────────────────────────────────────┘""")
            
            continua = input(Fore.RED + '\nDeseja continuar (S/N): ').strip().upper()
            if continua == 'S':
                continue
            elif continua == 'N':
                break
            else:
                print(Fore.RED + 'Opção inválida')
                time.sleep(1)
                continue

        elif opc == 0:
            print(Fore.RED + "\nSaindo... Até mais! 👋")
            time.sleep(2)
            limpar_tela()
            break

        else:
            print(Fore.RED + "❌ Opção inválida! Digite 0, 1, 2 ou 3.")
            time.sleep(2)
            continue
