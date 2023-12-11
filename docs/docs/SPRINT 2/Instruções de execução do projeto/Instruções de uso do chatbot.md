# Instruções de uso do ChatBot com LLM da OpenAI

#### 1. Clonando o Repositório

-   Execute o comando abaixo para clonar o repositório do GitHub:
```   
    git clone github.com/2023M8T2-Inteli/grupo5.git
```
    
-   Navegue até o diretório clonado.

#### 2. Instalação de Dependências

-   Execute o comando para instalar todas as dependências necessárias:

    ```
    pip install -r requirements.txt
    ```

#### 3. Configuração de Variáveis de Ambiente

-   Crie um arquivo `.env` na raiz do projeto.
-   Adicione sua chave de API do OpenAI:
    
    ```
    OPENAI_API_KEY=sua_chave_de_api_aqui
    ```

#### 4. Preparação do Arquivo PDF

-   Prepare um arquivo PDF que deseja usar com o chatbot. Este arquivo será carregado e processado pelo sistema.

#### 5. Executando o ChatBot

-   Execute o script principal do chatbot:
    
    ```
    chainlit run app.py -w
    ```
    
-   O chatbot agora está rodando e aguardando a interação do usuário.

#### 6. Interagindo com o ChatBot

-   O bot solicitará que você faça o upload de um arquivo PDF.
-   Após o upload, o bot processará o conteúdo do PDF.
-   Você pode fazer perguntas relacionadas ao conteúdo do PDF.
-   O bot utilizará o modelo LLM da OpenAI para responder às suas perguntas.

O vídeo abaixo apresenta como deve ser realizada a última etapa:
[![Veja o vídeo no youtube!](https://i3.ytimg.com/vi/WwcymLsu2Hs/maxresdefault.jpg)](https://youtu.be/WwcymLsu2Hs)
