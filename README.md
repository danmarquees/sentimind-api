

# Sentimind API 🧠
Um microsserviço de alta performance para análise de sentimento e sumarização de texto, construído com FastAPI e modelos de linguagem da Hugging Face. O projeto é focado na implementação de um ciclo de vida completo de MLOps, demonstrando práticas modernas de desenvolvimento, automação e deploy em nuvem.

✨ Funcionalidades
Core da API
Análise de Sentimento: Endpoint /analyze que classifica textos em 5 categorias (de "muito negativo" a "muito positivo").

Sumarização de Texto: (Em desenvolvimento) Endpoint /summarize para gerar resumos concisos de textos longos.

MLOps e DevOps
Containerização: Aplicação totalmente containerizada com Docker.

Integração Contínua (CI): Pipeline no GitHub Actions que roda testes e linters a cada push.

Deploy Contínuo (CD): Deploy automatizado no Google Cloud Run a cada merge na branch main.

Documentação Automática: Interface interativa (Swagger UI) gerada automaticamente pelo FastAPI.

🛠️ Stack de Tecnologias
Backend: FastAPI

Machine Learning: Hugging Face Transformers & PyTorch

Validação de Dados: Pydantic

Testes: Pytest

Containerização: Docker

CI/CD: GitHub Actions

Nuvem: Google Cloud Run

🚀 Como Executar Localmente
Siga os passos abaixo para ter a API rodando na sua máquina.

Pré-requisitos
Git

Python 3.9+

Docker (Opcional, para rodar com container)

1. Clonar o Repositório
git clone [https://github.com/danmarquees/sentimind-api.git](https://github.com/danmarquees/sentimind-api.git)
cd sentimind-api

2. Configurar o Ambiente Virtual
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate

3. Instalar as Dependências
Com o ambiente ativado, instale as bibliotecas necessárias.

pip install -r requirements.txt

4. Rodar a API
uvicorn app.main:app --reload

A API estará disponível em http://127.0.0.1:8000.

5. Acessar a Documentação Interativa
Abra seu navegador e acesse http://127.0.0.1:8000/docs para ver a interface do Swagger UI e testar os endpoints.

🐳 Rodando com Docker
Você também pode rodar a aplicação via Docker, o que simplifica o setup do ambiente.

Construir a imagem Docker:

docker build -t sentimind-api .

Executar o container:

docker run -p 8000:8000 sentimind-api

A API estará rodando em http://127.0.0.1:8000.

✅ Rodando os Testes
Para garantir que tudo está funcionando como esperado, execute a suíte de testes automatizados:

pytest

🗺️ Roadmap do Projeto
[x] Fase 1: MVP local com endpoint de análise e testes.

[ ] Fase 2: Configurar pipeline de CI com GitHub Actions.

[ ] Fase 3: Automatizar o deploy no Google Cloud Run.

[ ] Fase 4: Implementar o endpoint /summarize.

[ ] Fase 5: Gerenciar a infraestrutura na nuvem com Terraform (IaC).

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
