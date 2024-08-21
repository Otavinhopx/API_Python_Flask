
# API de Frutas

Este projeto é uma API simples construída com Flask-RESTful, que permite a manipulação de um banco de dados simulado de frutas. A API oferece operações básicas de CRUD (Create, Read, Update, Delete) para gerenciar uma lista de frutas.

## Estrutura do Projeto

O projeto é composto por duas classes principais:

1. **Frutas**: Retorna uma lista de todas as frutas disponíveis.
2. **Fruta**: Permite operações detalhadas em uma única fruta, incluindo recuperação, criação, atualização e exclusão.

## Endpoints Disponíveis

### 1. `GET /frutas`
Retorna a lista de todas as frutas disponíveis.

**Resposta de Sucesso (200):**
```json
{
    "frutas": [
        {
            "fruta_id": "laranja",
            "nomeFruta": "laranja",
            "corFruta": "laranja",
            "precoFruta": 4.20
        },
        {
            "fruta_id": "morango",
            "nomeFruta": "morango",
            "corFruta": "vermelha",
            "precoFruta": 6.20
        },
        {
            "fruta_id": "maça",
            "nomeFruta": "maça",
            "corFruta": "vermelha",
            "precoFruta": 1.20
        }
    ]
}
```

### 2. `GET /fruta/<fruta_id>`
Recupera os detalhes de uma fruta específica pelo `fruta_id`.

**Resposta de Sucesso (200):**
```json
{
    "fruta_id": "laranja",
    "nomeFruta": "laranja",
    "corFruta": "laranja",
    "precoFruta": 4.20
}
```

**Resposta de Erro (404):**
```json
{
    "message": "Fruta Not found"
}
```

### 3. `POST /fruta/<fruta_id>`
Adiciona uma nova fruta ao banco de dados.

**Corpo da Requisição:**
```json
{
    "nomeFruta": "banana",
    "corFruta": "amarela",
    "precoFruta": 2.50
}
```

**Resposta de Sucesso (201):**
```json
{
    "fruta_id": "banana",
    "nomeFruta": "banana",
    "corFruta": "amarela",
    "precoFruta": 2.50
}
```

### 4. `PUT /fruta/<fruta_id>`
Atualiza os detalhes de uma fruta existente. Se a fruta não existir, retorna um erro.

**Corpo da Requisição:**
```json
{
    "nomeFruta": "laranja",
    "corFruta": "laranja",
    "precoFruta": 4.50
}
```

**Resposta de Sucesso (200):**
```json
{
    "fruta_id": "laranja",
    "nomeFruta": "laranja",
    "corFruta": "laranja",
    "precoFruta": 4.50
}
```

**Resposta de Erro (404):**
```json
{
    "message": "Fruta not found to update"
}
```

### 5. `DELETE /fruta/<fruta_id>`
Remove uma fruta do banco de dados.

**Resposta de Sucesso (200):**
```json
{
    "message": "Fruta deleted"
}
```

## Como Rodar o Projeto

1. Clone o repositório:
    ```bash
    git clone <URL do Repositório>
    ```

2. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute a aplicação:
    ```bash
    python app.py
    ```

## Observações

- Esta API utiliza um banco de dados simulado representado por uma lista de dicionários.
- A API não persiste os dados após a reinicialização do servidor.
