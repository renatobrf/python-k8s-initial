# python-k8s-initial

Este projeto é uma aplicação simples que simula o lançamento de um dado e exibe uma mensagem de boas-vindas.

## Estrutura do Projeto

```
python-k8s-initial
├── src
│   ├── app.py          # Ponto de entrada da aplicação que rola um dado a cada 10 segundos.
│   └── welcome.py      # Implementa a página de boas-vindas.
├── requirements.txt     # Lista de dependências necessárias para o projeto.
└── README.md            # Documentação do projeto.
```

## Instalação

Para instalar as dependências necessárias, execute o seguinte comando:

```
pip install -r requirements.txt
```

## Uso

Para executar a aplicação, utilize o seguinte comando:

```
python src/app.py
```

A aplicação irá imprimir uma mensagem de boas-vindas e, a cada 10 segundos, mostrará o resultado do dado rolado.