# Decision Match AI 🤖

## 📝 Descrição do Projeto

Este projeto foi desenvolvido como solução para o **Datathon Decision**, um desafio focado em aplicar Inteligência Artificial para otimizar os processos de recrutamento e seleção da empresa Decision, uma especialista em bodyshop de TI.

O principal desafio da Decision é encontrar o talento ideal para cada vaga de forma ágil e precisa. O processo atual, embora robusto, enfrenta dores como a falta de padronização em entrevistas e a dificuldade em escalar a análise de um grande volume de candidatos, o que pode levar à perda de talentos e a um tempo de contratação elevado.

A solução proposta é o **Decision Match AI**, um MVP (Minimum Viable Product) de um sistema de recomendação inteligente. A ferramenta utiliza um modelo de Machine Learning para analisar o perfil de um candidato em relação a uma vaga e gerar um **"score de compatibilidade"**. O objetivo é ranquear os candidatos, permitindo que o time de recrutadores foque seu tempo e energia nos perfis mais promissores, otimizando todo o fluxo de seleção.

O modelo foi treinado com uma base de dados real da Decision, aprendendo a identificar os padrões que diferenciam os candidatos contratados dos demais.

## 🛠️ Stack Utilizada

* **Linguagem:** Python 3
* **Análise e Processamento de Dados:** Pandas, NumPy
* **Machine Learning:** Scikit-learn, XGBoost
* **Web App (Dashboard):** Streamlit
* **Visualização de Dados:** Matplotlib, Seaborn
* **Serialização do Modelo:** Joblib

## 📂 Estrutura do Repositório

O projeto está organizado da seguinte forma para garantir a manutenibilidade e reprodutibilidade:

├── app/
│   └── app.py                  # Script principal da aplicação com Streamlit
├── data/
│   ├── raw/                    # Onde os dados brutos em JSON devem ser colocados
│   │   ├── vagas.json
│   │   ├── prospects.json
│   │   └── Applicants.json (ou a amostra)
│   └── processed/              # Arquivos intermediários gerados pelo pipeline
│       ├── dados_consolidados.json
│       └── dados_com_features.json
├── images/
│   └── matriz_confusao.png     # Imagem da matriz de confusão gerada no treino
├── models/
│   └── modelo_decision_match_ai.joblib # Modelo treinado e serializado
├── notebooks/
│   ├── 1_Data_Processing.ipynb     # Notebook da Etapa 1
│   ├── 2_Feature_Engineering.ipynb # Notebook da Etapa 2
│   └── 3_Model_Training.ipynb      # Notebook da Etapa 3
├── README.md                     # Documentação do projeto
└── requirements.txt              # Bibliotecas e versões para o ambiente


## ⚙️ Instruções de Instalação

Para executar este projeto localmente, siga os passos abaixo.

**1. Pré-requisitos:**
* Ter o [Python 3.8+](https://www.python.org/downloads/) instalado.
* Ter o `pip` (gerenciador de pacotes do Python) instalado.

**2. Clone o Repositório:**
```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd SEU_REPOSITORIO
3. Crie um Ambiente Virtual (Recomendado):
Isso isola as dependências do projeto.

Bash

# Para Windows
python -m venv venv
venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
4. Instale as Dependências:
O arquivo requirements.txt contém todas as bibliotecas necessárias.

Bash

pip install -r requirements.txt
▶️ Como Rodar a Aplicação
Com o ambiente configurado, você pode iniciar a aplicação Streamlit.

Certifique-se de que o modelo treinado (modelo_decision_match_ai.joblib) está no diretório models/.

Execute o comando abaixo na raiz do projeto:

Bash

streamlit run app/app.py
A aplicação será aberta automaticamente no seu navegador.

🧠 Como Treinar o Modelo Novamente
Para re-executar o pipeline de treinamento e gerar um novo modelo, siga estes passos:

1. Prepare os Dados:

Coloque os arquivos de dados brutos (vagas.json, prospects.json, e Applicants_amostra.json ou o Applicants.json completo) no diretório data/raw/.

2. Execute os Notebooks Jupyter:

É recomendado usar o Jupyter Notebook ou JupyterLab para executar os scripts de forma interativa.

Execute os notebooks na seguinte ordem, pois eles são sequenciais:

notebooks/1_Data_Processing.ipynb: Para ler os dados brutos, consolidá-los e salvar dados_consolidados.json.

notebooks/2_Feature_Engineering.ipynb: Para carregar os dados consolidados, criar as features de compatibilidade e salvar dados_com_features.json.

notebooks/3_Model_Training.ipynb: Para carregar os dados com features, treinar os modelos, selecionar o melhor e salvar o artefato final (modelo_decision_match_ai.joblib) no diretório models/.