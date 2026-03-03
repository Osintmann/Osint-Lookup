# 🕵️ OSINT-LOOKUP

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.6+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

Ferramenta de consulta OSINT (Open Source Intelligence) desenvolvida em Python para obtenção rápida de informações sobre IPs e CEPs brasileiros.

---

## 📋 Sobre o Projeto

O **OSINT-LOOKUP** é uma ferramenta simples e eficiente que permite consultar informações de geolocalização de IPs e dados detalhados de CEPs brasileiros utilizando APIs públicas gratuitas, sem necessidade de cadastro ou tokens de autenticação.
┌────────────────────────────────────────────────────────────┐
│ SOBRE A FERRAMENTA │
├────────────────────────────────────────────────────────────┤
│ │
│ OSINT-LOOKUP é uma ferramenta de consulta OSINT │
│ (Open Source Intelligence) desenvolvida em Python, │
│ focada em fornecer informações rápidas e precisas │
│ através de APIs públicas gratuitas. │
│ │
│ 📌 FUNCIONALIDADES: │
│ • Consulta de endereços IP com dados de geolocalização, │
│ provedor e organização │
│ • Busca de CEP com informações completas de endereço, │
│ bairro, cidade e estado │
│ │
│ 🛠️ TECNOLOGIAS UTILIZADAS: │
│ • Python 3 │
│ • Requests │
│ • Colorama │
│ • APIs gratuitas (ipinfo.io e ViaCEP) │
│ │
│ 🎯 OBJETIVO: │
│ Oferecer uma solução simples, eficiente e de fácil │
│ utilização para consultas OSINT, sem complicações ou │
│ necessidade de cadastros. │
│ │
│ 👨‍💻 DESENVOLVEDOR: │
│ GitHub: https://github.com/Osintmann │
│ │
│ 📅 VERSÃO: 1.0.0 │
│ │
│ ⭐ Se gostou da ferramenta, deixe uma estrela no │
│ repositório! │
│ │
└────────────────────────────────────────────────────────────┘

text

## ✨ Funcionalidades

### 🌐 IP LOOKUP
| Campo | Descrição |
|-------|-----------|
| **Geolocalização** | Cidade, estado e país |
| **Provedor** | Organização/ISP |
| **Coordenadas** | Latitude e longitude |
| **Fuso Horário** | Timezone local |
| **CEP** | Código postal associado |

### 📮 CEP LOOKUP
| Campo | Descrição |
|-------|-----------|
| **Logradouro** | Rua/Avenida |
| **Bairro** | Bairro da localidade |
| **Cidade/UF** | Município e estado |
| **DDD** | Código de área telefônico |

## 🚀 Como Usar

### Pré-requisitos
- Python 3.6 ou superior
- Pip (gerenciador de pacotes Python)

### Instalação Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/Osintmann/osint-lookup.git
cd osint-lookup
Instale as dependências

bash
pip install -r requirements.txt
Execute o programa

bash
python osint_lookup.py
📦 Dependências
Crie um arquivo requirements.txt com:

txt
requests==2.31.0
colorama==0.4.6
Para instalar:

bash
pip install -r requirements.txt
🎯 APIs Utilizadas
Serviço	Função	Endpoint
ipinfo.io	Geolocalização de IP	https://ipinfo.io/{ip}/json
ViaCEP	Consulta de CEP	https://viacep.com.br/ws/{cep}/json/
✅ Todas são gratuitas e sem necessidade de token!

🖥️ Interface do Programa
Menu Principal
text
   ____       _       __        __            __             
  / __ \_____(_)___  / /_      / /___  ____  / /____  ______ 
 / / / / ___/ / __ \/ __/_____/ / __ \/ __ \/ //_/ / / / __ \
/ /_/ (__  ) / / / / /_/_____/ / /_/ / /_/ / ,< / /_/ / /_/ /
\____/____/_/_/ /_/\__/     /_/\____/\____/_/|_|\__,_/ .___/ 
                                                    /_/       by: OSINTMANN

==============================================
               OSINT-LOOKUP
==============================================
- 1 - IP LOOKUP (IP Lookup)
- 2 - Buscar CEP (Search ZIP Code)
- 3 - SOBRE A FERRAMENTA (About)
- 0 - SAIR (Exit)
==============================================
IP Lookup
text
┌──[🌐 OSINTMANN@IP-LOOKUP]─[~]
└─$ Digite o IP alvo (Enter = auto): 8.8.8.8

📍 INFORMAÇÕES DO IP: 8.8.8.8
--------------------------------------------------
IP: 8.8.8.8
Hostname: dns.google
Cidade: Mountain View
Região: California
País: US
Localização: 37.4056,-122.0775
Organização: AS15169 Google LLC
CEP: 94043
Timezone: America/Los_Angeles
CEP Lookup
text
┌──[📮 OSINTMANN@CEP-LOOKUP]─[~]
└─$ Digite o CEP (Enter = 01452924): 01001000

📦 Dados do CEP:
{
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "complemento": "lado ímpar",
  "bairro": "Sé",
  "localidade": "São Paulo",
  "uf": "SP",
  "ibge": "3550308",
  "gia": "1004",
  "ddd": "11",
  "siafi": "7107"
}

📋 Resumo:
Logradouro: Praça da Sé
Bairro: Sé
Cidade: São Paulo
Estado: SP
DDD: 11
📁 Estrutura do Projeto
text
osint-lookup/
│
├── osint_lookup.py      # Script principal (código fonte)
├── requirements.txt     # Dependências do projeto
├── README.md           # Documentação (este arquivo)
└── LICENSE             # Licença do projeto
