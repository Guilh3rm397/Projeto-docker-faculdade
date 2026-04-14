from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["escola"]
alunos = db["alunos"]

alunos.insert_many([
    {
        "nome": "João",
        "idade": 20,
        "curso": "ADS",
        "notas": [7, 8, 9],
        "endereco": {"cidade": "Maricá", "estado": "RJ"}
    },
    {
        "nome": "Maria",
        "idade": 22,
        "curso": "ADS",
        "notas": [8, 9, 10],
        "endereco": {"cidade": "Niterói", "estado": "RJ"}
    },
    {
        "nome": "Pedro",
        "idade": 19,
        "curso": "Engenharia",
        "notas": [6, 7, 8],
        "endereco": {"cidade": "São Gonçalo", "estado": "RJ"}
    },
    {
        "nome": "Ana",
        "idade": 23,
        "curso": "ADS",
        "notas": [9, 9, 10],
        "endereco": {"cidade": "Maricá", "estado": "RJ"}
    },
    {
        "nome": "Lucas",
        "idade": 21,
        "curso": "Ciência da Computação",
        "notas": [5, 6, 7],
        "endereco": {"cidade": "Rio de Janeiro", "estado": "RJ"}
    }
])

for aluno in alunos.find():
    print(aluno)

for aluno in alunos.find({"curso": "ADS"}):
    print(aluno)

for aluno in alunos.find({"idade": {"$gt": 21}}):
    print(aluno)

alunos.update_one(
    {"nome": "João"},
    {"$set": {"idade": 21}}
)

alunos.update_one(
    {"nome": "Maria"},
    {"$push": {"notas": 10}}
)

alunos.delete_one({"nome": "Lucas"})

for aluno in alunos.aggregate([
    {
        "$project": {
            "nome": 1,
            "media": {"$avg": "$notas"}
        }
    }
]):
    print(aluno)

for curso in alunos.aggregate([
    {
        "$group": {
            "_id": "$curso",
            "quantidade": {"$sum": 1}
        }
    }
]):
    print(curso)