# Documentação do uso do ChatBot LLM com Chainlit e API da OpenAI

## LLM (Large Language Model)

Um LLM é um software avançado de inteligência artificial, treinado em vastos volumes de dados textuais. Ele é projetado para compreender e gerar texto em linguagem humana de forma sofisticada, permitindo aplicações diversas em processamento de linguagem natural.

## Implementação com a API da OpenAI

Utilizamos a API da OpenAI, integrada com o Chat-GPT 3.5-turbo, para pesquisa e geração de respostas. Esta integração permite a personalização do prompt e a sincronização com o LLM da OpenAI. Também implementamos a leitura de documentos, como PDFs, para fornecer contexto às perguntas. Por exemplo, usamos um PDF simulando um inventário de almoxarifado para responder perguntas sobre tipos e localizações de itens.

## Custos de implementação

- Devido a utilização da api para um modelo treinado por uma compania a realização de prompts de pesquisa possui um custo, entrentano esse custo é significativamente baixo além da própria plataforma oferecer 5 dólares iniciais que possuem validade de 6 meses, posterior a este periodo eles expiram. O pagamento deste custo não é um problema para a realização de teste e implementação de provas de conceito necessárias para a entrega do projeto. Os valores podem variar dependendo do tamanho da pergunta e do seu nivel de complexidade, mas os valores variam entre 0,001 cents e 0,020 cents.

## Principais bibliotecas utilizadas 

Para implementar este recurso, utilizamos bibliotecas como Langchain e Chainlit. Langchain facilita a interação com várias funcionalidades, como encadeamento de modelos e carregamento de arquivos (PDF, .txt, Google Drive), e vetorização de inputs para melhor tratamento de perguntas. Inicialmente, usamos o Streamlit como interface, mas depois migramos para o Chainlit, que oferece adaptações específicas para aplicações de chatbot. Bibliotecas auxiliares como PyPDF2 (leitura de PDFs) e python-dotenv (gerenciamento de chaves de API) também foram utilizadas.

## Arquitetura do ChatBot


**1 . Interface do Chatbot em Chainlit:**


- O usuário inicia interagindo com o chatbot através de uma interface construída em Chainlit.
- O usuário faz upload de um arquivo PDF e envia uma pergunta.

**2. Pré-processamento e Preparação dos Dados:**

  - O arquivo PDF é recebido e processado para extrair o texto.
- O texto do PDF é dividido em pedaços menores para facilitar o processamento.
- Estes pedaços são armazenados e possivelmente convertidos em embeddings usando a biblioteca langchain.

**3. Processamento da Consulta:**

- Quando uma pergunta é recebida, ela é processada utilizando o modelo GPT-3.5 da OpenAI, acionado pela API da OpenAI e gerenciado pelo `langchain.`
- A consulta é associada aos documentos mais relevantes (pedaços de texto do PDF) por meio de um `VectorStore.`

**4. Geração e Envio da Resposta:**

- Com base nos documentos relevantes e na pergunta, o chatbot gera uma resposta.
- A resposta é então enviada de volta para o usuário através da interface Chainlit.

<img src="https://raw.githubusercontent.com/2023M8T2-Inteli/grupo5/main/media/images/arquitetura_chat_bot.png" alt="Arquitetura Chat Bot" width="100%" />





