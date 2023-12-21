# Backend Leitor de Cupons Fiscais

Backend desenvolvido  em Flask para processamento e gerenciamento de notas fiscais através de OCR.



![Arquitetura CuponsFiscais](https://i.imgur.com/ChLBP9d.png)

## Tecnologias Utilizadas

- **Flask**: Framework web para construir a API.
- **Flask-Cors**: Para permitir o acesso à API através de diferentes domínios.
- **Flask-JWT-Extended**: Para autenticação via JSON Web Tokens.
- **Flask-Restx**: Para uma organização melhor da API e documentação automática.
- **Celery**: Para gerenciamento de tarefas assíncronas com Redis.
- **Docker**: Utilizado para conteinerizar os serviços de PostgreSQL e Redis.
- **Redis**: Como broker de mensagens para tarefas assíncronas.

