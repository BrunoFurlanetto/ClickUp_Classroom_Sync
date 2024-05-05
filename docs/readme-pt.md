# Documentação de Sincronização do Google Classroom com o ClickUp

## Visão Geral

Esta documentação destina-se a ajudar os alunos a usar o sistema de
sincronização do Google Classroom com o ClickUp. O objetivo deste passo a
passo é guiar você através do processo de configuração e execução do projeto
em sua própria máquina, permitindo que você automatize uma transferência de
dados entre o Google Classroom e o ClickUp.

## Pré-requisitos

1. Python 3.11 ou mais recente
2. Credenciais da API do ClickUp

## Passo 1: Configuração do Projeto

1. Clone o repositório do projeto:
```bash
git clone https://github.com/BrunoFurlanetto/ClickUp_Classroom_Sync.git

cd ClickUp_Classroom_Sync
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:

- No windowns

```bash
venv\Scripts\activate
```

- No macOS/Linux:

```bash
source venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Etapa 2: configuração das credenciais da API

1. Credenciais do Google Classroom:
     - Na primeira vez que você usar o sistema, ele irá redirecioná-lo para a 
        tela de autorização do Google. Depois disso, você não precisará 
        fornecer esses permissões novamente.

2. Credenciais do ClickUp:
     - Para o ClickUp, siga as instruções apresentadas na [documentação](https://clickup.com/api/developer-portal/authentication/) da 
        própria API:
       - Faça login no ClickUp.
       - Clique no seu avatar no canto inferior esquerdo e selecione "Aplicativos".
       - Em "API Token", clique em "Gerar".
       - Você pode copiar e colar seu token de API pessoal sempre que necessário!
     - Neste ponto, crie um arquivo `.env` e salve o token gerado nele:
       ```
       clickup_api_key = '<YOUR_API_TOKEN>'
       ```

## Passo 3: Configuração Adicional

1. Este projeto utiliza um banco de dados local em ``SQlite``, visando reduzir 
    o número de solicitações feitas às APIs. Assim, é necessário implementar 
    as migrações vindo do alambic como segue:

```bash
alembic upgrade head
```

2. Após a aplicação das migrações, é necessário cadastrar o ID e nome do
    o espaço que receberá as novas listas vindas do Google Classroom (No
    versão alfa, será necessário o uso de ferramentas de terceiros para fazer
    esse registro).

   - Na tabela ``espacos`` do banco de dados, registre o ID e o nome do
   espaço dentro do ClickUp para o qual as listas relacionadas às turmas
   devem ser registradas.
     - Para isso abra o espaço que deseja usar em seu navegador.
     - Na barra de endereços do navegador, você verá a URL do espaço, que 
     normalmente é algo como `https://app.clickup.com/1234567/v/l/123456/`.
     O ID do espaço é o conjunto de caracteres após a última barra ("/"),
     então neste exemplo, o ID do espaço seria `123456`. Também pode aparecer
     como `https://app.clickup.com/1234567/v/l/4-123456-1/`, e neste
     caso, pegue apenas o número do meio.

## Passo 4: Agendamento de Tarefas

Para agendar a execução do script em python de sincronização do Google
Classroom com ClickUp no Windows, você pode usar o Agendador de Tarefas do sistema. Para mais
informações [clique aqui](https://github.com/BrunoFurlanetto/ClickUp_Classroom_Sync/blob/main/docs/agendamento_tarefa_windows.md).

Para garantir que as configurações de agendamento estejam corretas, execute a tarefa e veja se
o status permanece "Em execução".

A partir deste ponto, o sincronizador está funcionando e deve iniciar junto com
o Windows. O sistema faz a verificação logo na inicialização e todos os dias 
entre 14h e 20h. Ele só lançará uma notificação de sincronização se houver um
diferença entre o banco de dados local e os sistemas remotos, caso contrário isto
será executado silenciosamente.

## Considerações finais

Com este guia passo a passo, você configurou e executou o sistema de 
sincronização entre o Classroom e o ClickUp. Agora, você pode automatizar a 
transferência de dados entre as plataformas e otimizar o gerenciamento de 
classes e tarefas.

Se você tiver alguma dúvida ou encontrar problemas, sinta-se à vontade para 
consultar o documentação do projeto e/ou entrar em contato com a equipe de 
manutenção. Divirta-se usando o sistema para aprimorar sua experiência de 
estudante!

## Funcionalidades futuras

Este sincronizador está constantemente evoluindo para atender às necessidades dos 
usuários. Abaixo estão algumas das funcionalidades que estamos considerando 
implementar no futuro:

1. **Interface gráfica**: Uma das primeiras funcionalidades que está sendo considerado,
é a implementação de uma interface gráfica para facilitar tanto o cadastro das API KEY
quanto para as vizualizações das ultimas tarefas que foram encontradas no Google
Classroom e que foram adicionadas no ClickUp.
2. **Aumento das notificações**: Também está sendo considerado o aumento do número de
notificações e não apenas quando a sincronização é iniciada.
3. **Verificação de urgênca e Mensagens pelo WhatsApp**: Por último, está sendo 
considerado é a implementação de uma verificação das atividades já cadastradas no
ClickUp e com isto o envio de mensagens via WhatsApp lembrando da data de entrega da
atividade. Nesta etapa também será implementado a alteração de status de urgência da
tarefa conforme a proximidade com a data de entrega da tarefa.
