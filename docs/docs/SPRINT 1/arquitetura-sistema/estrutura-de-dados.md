# Estrutura de dados 

A estrutura de dados proposta foca no desenvolvimento de um sistema robótico para o almoxarifado da Ambev, integrando automação e inteligência artificial. O objetivo é otimizar o gerenciamento de inventário e operações logísticas, enfatizando a eficiência e a precisão. Aspectos cruciais como gestão de estoque e experiência do usuário serão explorados.

**1.  Gestão do estoque e validação de itens retirados**
    
- Implementar um sistema de controle no robô, garantindo que os itens e quantidades retirados correspondam exatamente ao solicitado.
          
- Desenvolver um mecanismo de verificação digital que registre todas as transações feitas pelo robô, garantindo assim um rastreamento preciso dos itens retirados.

**2.  Mapeamento do ambiente do almoxarifado**
   
- Representação gráfica de um layout do almoxarifado que contenha todas as disposições das peças e itens, bem como obstáculos e objetos presentes no ambiente. Elementos importantes para a navegação autônoma do robô.  
      
**3. Banco de dados do itens do almoxarifado**

- Uma tabela contendo a descrição, código ou quantidade dos itens ou peças presentes em estoque. Esse banco de dados também pode conter informações sobre qual a localização do item no almoxarifado.  
      
**4. Gestão de operações e Integração com o sistema SAP (System Applications and Products in Data Processing)**
   
-  O robô deve ser integrado ao sistema SAP para acessar e consultar a disponibilidade de peças em tempo real.
    
- O robô também deverá ter a capacidade de indicar a necessidade de devolver itens ao almoxarifado se identificar requisições feitas incorretamente.
    
- Todos os dias o sistema gerará um arquivo CSV que documenta todas as atividades executadas, como pedidos atendidos, destinos apontados, e eventuais interações com os operadores. Este registro servirá para análise das operações. 
      
**5. Modelagem do Chatbot**
    
- **Modelo de Linguagem (LLM) com ChatGPT:**  projeto será aprimorado com a integração do ChatGPT, uma modalidade de LLM.  Essa integração possibilita que o chatbot não só compreenda e responda de forma precisa às solicitações, mas também desenvolva diálogos mais naturais e contextualizados. O ChatGPT oferece capacidades de aprendizado contínuo e adaptação, o que garante que o sistema se mantenha sempre atualizado. 
    
- **Registro de Interações:** Uma lista detalhada que registra todas as interações entre o chatbot e o usuário. Essa lista é vital para análises futuras, refinamento do modelo e melhoria contínua da interação com o usuário.  

**6. Experiência do Usuário e Modalidades de Interação**
    
- O chatbot, baseado em diálogos reais entre operadores e almoxarifes, será projetado para oferecer uma interação autêntica e se adaptar a diferentes modalidades de comunicação, como voz e texto.