# Design Patterns

### O que é Design Pattern

Design patterns representam soluções reutilizáveis e comprovadas para desafios comuns encontrados no desenvolvimento de software. Esses padrões encapsulam as melhores práticas e abordagens consolidadas ao longo do tempo para enfrentar os desafios específicos que os desenvolvedores frequentemente encontram durante o processo de design de sistemas.

### Design Pattern utilizado

No contexto do projeto em questão, está previsto o emprego do padrão **Observer Pattern**. O Observer Pattern é uma abordagem de design que estabelece uma relação de dependência entre objetos, de modo que, quando um objeto sofre uma alteração em seu estado, todos os objetos dependentes são automaticamente notificados e atualizados. Esse padrão é amplamente empregado em sistemas nos quais um componente precisa manter outros componentes informados sobre mudanças relevantes.

### Motivação da escolha

A escolha e adoção desse padrão se justificam devido à sua compatibilidade com o Robot Operating System (ROS), que é o principal framework utilizado no projeto. O ROS utiliza uma variante do Observer Pattern em sua infraestrutura de comunicação, onde os "publishers" divulgam mensagens em tópicos, e os "subscribers" se inscrevem nesses tópicos para receber e processar as mensagens. Essa relação entre publishers e subscribers no ROS é análoga à relação entre observáveis e observadores no Observer Pattern, tornando-o uma escolha apropriada para o contexto do projeto.

