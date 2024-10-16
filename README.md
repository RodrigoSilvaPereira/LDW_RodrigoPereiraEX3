# API Rest com Flask - Carros

Este projeto é uma API REST para gerenciamento de carros, construída com Flask. A API permite realizar operações CRUD (Create, Read, Update e Delete) em um banco de dados MongoDB, utilizando **Flask-Restful**, **Flask-PyMongo**, e **Flask-Marshmallow** para facilitar a integração com o banco de dados e a serialização de dados.

## Funcionalidades
- Listar carros
- Adicionar novos carros
- Atualizar dados de carros
- Remover carros

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:
- Python 3.7+
- MongoDB

## Configuração do ambiente

### 1. Clonar o repositório

```bash
git clone https://github.com/RodrigoSilvaPereira/LDW_RodrigoPereiraEX3
cd LDW_RodrigoPereiraEX3
```

### 2. Criar o ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual - Windows

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar a API

```bash
python run.py
```

## Dependencias Principais

#### Flask-Restful: Extensão para criar APIs RESTful com Flask.

```bash
pip install flask-restful
```

#### Flask-PyMongo: Integração com MongoDB para operações CRUD.

```bash
pip install flask-pymongo
```

#### Flask-Marshmallow: Serialização e validação de dados.

```bash
pip install flask-marshmallow
```

# API Rest de Carros - Endpoints

## 1. Listar todos os carros

- **Método:** `GET`
- **Rota:** `/cars`
- **Descrição:** Retorna uma lista com todos os carros cadastrados.

### Exemplo de Resposta:

```json
[
  {
    "_id": "67093fd1c4935011d8a1fb38",
    "model": "Fusca",
    "specifications": {
      "color": "blue",
      "engine": "1.0L",
      "doors": 2
    },
    "year": 1975
  },
  {
    "_id": "67093fd1c4935011d8a1fb39",
    "model": "Civic",
    "specifications": {
      "color": "red",
      "engine": "2.0L",
      "doors": 4
    },
    "year": 2020
  }
]
```

## 2. Adicionar um carro

- **Método:** `POST`
- **Rota:** `/cars`
- **Descrição:** Adiciona um novo carro no banco de dados.
  
### Corpo da Requisição:

```json
{
  "model": "Fusca",
  "specifications": {
    "color": "blue",
    "engine": "1.0L",
    "doors": 2
  },
  "year": 1975
}
```

### Exemplo de Resposta:

```json
{
  "_id": "67093fd1c4935011d8a1fb38",
  "model": "Fusca",
  "specifications": {
    "color": "blue",
    "engine": "1.0L",
    "doors": 2
  },
  "year": 1975
}
```

## 3. Atualizar um carro

- **Método:** `PUT`
- **Rota:** `/car/<id>`
- **Descrição:** Atualiza os dados de um carro existente.
- **Parâmetros da URL:**
  - `id`: O ID do carro que será atualizado.
- **Corpo da Requisição:**

```json
{
  "model": "Corsa Atualizado",
  "specifications": {
    "color": "red",
    "engine": "1.6L",
    "doors": 2
  },
  "year": 1978
}
```

### Exemplo de Resposta:

```json
{
  "_id": "67093fd1c4935011d8a1fb38",
  "model": "Fusca",
  "specifications": {
    "color": "red",
    "engine": "1.6L",
    "doors": 2
  },
  "year": 1978
}
```

## 3. Atualizar um carro

- **Método:** `PUT`
- **Rota:** `/car/<id>`
- **Descrição:** Atualiza os dados de um carro existente.
- **Parâmetros da URL:**
  - `id`: O ID do carro que será atualizado.

### Corpo da Requisição:

```json
{
  "model": "Fusca",
  "specifications": {
    "color": "red",
    "engine": "1.6L",
    "doors": 2
  },
  "year": 1978
}
```

### Exemplo de resposta:

```json
{
  "_id": "67093fd1c4935011d8a1fb38",
  "model": "Fusca",
  "specifications": {
    "color": "red",
    "engine": "1.6L",
    "doors": 2
  },
  "year": 1978
}

```

## 4. Excluir um carro

- **Método:** `DELETE`
- **Rota:** `/car/<id>`
- **Descrição:** Exclui um carro existente do banco de dados.
- **Parâmetros da URL:**
  - `id`: O ID do carro que será excluído.

### Exemplo de Resposta:

```json
{
  "message": "Car deleted successfully!"
}
```

## 5. Atualizar um carro

- **Método:** `PUT`
- **Rota:** `/car/<id>`
- **Descrição:** Atualiza os dados de um carro existente no banco de dados.
- **Parâmetros da URL:**
  - `id`: O ID do carro a ser atualizado.

### Corpo da Requisição:

```json
{
  "model": "Novo Modelo",
  "specifications": {
    "color": "Nova Cor",
    "engine": "Novo Motor",
    "doors": 4
  },
  "year": 2022
}
```

### Exemplo de resposta:
```json
{
  "_id": "id_gerado_pelo_mongo",
  "model": "Novo Modelo",
  "specifications": {
    "color": "Nova Cor",
    "engine": "Novo Motor",
    "doors": 4
  },
  "year": 2022
}
```

