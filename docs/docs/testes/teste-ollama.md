# Tentativa de implementação do Ollama

## Visão Geral

Além da implementação do chatbot com a API da OpenAI, também foi realizado uma tentativa de desenvolver um chatbot utilizando a biblioteca Ollama, que integra modelos de linguagem de aprendizado profundo (LLM) em Python. Nesse contexto, nosso objetivo específico era criar uma aplicação capaz de interpretar e utilizar PDFs ou outros arquivos como contexto para as interações do chatbot.

## Seleção do Modelo e Desafios

Optamos pelo modelo LLM Ollaama2, considerando suas capacidades e compatibilidade com nossos requisitos. Inicialmente, o modelo demonstrou um desempenho satisfatório em tarefas básicas de compreensão e geração de linguagem. No entanto, enfrentamos dificuldades significativas relacionadas à integração e ao processamento de arquivos PDF.

## Problemas com o Processamento de PDF

O principal obstáculo encontrado foi a incapacidade da aplicação de reconhecer e interpretar o conteúdo de arquivos PDF. Diversas tentativas foram feitas para extrair informações dos PDFs e convertê-las em um formato legível para o modelo LLM Ollama2. Apesar dos esforços, todos os erros encontrados estavam relacionados à extração e ao processamento do conteúdo dos PDFs, o que impedia a aplicação de utilizar esses dados como contexto para o chatbot.

## Resultado e Decisão Final

Devido às limitações encontradas na implementação do chatbot com oLlama, especialmente em relação ao manuseio de PDFs, a equipe decidiu migrar para a solução oferecida pela OpenAI. A funcionalidade de processamento de PDF era essencial para o escopo do projeto, e a incapacidade de atender a esse requisito com Ollama foi determinante para a nossa decisão final.
