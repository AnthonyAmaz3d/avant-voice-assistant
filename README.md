<h1 align="center" > Speech Command Assistant 🔊 </h1>

Este projeto é um assistente de comandos de voz desenvolvido em Python, capaz de ouvir comandos, responder por meio de síntese de fala, automatizar algumas tarefas e gerenciar uma lista de tarefas usando um banco de dados SQLite.

<h2 align="center" > Funcionalidades 🧰</h2>

- **Reconhecimento de fala:** O assistente escuta e reconhece comandos de voz em português (pt-BR).
- **Síntese de fala:** O assistente responde aos comandos com áudio gerado.
- **Gerenciamento de tarefas:** É possível adicionar tarefas a uma lista que é armazenada em um banco de dados SQLite.
- **Automação de tarefas:** O assistente pode tirar screenshots e abrir o navegador para sites específicos.
- **Comandos de voz suportados:**
  - "Adicione uma tarefa"
  - "Liste as tarefas"
  - "Tire um print"
  - "Youtube"
  - "World of Warcraft"
  - "Steam"
  - "Sair"

<h2 align="center" > Instalação ⏳</h2>

1. Clone o repositório para sua máquina local:
   
   ```bash
   git clone https://github.com/AnthonyAmaz3d/speech-command-assistant.git
   
2. Instale as dependências necessárias:
   
   ```bash
   pip install -r requirements.txt
   
<h2 align="center" > Dependências 📦</h2>

  - speech_recognition
  - gTTS
  - winsound
  - pydub
  - pyautogui
  - webbrowser
  - sqlite3

<h2 align="center" > Como usar 📖</h2>

  1. Execute o script principal:
     ```bash
     python main.py
  2. O assistente começará a escutar os comandos de voz. Siga as instruções faladas para interagir.

<h2 align="center" > Banco de Dados 📂</h2>

  - O banco de dados SQLite tasks.db é criado automaticamente ao iniciar o programa, armazenando suas tarefas em uma tabela chamada tasks.

<h2 align="center" > Exemplo de uso 🔍</h2>

  - Adicionar uma tarefa: Diga "Adicione uma tarefa" e, em seguida, informe a tarefa que deseja adicionar.
  - Listar tarefas: Diga "Liste as tarefas" para exibir todas as tarefas armazenadas.
  - Tirar um print: Diga "Tire um print" para o assistente capturar uma captura de tela.
  - Abrir o YouTube: Diga "YouTube" para abrir o navegador na página do YouTube.
    
<h2 align="center" > Contribuição 🤝 </h2>

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
