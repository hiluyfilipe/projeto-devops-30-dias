# imagem base
FROM python:3.9

# diretório de trabalho
WORKDIR /app

# copia arquivos
COPY . .

# instala dependências
RUN pip install -r requirements.txt

# executa aplicação
CMD ["python", "app.py"]
