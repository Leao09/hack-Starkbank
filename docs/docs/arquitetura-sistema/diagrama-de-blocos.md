import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Descrição da Arquitetura

### Diagrama de blocos

O diagrama de blocos é uma representação gráfica que esclarece as partes de um sistema, demonstrando como os vários elementos que constituem a solução se interconectam.

<img src={require('/img/Arquitetura.png').default} width='100%'/>

### Descrição dos elementos da arquitetura

| Elemento | Descrição |
|---|---|
| Rede Local | Para que todos os elementos da arquitetura consigam se comunicar todos devem ser sincronizados na mesma rede de internet. Diante disso, o protocolo de comunicação escolhido foi o ROS2. O ROS (Robot Operating System) é um conjunto de bibliotecas de software e ferramentas que facilitam o desenvolvimento de aplicações robóticas.  |
| Interface homem-máquina | A interface homem-máquina representa os pontos de conexão entre o usuário e a máquina. Para a criação desta interface, foram considerados dois tipos de canais de comunicação. Um deles é através de uma tela LCD incorporada no robô utilizado, enquanto o outro se direciona a uma máquina local que pode ser utilizada em conjunto com a tela incorporada. |
| Servidor STT |O servidor STT, que representa "Speech-to-Text" ou "Conversão de Fala para Texto", é um sistema de software capaz de transformar a expressão vocal humana em texto escrito. Os dados de áudio são submetidos a esse servidor com o propósito de serem traduzidos em formato textual. |
| Servidor TTS | O servidor TTS, que corresponde a "Text-to-Speech" ou "Conversão de Texto em Fala", desempenha a função de transformar texto em dados de áudio. Esse sistema capacita o robô a fornecer respostas no formato de fala. |
| Servidor LLM | O servidor LLM, uma abreviação para "Large Language Model" (Modelo de Linguagem Grande), é um tipo de modelo de linguagem que consiste em uma rede neural com um grande número de parâmetros. Ele capacita o sistema a interpretar o conteúdo falado ou escrito pelo operador e gerar respostas com base em seu treinamento anterior. |


## Fluxo de utilização da solução



<Tabs defaultValue="voz" values={[
        {label: 'Utilizando input de voz', value: 'voz'},
        {label: 'Utilizando input de texto', value: 'texto'}
  ]}>

<TabItem value="voz">

1. O processo se inicia quando o operador se comunica com o robô, utilizando a voz como meio de interação. Para isso, o robô estará equipado com um microfone que possibilitará essa funcionalidade.

2. Após a captação da informação vocal, o áudio é encaminhado para o servidor SST (Speech-to-Text), responsável por convertê-lo em texto. Esse fluxo é representado pelas setas azuis na imagem.

3. Em seguida, o servidor STT envia o texto resultante para o servidor LLM, que interpreta a solicitação e fornece uma resposta correspondente.

4. Ss respostas são transmitidas diretamente do LMM para o robô em formato escrito.

5. Além disso, a resposta também é encaminhada do LLM para o servidor TTS, que transformará o texto em uma mensagem de áudio.

5. Por fim, o áudio da resposta é transmitido à interface homem-máquina, que disponibilizará a resposta ao usuário, executa as tarefas solicitadas e esse fluxo pode ser representado pela seta roxa na imagem. 


</TabItem>

<TabItem value="texto">

1. O processo se inicia quando o operador faz uma requisição por escrito na interface homem-máquina, seja através da interface do usuário local ou do painel LCD touch acoplado ao robô.

2. Após o envio da requisição, ela é encaminhada para o servidor LLM, responsável por interpretar a solicitação e fornecer uma resposta correspondente. Esse fluxo é representado pelas setas vermelhas na imagem.

3. Em seguida, a resposta do LLM é direcionada para o servidor TTS, que converte o texto em uma mensagem de áudio. O resultado obtido é encaminhado ao robô e está respresentada pela seta roxa. 

4. Além disso, as respostas também são transmitidas diretamente do LMM para o robô em formato escrito.

5. O robô, com base nas informações recebidas, executa as tarefas solicitadas e retorna os resultados.


</TabItem>
</Tabs>

