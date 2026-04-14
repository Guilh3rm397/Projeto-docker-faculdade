## 📚 Projeto MongoDB com PyMongo + Docker
## 📌 Descrição

Este projeto demonstra operações básicas de banco de dados utilizando MongoDB com Python (PyMongo), executando o banco através de Docker.

São realizadas operações de:
```bash
Inserção de dados
Consulta
Atualização
Remoção
Agregação
⚙️ Tecnologias utilizadas
Python
MongoDB
PyMongo
Docker
Docker Compose
📁 Estrutura do projeto
📦 projeto
 ┣ 📜 docker-compose.yaml
 ┣ 📜 main_insert.py
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
🚀 Como executar o projeto
1. Subir o MongoDB com Docker
docker-compose up -d
2. Instalar dependências do Python
pip install -r requirements.txt
3. Executar o script
python main_insert.py
🗄️ Estrutura dos dados

Cada aluno possui a seguinte estrutura:

{
  "nome": "João",
  "idade": 20,
  "curso": "ADS",
  "notas": [7, 8, 9],
  "endereco": {
    "cidade": "Maricá",
    "estado": "RJ"
  }
}
🔍 Operações realizadas
📥 Inserção
Inserção de múltiplos alunos na coleção alunos
🔎 Consultas
Listar todos os alunos
Filtrar alunos por curso
Buscar alunos com idade maior que 21
✏️ Atualizações
Atualizar idade de um aluno
Adicionar nova nota a um aluno
❌ Remoção
Remover um aluno da coleção
📊 Agregações
Calcular média das notas por aluno
Contar quantidade de alunos por curso
🔌 Conexão com o banco

A aplicação se conecta ao MongoDB através da seguinte URI:

MongoClient("mongodb://localhost:27017/")
💡 Observações
O banco de dados e a coleção são criados automaticamente
O MongoDB roda em container Docker
Caso execute o script mais de uma vez, os dados serão duplicados
```
👨‍💻 Autor

Guilherme Ramos Rangel
