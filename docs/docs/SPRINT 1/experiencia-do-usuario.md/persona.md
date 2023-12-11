# Persona

Uma persona é uma construção fictícia que representa o cliente ideal de um produto. Ela é fundamentada em dados reais que abrangem o comportamento, características demográficas e, além disso, incorpora histórias pessoais, motivações, objetivos, desafios e preocupações dos clientes.

## Persona 1: Técnico de Manutenção

<img src={require('/img/Persona-1.png').default} width='100%'/>

## Persona 2: Operador de Packing

<img src={require('/img/Persona-2.png').default} width='100%'/>

Pensando no impacto da acessibilidade do projeto e a responsabilidade social da Ambev para com seus colaboradores, lista-se as possíveis limitações funcionais das personas:

#### Ausência ou perda de visão moderada ou completa
A perda de visão moderada pode significar uma visão significativamente comprometida, tornando a realização de tarefas cotidianas desafiadoras, enquanto a cegueira completa implica na incapacidade total de enxergar luz ou formas. Aqueles que enfrentam essa condição frequentemente precisam aprender a se adaptar usando seus outros sentidos, como audição e tato. 
O presente projeto incorpora uma interação sonora com o usuário, permitindo que aqueles que dependem dessa forma de comunicação utilizem o sistema. Além disso, o sistema é equipado com recursos de detecção de obstáculos durante a movimentação, com o objetivo de prevenir potenciais acidentes de trabalho.

#### Limitações de vigor
As limitações de vigor referem-se à dificuldade de uma pessoa em realizar atividades físicas com força, energia e resistência adequadas, devido a problemas de saúde, falta de condicionamento físico ou lesões. Pode afetar tarefas que exigem esforço físico.
O sistema, por ser móvel, é capaz de auxiliar o usuário com algumas tarefas que antes exigiam algum esforço físico. Como exemplo, pode-se imaginar o seguinte cenário: O técnico de manutenção precisa interromper a atividade que está realizando em uma máquina, pois necessita de uma peça. Para isso, ele precisa se deslocar até o local de criação da ordem de serviço e retornar até onde estava previamente, possivelmente causando desgaste físico. Com a implementação do sistema, essa dor é aliviada, visto que o mesmo é capaz de se deslocar até o técnico para receber uma entrada via texto ou voz e completar a solicitação feita pelo usuário.

#### Dificuldade em interpretar informações
A dificuldade em interpretar informações refere-se à incapacidade ou desafio de uma pessoa em compreender e extrair significado de dados, textos ou outros tipos de informações apresentadas, tornando a assimilação de conhecimento ou tomada de decisões mais complexa. Isso pode resultar em mal-entendidos, erros de julgamento e dificuldades na resolução de problemas.
Neste sentido, o projeto, por utilizar LLM (Large Language Model), é capaz de servir como guia para o usuário, pois consegue interpretar o que é dito por ele e auxiliá-lo com possíveis dúvidas. O sistema também possui as aptidões para compreender a linguagem cotidiana utilizada pelos usuários.

#### Ausência ou perda de audição moderada ou completa
A ausência ou perda de audição moderada ou completa é uma limitação funcional que afeta a capacidade de uma pessoa de ouvir sons em diferentes graus. Pode dificultar a comunicação verbal, a percepção de sinais de perigo e a participação em atividades sociais.
O presente projeto contempla interação visual com o usuário, através de um dispositivo da empresa e/ou um display LCD acoplado no robô. Dessa forma, aqueles que dependem dessa forma de comunicação são inclusos e podem se tornar usuários.

#### Ausência, perda ou dificuldades de fala moderada ou completa
A ausência de fala refere-se à incapacidade completa de produzir sons articulados da fala, geralmente devido a danos neurológicos graves. A perda de fala é a diminuição da capacidade de fala devido a lesões ou distúrbios, enquanto a dificuldade de fala pode incluir gagueira, um distúrbio que causa interrupções na fluência e pode ser acompanhado por sotaque, uma variação na pronúncia que pode ser cultural ou devido a influências regionais ou linguísticas.
Conforme citado acima, o sistema conta com interação visual e um LLM funcionando como o cérebro do robô auxiliar. Para tentar aliviar as dores de quem sofre com essa limitação funcional, o LLM pode usar modelos de linguagem treinados em diferentes regiões do país e também em diferentes idiomas. Além disso, o modelo consegue auxiliar na correção gramatical, filtrando, mesmo que limitadamente, o que é comunicado via voz.  

#### Dificuldade em manejar e/ou dedilhar
"Dificuldade em manejar e/ou dedilhar" em um contexto industrial refere-se à incapacidade ou inabilidade de um operador ou trabalhador em manipular com precisão e destreza equipamentos, ferramentas ou componentes, prejudicando a eficiência e a qualidade do trabalho. Isso pode resultar em erros de montagem, produção mais lenta e maior risco de acidentes.
Um robô autônomo, ao automatizar certos processos, pode significativamente reduzir a carga manual dos operadores. Além disso, ele tem a capacidade de oferecer treinamento e assistência nas operações a serem realizadas, o que não apenas diminui a probabilidade de erros, mas também reduz o risco de possíveis lesões.

#### Excesso de ruido no ambiente de fabrica
O excesso de ruído no ambiente de fábrica pode prejudicar a comunicação entre os trabalhadores, causar fadiga auditiva e impactar negativamente na saúde, segurança e bem-estar dos funcionários. Além disso, níveis elevados de ruído podem dificultar a detecção de alarmes e sinais de perigo, comprometendo a segurança no local de trabalho.
Além de manter uma interação visual com o usuário, o LLM também pode ser personalizado para filtrar as informações relevantes do ruído das conversas. Além disso, o robô pode exibir alertas em seu visor para situações que não podem ser reconhecidas por meio de áudio.



