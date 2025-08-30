# ---- 1. Estágio de Base: Imagem Python ----
# Começamos com uma imagem oficial do Python. A versão 'slim' é mais leve,
# o que resulta numa imagem final mais pequena e segura.
FROM python:3.11-slim

# ---- 2. Configuração do Ambiente ----
# Define o diretório de trabalho dentro do container.
# Todos os comandos a seguir serão executados a partir deste diretório.
WORKDIR /app

# Define variáveis de ambiente para otimizar o Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ---- 3. Instalação de Dependências ----
# Copiamos primeiro o ficheiro de requisitos para dentro do container.
# Esta é uma otimização de cache do Docker. Se este ficheiro não mudar,
# o Docker reutiliza o 'layer' com as dependências já instaladas,
# tornando os builds futuros muito mais rápidos.
COPY requirements.txt .

# Instala as dependências Python. A flag --no-cache-dir reduz o tamanho da imagem.
# Adicionamos --extra-index-url para apontar para o repositório de CPU do PyTorch,
# o que resolve o erro de não encontrar a versão "torch==...+cpu".
RUN pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt

# ---- 4. Cópia do Código da Aplicação ----
# Agora, copiamos o código fonte da nossa aplicação para o diretório de trabalho.
COPY ./app ./app

# ---- 5. Exposição da Porta ----
# Informa ao Docker que o container vai ouvir na porta 8000 em tempo de execução.
EXPOSE 8000

# ---- 6. Comando de Execução ----
# Este é o comando que será executado quando o container iniciar.
# - "app.main:app": Aponta para o objeto 'app' no ficheiro 'app/main.py'.
# - "--host 0.0.0.0": Essencial para que a API seja acessível de fora do container.
# - "--port 8000": A porta que definimos em EXPOSE.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
