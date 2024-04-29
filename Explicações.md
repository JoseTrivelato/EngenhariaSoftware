unica.py 
O código é um exemplo simples em Python que implementa uma classe chamada Calculadora. Esta classe tem o propósito de realizar operações matemáticas básicas, como soma, subtração, multiplicação e divisão.
Neste exemplo, a classe Calculadora tem uma única responsabilidade: realizar operações matemáticas simples. Cada método dentro da classe executa uma única operação matemática (somar, subtrair, multiplicar, dividir).
Resumindo, o código serve para demonstrar como aplicar o Princípio da Responsabilidade Única em Python, criando uma classe que realiza operações matemáticas básicas.

Aberto_Fechado.py
Neste exemplo, temos a classe abstrata Produto que define um método calcular_preco(). Em seguida, temos duas implementações de produtos: ProdutoSimples e ProdutoComDesconto, que representam produtos sem desconto e produtos com desconto, respectivamente. A classe Pedido recebe uma lista de produtos e pode calcular o custo total do pedido somando os preços de cada produto.
Se quisermos adicionar um novo tipo de produto, como um produto com impostos adicionais, podemos criar uma nova classe que estende Produto e implementa calcular_preco(), sem precisar modificar o código existente em Pedido. Isso mantém a classe Pedido fechada para modificação, mas aberta para extensão, conforme exigido pelo principio Aberto_Fechado.

inversao_dependencia.py
Neste exemplo, temos a classe abstrata ServicoDeNotificacao que define um método notificar(). Em seguida, temos duas implementações concretas: ServicoDeEmail e ServicoDeSMS, que notificam os usuários por e-mail e SMS, respectivamente.
A classe Notificador é um módulo de alto nível que depende da abstração ServicoDeNotificacao, conforme exigido pelo DIP. Ele recebe uma instância de ServicoDeNotificacao em seu construtor e pode enviar notificações usando o método enviar_notificacao(), sem se preocupar com os detalhes de implementação de cada serviço de notificação.
Isso permite que adicionemos facilmente novos métodos de notificação no futuro, seguindo o princípio da inversão da dependência.

Demeter.py
Neste exemplo, a classe Cliente tem um método imprimir_produtos_comprados() que percorre todos os pedidos do cliente e, para cada pedido, percorre todos os itens do pedido e imprime os produtos comprados.
Este exemplo segue o princípio de Demeter, pois a classe Cliente não precisa saber sobre a estrutura interna de um pedido ou de um item. Em vez disso, ela interage apenas com seus vizinhos imediatos (pedidos), delegando a responsabilidade de imprimir os produtos comprados para as classes Pedido e ItemPedido. Isso promove um baixo acoplamento entre as classes e facilita a manutenção do código.
