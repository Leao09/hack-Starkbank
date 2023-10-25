# Análise financeira

A análise financeira do projeto determina aspectos importantes para a estratégia econômica que será adotada pela empresa. Essa projeção permite mensurar o desempenho do projeto e elaborar melhores tomadas de decisões. Destaca-se que essa análise inclui entre os fatores um planejamento orçamentário e otimização de recursos. 

A tabela abaixo ilustra as estimativas de despesas anuais e custos associados ao investimento no projeto. As despesas se relacionam aos compromissos financeiros recorrentes que a empresa tem, como as mensalidades dos serviços AWS. Por outro lado, os custos refletem os investimentos únicos ou fixos, como a aquisição de hardware (exemplo: robô, MacBook Pro) e contratação de pessoal.

<table border="1">
  <thead>
    <tr>
      <th>Categorias</th>
      <th>Quantidades</th>
      <th>Descrição</th>
      <th>Gastos mensais</th>
      <th>Valor CLT por funcionário</th>
      <th>Duração (Meses)</th>
      <th>Total Acumulado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Estagiário</td>
      <td>1</td>
      <td>O estagiário desempenha um papel crucial no desenvolvimento e implementação do projeto, trazendo perspectivas novas e habilidades atualizadas.</td>
      <td>R$ 2,000.00</td>
      <td>4,444.44</td>
      <td>6</td>
      <td>26,666.64</td>
    </tr>
    <tr>
      <td>UX Design/Research</td>
      <td>1</td>
      <td>Desenvolve produtos e serviços digitais que satisfazem as necessidades, desejos e expectativas dos usuários, de forma eficiente e atrativa.</td>
      <td>R$ 6,800.00</td>
      <td>11,271.11</td>
      <td>2</td>
      <td>22,542.22</td>
    </tr>
    <tr>
      <td>Engenheiro da Computação</td>
      <td>1</td>
      <td>Responsável pela arquitetura geral do sistema...</td>
      <td>R$ 8,000.00</td>
      <td>12,977.78</td>
      <td>12</td>
      <td>155,733.36</td>
    </tr>
    <tr>
      <td>Engenheiro de Software</td>
      <td>1</td>
      <td>Encarregado do desenvolvimento...</td>
      <td>R$ 7,500.00</td>
      <td>12,266.67</td>
      <td>8</td>
      <td>98,133</td>
    </tr>
    <tr>
      <td>PO</td>
      <td>1</td>
      <td>Líder de equipe de desenvolvimento</td>
      <td>R$ 8,000.00</td>
      <td>12,977.78</td>
      <td>12</td>
      <td>155,733.36</td>
    </tr>
    <tr>
      <td>turblebot3 burguer</td>
      <td>1</td>
      <td>Robô que será utilizado no projeto...</td>
      <td>R$ 3,400.00</td>
      <td>-</td>
      <td>-</td>
      <td>3400</td>
    </tr>
    <tr>
      <td>MacBook Pro para desenvolvimento</td>
      <td>2</td>
      <td>Especificações do MacBook...</td>
      <td>R$ 24,998.00</td>
      <td>-</td>
      <td>-</td>
      <td>24998</td>
    </tr>
    <tr>
      <td rowspan="5">Serviços da AWS</td>
      <td>Amazon S3</td>
      <td>50</td>
      <td>R$ 249.99</td>
      <td>-</td>
      <td>12</td>
      <td>2999.88</td>
    </tr>
    <tr>
      <td>Amazon EC2</td>
      <td>2000</td>
      <td>R$ 9,999.80</td>
      <td>-</td>
      <td>12</td>
      <td>119997.6</td>
    </tr>
    <tr>
      <td>Amazon RDS</td>
      <td>200</td>
      <td>R$ 999.80</td>
      <td>-</td>
      <td>12</td>
      <td>11997.6</td>
    </tr>
    <tr>
      <td>AWS Lambda</td>
      <td>50</td>
      <td>R$ 249.99</td>
      <td>-</td>
      <td>12</td>
      <td>2999.88</td>
    </tr>
    <tr>
      <td>Amazon CloudWatch</td>
      <td>100</td>
      <td>R$ 499.90</td>
      <td>-</td>
      <td>12</td>
      <td>5998.8</td>
    </tr>
    <tr>
      <td>ChatGPT 4</td>
      <td>1 conta comercial</td>
      <td>20</td>
      <td>R$ 99.98</td>
      <td>-</td>
      <td>12</td>
      <td>1199.76</td>
    </tr>
</tbody>
<tr>  <td colspan="3">Somatório</td>  <td>R$ 72,797.46</td>  <td>-</td>  <td>-</td>  <td>632,400.46</td>  
</tr>  
</table>

Os custos com os funcionários CLT são baseados em pesquisas de mercado dos sites Catho e iDinheiro. Além dos salários base, foram inclusos benefícios como plano de saúde de R$ 600, Vale Transporte de R$ 400 e VR de R$ 600.

As despesas relacionadas ao ambiente de desenvolvimento na AWS são distribuídas da seguinte forma:

- 1 EC2 a $ 2,000 mensais para operacionalizar os serviços do robô.
- Armazenamento S3 a $ 50 mensais para gestão de dados.
- RDS com custo mensal de R$ 200 para o banco MySQL.
- CloudWatch a $ 100 mensais para armazenamento de logs, visando facilitar a identificação e correção de possíveis falhas.
- Lambda a $ 50 mensais para processamento e transformação inicial dos dados recebidos do robô.