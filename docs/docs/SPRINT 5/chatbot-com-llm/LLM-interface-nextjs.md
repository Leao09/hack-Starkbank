# Documentação do uso do ChatBot LLM com Next.js e API da OpenAI

## Implementação com a API da OpenAI

Neste projeto, utilizamos a API da OpenAI, integrada com o Next.js e o Chat-GPT 3.5-turbo. Essa integração permite personalizar prompts e sincronizar com o modelo de linguagem de grande escala (LLM) da OpenAI. Implementamos também a funcionalidade de leitura de documentos, como PDFs, para fornecer contexto adicional às interações dos usuários.

## Custos de implementação

Devido a utilização da api para um modelo treinado por uma compania a realização de prompts de pesquisa possui um custo, entrentano esse custo é significativamente baixo além da própria plataforma oferecer 5 dólares iniciais que possuem validade de 6 meses, posterior a este periodo eles expiram. O pagamento deste custo não é um problema para a realização de teste e implementação de provas de conceito necessárias para a entrega do projeto. Os valores podem variar dependendo do tamanho da pergunta e do seu nivel de complexidade, mas os valores variam entre 0,001 cents e 0,020 cents.

## Principais Bibliotecas Utilizadas
- Next.js: Framework React utilizado para construir a interface do usuário.
- Web Speech API: Para reconhecimento de voz (STT) e transcrição de áudio para texto.
- React-Speech-Recognition: Biblioteca para captura de voz.
- OpenAI GPT-3.5: Usado para processamento de linguagem natural e geração de respostas.
- PyPDF2: Para leitura de arquivos PDF.
- python-dotenv: Gerenciamento de variáveis de ambiente e chaves de API.

## Funcionalidades 
- Contextualização de Respostas: Utiliza informações de arquivos PDF para contextualizar as perguntas dos usuários e respostas que são fornecidas.
- Gravação e Transcrição de Áudio: O usuário pode gravar sua pergunta em áudio, que é transcrita em texto.
- Resposta em Áudio: O chatbot fornece respostas tanto escritas quanto em áudio, utilizando a API de texto-para-voz da OpenAI e a Web Speech API.

## Arquitetura do ChatBot


**1. Interface do Usuário com Next.js:**

- Interação por texto ou gravação de áudio.
- Uso da Web Speech API para reconhecimento de voz e conversão de áudio em texto.
- Opção de upload de arquivo PDF.

**2. Pré-processamento e Preparação dos Dados:**

- Conversão de Áudio em Texto: A gravação de áudio é transcrita em texto pela Web Speech API.

**3. Processamento da Consulta:**

- As consultas, seja texto direto ou transcrição de áudio, são processadas pelo modelo GPT-3.5 da OpenAI.

**4. Geração e Envio da Resposta:**

- As respostas são geradas em texto e convertidas em áudio.
- Utilização da API Texto-para-Voz da OpenAI para a conversão de texto em áudio.

**5. Servidor para Conversão de Texto em Áudio:**

- Configuração de um servidor em FastAPI para gerenciar a conversão de texto em áudio.
- O texto gerado é convertido em áudio pela API da OpenAI e enviado de volta para a interface do usuário.


### Diagrama da arquitetura

O diagrama abaixo representa a interação do usuário com o chatbot, o processamento de entrada de texto e áudio, e a geração de respostas em texto e áudio. A integração com a API da OpenAI é crucial para o processamento de linguagem natural e a conversão de texto em fala.

<img src="https://raw.githubusercontent.com/2023M8T2-Inteli/grupo5/main/media/images/arquitetura_nextjs.png" alt="Arquitetura Chat Bot" width="100%" />










