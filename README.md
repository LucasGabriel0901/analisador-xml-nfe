# 🚀 Analisador e Processador de Notas Fiscais Eletrônicas (NFe)

Este projeto é uma aplicação web construída com **Django (Python)**, projetada para processar, analisar e persistir dados de Notas Fiscais Eletrônicas (NFe) formatadas em XML. O sistema foi desenvolvido com foco em eficiência de *parsing* e infraestrutura de produção, sendo hospedado no **Azure App Service**.

## ✨ Funcionalidades

* **Upload de Arquivo:** Interface web com design *Dark Mode* (Bootstrap) para upload de arquivos.
* **Processamento XML:** Utiliza a biblioteca `xml.etree.ElementTree` para realizar o *parsing* (extração) de dados estruturados da NFe (CNPJ, valores, itens, etc.).
* **Persistência de Dados:** Modelagem e salvamento dos dados extraídos em um banco de dados relacional (SQLite/PostgreSQL).
* **Ambiente de Produção:** Configurado para *Continuous Deployment* no Azure App Service (Linux + Python).

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia | Uso |
| :--- | :--- | :--- |
| **Backend/Web** | Python, Django | Framework MVT para desenvolvimento rápido e seguro. |
| **Parsing de Dados**| `xml.etree.ElementTree` | Extração e estruturação dos dados fiscais do XML. |
| **Banco de Dados** | SQLite (Desenvolvimento) | Persistência dos modelos (Empresa, NotaFiscal, Item). |
| **Frontend/Estilo** | HTML, CSS, Bootstrap 5 | Interface moderna, responsiva e com tema escuro. |
| **Infraestrutura** | Azure App Service (Linux) | Hospedagem em ambiente de produção com *deployment* contínuo. |

## ⚙️ Configuração e Instalação Local

Siga estes passos para configurar e rodar a aplicação em sua máquina local.

### Pré-requisitos

* Python (Recomendado: 3.10 ou superior)
* Pip ou Conda (Para gestão de ambientes)
* Git

### 1. Clonar o Repositório

```bash
git clone [https://docs.github.com/pt/repositories/creating-and-managing-repositories/quickstart-for-repositories](https://docs.github.com/pt/repositories/creating-and-managing-repositories/quickstart-for-repositories)
cd sistema_xml
