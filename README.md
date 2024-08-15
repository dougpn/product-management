# Gerenciamento de Produtos

Este é um projeto de **Gerenciamento de Produtos** desenvolvido em Python usando a biblioteca Tkinter para a interface gráfica e SQLite para o banco de dados. Ele permite adicionar, atualizar, excluir e visualizar produtos em um banco de dados local.

## Funcionalidades

- Adicionar novos produtos com nome, descrição, quantidade e preço.
- Atualizar informações de produtos existentes.
- Excluir produtos do banco de dados.
- Visualizar a lista de produtos cadastrados.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação utilizada.
- **Tkinter**: Biblioteca para construção da interface gráfica.
- **SQLite**: Banco de dados leve para armazenamento local dos dados.

## Instalação

Certifique-se de ter Python instalado na máquina e siga os passos abaixo para clonar e configurar o projeto em sua máquina local:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/dougpn/product-management
   cd product-management
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Execute o projeto:**

   ```bash
   python app.py
   ```

## Como Usar

1. Ao executar o script `app.py`, a interface gráfica será exibida.
2. Utilize os campos de entrada para adicionar novos produtos. Preencha o nome, descrição, quantidade e preço e clique em "Adicionar".
3. A lista de produtos cadastrados aparecerá na parte inferior da janela. Selecione um produto para editá-lo ou excluí-lo.
4. Para atualizar um produto, edite as informações nos campos e clique em "Atualizar".
5. Para excluir um produto, selecione-o na lista e clique em "Excluir".

## Estrutura do Projeto

```
gerenciamento-de-produtos/
│
├── app.py             # Arquivo principal da aplicação
├── database.py        # Operações do banco de dados (SQLite)
├── README.md          # Documentação do projeto
```

## Contribuição

Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
