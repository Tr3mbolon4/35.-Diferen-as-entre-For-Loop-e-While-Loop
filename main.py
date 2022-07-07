# Vamos Dizer que eu tenho site ou app de venda, onde o cliente tem acesso a ele para fazer vendar particular e nesse site ou app o cliente cadastra seu produto e colocar seu preço.

# porém, eu cobro uma taxa de 10% para vendar realizada na minha plataforma, como eu poderia fazer esse código para esse problema, essa foi minha tarefa.

#tinha maneira diferente para realizar essa soma ou esse calculo porem essa e uma forma mais prática na minha opinião.

#aqui usei uma forma de para o loop usando o break, para ele não fazer uma soma ou um cálculo sem fim, ele iria fazer o cálculo e continuar o mesmo calculo sem fim.

#O produto tem um valor mínimo de R$ 20 para ser anunciado.

print('='*43)
print('       Alexandre Santana Dos Santos:')
print( ' *'*52)
print('     cybersegurança em formação| linux | python | C++ | hardware | redes | Ethical Hacking')
print('   *'*39)
print('        C O D I G O - P Y T H O N')
print('='*50)
print('='*50)
print('='*50)

print('      V E N D A S - O N L I N E')
print('Cadastre seu produto, cobramos um valor simbólico de 10% pelo uso da plataforma!..')
print('                 ===========         ')
produto = input('Nome Do Produto: ')
valor = int(input('Qual valor do produto: '))
print('='*50)

while valor > 20:
  valor = ( valor * 0.10) + valor
  print(f' O valor Final do seu Produto com a comissão da plataforma e R${valor}')
  break
print('='*50)
print('Venda cadastrada!')
print('Etapa 1º do cadastro Realizada!..')