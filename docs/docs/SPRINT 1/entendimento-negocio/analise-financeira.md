# Análise financeira

A análise financeira do projeto determina aspectos importantes para a estratégia econômica que será adotada pela empresa. Essa projeção permite mensurar o desempenho do projeto e elaborar melhores tomadas de decisões. Destaca-se que essa análise inclui entre os fatores um planejamento orçamentário e otimização de recursos. 

## Tabela de despesas e custos

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
      <td>
        O estagiário desempenha um papel crucial no desenvolvimento e implementação do projeto, trazendo perspectivas
        novas e habilidades atualizadas.
      </td>
      <td>R$ 2,000.00</td>
      <td>4,444.44</td>
      <td>6</td>
      <td>26,666.64</td>
    </tr>
    <tr>
      <td>UX Design/Research</td>
      <td>1</td>
      <td>
        Desenvolve produtos e serviços digitais que satisfazem as necessidades, desejos e expectativas dos usuários, de
        forma eficiente e atrativa.
      </td>
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
      <td>Serviços da AWS - Amazon S3</td>
      <td>USD 50</td>
      <td>R$ 249.99</td>
      <td>-</td>
      <td>12</td>
      <td>2999.88</td>
    </tr>
    <tr>
      <td>Serviços da AWS - Amazon EC2</td>
      <td>USD 2000</td>
      <td>R$ 9,999.80</td>
      <td>-</td>
      <td>12</td>
      <td>119997.6</td>
    </tr>
    <tr>
      <td>Serviços da AWS - Amazon RDS</td>
      <td>USD 200</td>
      <td>R$ 999.80</td>
      <td>-</td>
      <td>12</td>
      <td>11997.6</td>
    </tr>
    <tr>
      <td>Serviços da AWS - AWS Lambda</td>
      <td>USD 50</td>
      <td>R$ 249.99</td>
      <td>-</td>
      <td>12</td>
      <td>2999.88</td>
    </tr>
    <tr>
      <td>Serviços da AWS - Amazon CloudWatch</td>
      <td>USD 100</td>
      <td>R$ 499.90</td>
      <td>-</td>
      <td>12</td>
      <td>5998.8</td>
    </tr>
    <tr>
      <td>ChatGPT 4</td>
      <td>1 conta comercial</td>
      <td>USD 20</td>
      <td>R$ 99.98</td>
      <td>-</td>
      <td>12</td>
      <td>1199.76</td>
    </tr>
  </tbody>
  <tr>
    <td colspan="3">Somatório</td>
    <td>R\$ 72,797.46</td>
    <td>-</td>
    <td>-</td>
    <td>R$ 632,400.46</td>
  </tr>
  <tr>
    <td colspan="3">Somatório incluindo impostos por dentro</td>
    <td>R\$ 81,533.15</td>
    <td>-</td>
    <td>-</td>
    <td>R$ 708,288.51</td>
  </tr>
</table>

Os custos com os funcionários CLT são baseados em pesquisas de mercado dos sites [Catho](https://paraempresas.catho.com.br/quanto-custa-um-funcionario-para-empresa/) e [iDinheiro](https://www.idinheiro.com.br/). Além dos salários base, foram inclusos benefícios como plano de saúde de R$ 600, Vale Transporte de R$ 400 e VR de R$ 600.

### Despesas com serviços da AWS
Nessa tabela, as despesas relacionadas ao ambiente de desenvolvimento na AWS são distribuídas da seguinte forma:

- 1 EC2 a $ 2,000 mensais para operacionalizar os serviços do robô.
- Armazenamento S3 a $ 50 mensais para gestão de dados.
- RDS com custo mensal de R$ 200 para o banco MySQL.
- CloudWatch a $ 100 mensais para armazenamento de logs, visando facilitar a identificação e correção de possíveis falhas.
- Lambda a $ 50 mensais para processamento e transformação inicial dos dados recebidos do robô.

### Cálculo do imposto por dentro

No cálculo do custo total de R$ 708,288.52, já foram incluídos impostos, que representam 12% do custo antes dos impostos. Para entender o valor dos impostos nesse contexto, usamos a seguinte fórmula:

- Custo Total = Custo Sem Imposto + (Custo Sem Imposto × Taxa de Imposto).

Reorganizando a fórmula para encontrar o custo sem imposto, temos:

- Custo Sem Imposto = Custo Total / (1 + Taxa de Imposto).

Substituindo com nossos valores:

- Custo Sem Imposto = R$ 708,288.52 / (1 + 0.12).

Calculando, temos:

- Custo Sem Imposto ≈ R$ 632,400.46.

Portanto, o valor dos impostos é:

- R$ 708,288.52 - R$ 632,400.46 = R$ 75,888.06.

### Hipótese de Estimativa de Receitas

Para calcular a estimativa de receitas deste projeto de implementação de um robô de autoatendimento, será considerado o cenário hipotético de desempenho financeiro descrito a seguir.

#### Premissas iniciais

- **Investimento Inicial**: R$ 1.000.000.
- **Gastos com Manutenção**: Consideremos que estes sejam uma fração anual do investimento inicial, por exemplo, 5% ao ano, que equivale a R$ 50.000.
- **Melhoria em Eficiência**: Suponhamos que a implementação do robô melhore a eficiência operacional, levando a uma economia de custos de 10% sobre os custos operacionais anuais da empresa.
- **Aumento na Capacidade Produtiva**: Presumamos um aumento de 15% na receita devido ao aumento da produção e satisfação do cliente.
- **Redução de Erros**: Estimemos uma economia de 5% nos custos associados a erros operacionais.

#### Cálculo da receita

- **Receita Anual Antes do Robô**: Para este exemplo, temos R$ 10.000.000.
- **Custos Operacionais Anuais Antes do Robô**: Suponhamos R$ 7.000.000.
- **Economia de Custos Operacionais com Robô**: 10% de R$ 7.000.000 = R$ 700.000.
- **Redução de Custos por Erros**: 5% de R$ 7.000.000 = R$ 350.000.
- **Aumento na Receita devido ao Robô**: 15% de R$ 10.000.000 = R$ 1.500.000.

#### Estimativa de Lucro no Primeiro Ano:
- **Receita Total com Robô**: R$ 10.000.000 + R$ 1.500.000 = R$ 11.500.000.
- **Custos Operacionais Totais com Robô**: R$ 7.000.000 - (R$ 700.000 + R$ 350.000) = R$ 5.950.000.
- **Lucro Operacional com Robô**: R$ 11.500.000 - R$ 5.950.000 = R$ 5.550.000.
- **Gastos com Manutenção Anual do Robô**: R$ 50.000.
- **Lucro Líquido após Manutenção**: R$ 5.550.000 - R$ 50.000 = R$ 5.500.000.
- **Lucro Líquido Hipotético no Primeiro Ano**: R$ 5.500.000.

Esta hipótese de lucros leva em conta o investimento inicial como um gasto único, concentrando-se nos ganhos anuais proporcionados pelo robô. A redução nos custos operacionais e a diminuição de erros têm um papel crucial no incremento do lucro operacional. Adicionalmente, o aprimoramento na eficiência e no serviço ao cliente impulsiona o crescimento da receita. Comparativamente, os custos anuais de manutenção do robô são mínimos frente ao lucro operacional obtido.

