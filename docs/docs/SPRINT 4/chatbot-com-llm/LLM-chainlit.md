# Documentação do uso do ChatBot LLM com Chainlit e API da OpenAI

## Implementação com a API da OpenAI

Utilizamos a API da OpenAI, integrada com o Chat-GPT 3.5-turbo, para pesquisa e geração de respostas. Esta integração permite a personalização do prompt e a sincronização com o LLM da OpenAI. Também implementamos a leitura de documentos, como PDFs, para fornecer contexto às perguntas. Por exemplo, usamos um PDF simulando um inventário de almoxarifado para responder perguntas sobre tipos e localizações de itens.

## Custos de implementação

Devido a utilização da api para um modelo treinado por uma compania a realização de prompts de pesquisa possui um custo, entrentano esse custo é significativamente baixo além da própria plataforma oferecer 5 dólares iniciais que possuem validade de 6 meses, posterior a este periodo eles expiram. O pagamento deste custo não é um problema para a realização de teste e implementação de provas de conceito necessárias para a entrega do projeto. Os valores podem variar dependendo do tamanho da pergunta e do seu nivel de complexidade, mas os valores variam entre 0,001 cents e 0,020 cents.

## Principais Bibliotecas Utilizadas
- Langchain: Facilita a interação com várias funcionalidades, como encadeamento de modelos e carregamento de arquivos (PDF, .txt, Google Drive). Utilizada para vetorização de inputs, melhorando o tratamento de perguntas.
- Chainlit: Inicialmente, o projeto utilizava Streamlit como interface, mas migrou para o Chainlit, que oferece funcionalidades específicas para aplicações de chatbot.
- PyPDF2: Biblioteca auxiliar para leitura de arquivos PDF.
- python-dotenv: Usada para gerenciamento de chaves de API.
- OpenAI GPT-3.5: Para tradução e geração de áudio.
- Chainlit: Framework para a interface interativa do usuário.
- React-Speech-Recognition: Biblioteca para captura de voz na interface do usuário.
- Flask: Para criar o servidor de geração de áudio.

## Funcionalidades 
- Contextualização de respostas: utiliza informações extraídas de um arquivo pdf para contextualizar as respostas dos usuários.
- Gravação de Áudio: Os usuários podem gravar suas perguntas diretamente na interface do chatbot.
- Resposta em Áudio: Além da resposta escrita, o chatbot gera uma resposta em áudio utilizando a API de texto-para-voz da OpenAI.

## Arquitetura do ChatBot


**1. Interface do Chatbot em Chainlit:**

- O usuário pode interagir por texto ou gravação de áudio.
- Para captura de aúdio o sistema utiliza a biblioteca ```react-speech-recognition```, um pacote do React que fornece funcionalidades de reconhecimento de voz, permitindo a conversão de fala em texto em aplicações web.
- Upload de arquivo PDF mantém-se como uma opção.

**2. Pré-processamento e Preparação dos Dados:**

- Conversão de Áudio em Texto: Quando o usuário opta por falar, a gravação de áudio é transcrita em texto por meio da biblioteca ```react-speech-recognition``` na interface do Chainlit.

**3. Processamento da Consulta:**

- Tratamento de Consultas de Áudio e Texto: As consultas, sejam elas originárias de áudio transcritas ou texto, são processadas pelo modelo GPT-3.5 da OpenAI.

**4. Geração e Envio da Resposta:**

- Respostas em Texto e Áudio: As respostas são geradas em texto e, simultaneamente, convertidas em áudio.
- API de Texto-para-Voz da OpenAI: A conversão de texto em áudio é realizada utilizando a API TTS (Text-to-Speech) da OpenAI. Esta API transforma o texto gerado pelo modelo GPT-3.5 em fala natural, utilizando vozes sintéticas.

**5. Servidor para Conversão de Texto em Áudio das Respostas:**

- Servidor Flask: Configuração de um servidor Flask para gerenciar a conversão de texto em áudio. Este servidor interage com a API TTS da OpenAI, convertendo texto em áudio para a interface do Chainlit.

- Fluxo de Resposta de Áudio: O texto gerado pelo chatbot é enviado ao servidor Flask que utilizando a API da OpenAI, gera a resposta em áudio e a retorna para a interface do usuário.

<img src="https://raw.githubusercontent.com/2023M8T2-Inteli/grupo5/main/media/images/arquiteura_chainlit.png
" alt="Arquitetura Chat Bot" width="100%" />





