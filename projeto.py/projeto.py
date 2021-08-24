from time import sleep
mcu = str(input('digite seu usuario para cadastro no programa de emprestimos: ')).strip().lower()
if len(mcu) >= 6:
    print('usuario cadastrado com sucesso')
    mcd = input('digite uma senha com no minimo 8 caracteres: ')
    if len(mcd) >= 8:
        print('sua senha foi cadastrada com sucesso, guarde-a bem')
        nu1 = input('digite seu nome de usuario: ').lower()
        nu2 = input('digite sua senha de usuario: ')
        if nu1 == mcu and nu2 == mcd:  # caso o usuario nao erre a senha
            print('usuario logado!!')
            n = str(input('digite seu nome: ')).strip()
            vy = input('qual a sua idade: ')
            vd = float(input('Qual o valor desejado para saque? '))
            vy = int(vy)
            if vy > 18:  # caso oeprestimo seja aprovado
                saque = 'S'.lower()
                transferencia = 'T'.lower()
                print('emprestimo aprovado, dirija-se a boca do caixa para sacar ou tranferir o dinheiro.')
                ap = input('Digite S para saque\nOu T para Transferencia: ')
                if ap != transferencia:  # caso saque seja selicionado
                    print('Saque selecionado')
                    print('contagem de notas')
                    print('retire suas notas', sleep(4))
                elif ap != saque:  # caso tranferencia seja selecionado
                    Trt = 1
                    g = 2
                    Trp = 3
                    print('metodos de tranferencia:')
                    mdt = int(input('digite 1 para tranferencia Ted\n2 Para doc\n3 para Pix\n '))
                    if mdt < g and Trp:  # se transferencia ted for selecionada
                        print('Transferencia Ted Selecionada')
                        me = float(input('Digite o Cpf para validaçao de chave e tranferencia: '))
                        le = me
                        float(input('Confirme Se o Cpf Foi digitado corretamente\n{}'.format(le),))
                        print('Valor Tranferido com sucesso')
                        print('Aguarde emissao de comprovante')
                        print('imprimindo')
                        print('impressao concluida, nao se esqueça de guarda-lo bem', sleep(4))
                    elif mdt < Trp and g:  # caso transferencia doc seja selecionada
                        print('tranferencia Doc Selecionada')
                        td = float(input('Digite seu cpf para validaçao de dados'))
                        le1 = td
                        float(input('confirme se seu cpf foi digitado corretamente\n{}'.format(le1)))
                        print('valor tranferido com sucesso')
                        print('aguarde emissao de comprovante')
                        print('imprimindo')
                        print('impressao concluida, nao se esqueça de guarda-lo bem.', sleep(4))
                    elif mdt != Trt or g:  # caso pix seja selecionado
                        print('tranferencia Pix Selecionado:')
                        print('fique atento(a) a sua chave pix e tome cuidado com golpes')
                        tp = float(input('digite sua chave pix para validaçao cpf,email,chave pix e etc :'))
                        input('confira COM ATENÇAO se a sua chave pix esta correta')
                        print('tranferencia pix realizada com sucesso')
                        print('comprovante enviado ao email cadastrado a chave pix.')
                        print('obrigado por ter utilizado nossos serivços')


else:
    print('erro desconhecido')
