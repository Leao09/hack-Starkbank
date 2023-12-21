import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Descrição da Arquitetura

### Diagrama de blocos

O diagrama de blocos é uma representação gráfica que esclarece as partes de um sistema, demonstrando como os vários elementos que constituem a solução se interconectam.

<img src={require('/img/Arquitetura-sprint5.png').default} width='150%'/>

### Descrição dos elementos da arquitetura

| Elemento | Descrição |
|---|---|
|Interface Homem-Máquina  | A interface homem-máquina representa os pontos de conexão entre o usuário e a máquina e foi desenvolvida no formato de uma aplicação web, utilizando o framework NextJS.  |
| Backend | O backend foi implementado em FastAPI e desempenha um papel central para o funcionamento da aplicação. Através dele, é possível realizar comunicação com o banco de dados, interagir com os servidores STT e LLM, além de enviar comandos para o robô por meio da bridge. |
| Servidor STT | O ChatGPT foi escolhido como servidor de "Large Language Model" para esta função. Ao fazer perguntas ao chatbot, este modelo se encarrega de estender o conteúdo solicitado e fornecer uma resposta adequada. |
| Servidor LLM | O servidor TTS, que corresponde a "Text-to-Speech" ou "Conversão de Texto em Fala", desempenha a função de transformar texto em dados de áudio. Esse sistema capacita o robô a fornecer respostas no formato de fala. |
| Servidor TTS | O servidor TTS, responsável pela "Text-to-Speech" ou "Conversão de Texto em Fala", tem a função de transformar texto em dados de áudio. |
| Bridge | A bridge foi construída utilizando o protocolo de comunicação WebSocket. É por meio dessa bridge que as solicitações feitas pelo backend conseguem alcançar o robô e enviar comandos para ele. |
| Robô | O robô desempenha um papel crucial no projeto, pois é responsável por buscar fisicamente as peças no almoxarifado. |
| Banco de Dados | O banco de dados utilizado na aplicação é um banco relacional em Postgres, hospedado no RDS da AWS. |
|Nav2 | Para a movimentação foi utilizado o framework Nav2, sistema de navegação para robôs desenvolvido para funcionar com o ROS 2. |
| API Simple Comander | O Simple Commander é uma API feita em Python para interagir com o Nav2 sem precisar criar os nós para isso diretamente. O Nav2 é o responsável por lançar os nós responsáveis pela navegação. |