# Agendamento de Tarefas no Windows

No Windows é necessário fazer uso do agendador de tarefas do sistema operacional
em si, e para isso, os seguintes passos devem ser seguidos.

Passo 1: Abra o Agendador de Tarefas:
- Pressione `Win + R` para abrir a caixa de diálogo ``Executar``. Digite 
`taskschd.msc` e pressione Enter.

Passo 2: Crie uma nova Tarefa:
- No painel direito, clique em "Criar tarefa básica" para iniciar o assistente.

Passo 3: Nome e Descrição:
- Insira um nome e, opcionalmente, uma descrição para a tarefa.

Etapa 4: escolha o tipo de gatilho:
- Selecione "Na inicialização" e clique em "Avançar".

Passo 5: Selecione a ação:
- Selecione "Iniciar um programa" e clique em "Avançar".

Etapa 6: Especifique o programa a ser executado:
- Nesta etapa, você deve especificar o caminho para o interpretador ``Pythonw``
(que não requer que o shell esteja aberto para permanecer rodando) e o script 
`main.py`:
   - Em "Programa/Script" coloque o caminho para o arquivo `Pythonw.exe` 
   presente na venv do projeto;
   - Agora em "Adicionar argumentos", coloque "main.py".
   - Finalmente coloque em "Start in" o caminho do arquivo `main.py`.

As configurações devem ficar como na imagem abaixo.

![Configuração da ação](https://github.com/BrunoFurlanetto/ClickUp_Classroom_Sync/blob/main/docs/action_configuration.jpg)

Etapa 7: Concluir a configuração:
- Clique em "Concluir" para criar a tarefa.

Etapa 8: Definir outras configurações:
- Você precisa ajustar outras configurações, para isso, clique com o botão direito na tarefa e vá para
     properties e siga estas configurações:

![Opções de segurança](https://github.com/BrunoFurlanetto/ClickUp_Classroom_Sync/blob/main/docs/security_options.jpg)

![Condições](https://github.com/BrunoFurlanetto/ClickUp_Classroom_Sync/blob/main/docs/conditions.jpg)

![Configurações](https://github.com/BrunoFurlanetto/ClickUp_Classroom_Sync/blob/main/docs/configurations.jpg)

Passo 9: Revise as configurações:
- Revise as configurações definidas para garantir que estejam corretas.