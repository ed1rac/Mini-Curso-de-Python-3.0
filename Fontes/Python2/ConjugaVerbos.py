# encoding: utf-8
"""
Função:
    Conjugador de verbos regulares
Autor:
    Edkallenn
Descrição:
    Esse programa serve para conjugar verbos regulares e demonstra o poder das
    listas na linguagem Python. Listas são mutáveis e são objetos facilmente
    manipuláveis através de seus métodos
Complexidade:
      n
Referências:
      https://pt.wikipedia.org/wiki/Verbo
"""
#verbo = 'programar'
verbo = str(raw_input("Digite um verbo da regular: "))
terminacao = verbo[-2:]
radical = verbo[:-2]
conjuga_ar_presente = ['o','as','a','amos','ais','am']
conjuga_ar_preteritop = ['ei','aste','ou','amos','astes','aram']
conjuga_ar_preteritoi = ['ava','avas','ava','ávamos','áveis','avam']
conjuga_ar_preteritomqp = ['ara','aras','ara','áramos','áreis','aram']
conjuga_ar_futurop = ['arei','arás','ará','aremos','areis','arão']
conjuga_ar_futuropret = ['aria','arias','aria','aríamos','aríeis','ariam']
conjuga_gerundio_ar='ando'
conjuga_participio_ar='ado'
conjuga_er_presente = ['o','es','e','emos','eis','em']
conjuga_er_preteritop = ['i','este','eu','emos','estes','eram']
conjuga_er_preteritoi = ['ia','ias','ia','íamos','íeis','iam']
conjuga_er_preteritomqp = ['era','eras','era','êramos','êreis','eram']
conjuga_er_futurop = ['erei','erás','erá','eremos','ereis','erão']
conjuga_er_futuropret = ['eria','erias','eria','eríamos','eríeis','eriam']
conjuga_gerundio_er='endo'
conjuga_participio_er='ido'
conjuga_ir_presente = ['o','es','e','imos','is','em']
conjuga_ir_preteritop = ['i','iste','iu','imos','istes','iram']
conjuga_ir_preteritoi = ['ia','ias','ia','íamos','íeis','iam']
conjuga_ir_preteritomqp = ['ira','iras','ira','íramos','íreis','iram']
conjuga_ir_futurop = ['irei','irás','irá','iremos','ireis','irão']
conjuga_ir_futuropret = ['iria','irias','iria','iríamos','iríeis','iriam']
conjuga_gerundio_ir='indo'
conjuga_participio_ir='ido'
pronomes=['eu','tu','ele','nós','vós','eles']
tempos_indicativo = ['Presente', 'Pretérito Perfeito', 'Pretérito Imperfeito', 'Pretérito Mais-que-perfeito', 'Futuro do Presente', 'Futuro do Pretérito']

print("Verbo: " + verbo + '\n' + '================')
if terminacao=='ar':
    print('Gerúndio: ' + radical + conjuga_gerundio_ar)
    print('Particípio: ' + radical + conjuga_participio_ar + '\n')
    j = 0
    print(tempos_indicativo[j] + '\n' + '==============')
    j+=1
    for i in range(6):        
        print(pronomes[i] + ' ' + radical + conjuga_ar_presente[i])
    print('\n' + tempos_indicativo[j] + '\n' + '==================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_ar_preteritop[i])
    print('\n' + tempos_indicativo[j] + '\n' + '====================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_ar_preteritoi[i])
    print('\n' + tempos_indicativo[j] + '\n' + '==========================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_ar_preteritomqp[i])
    print('\n' + tempos_indicativo[j] + '\n' + '==================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_ar_futurop[i])
    print('\n' + tempos_indicativo[j] + '\n' + '===================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_ar_futuropret[i])
    print('\n')
if terminacao=='er':
    print('Gerúndio: ' + radical + conjuga_gerundio_er)
    print('Particípio: ' + radical + conjuga_participio_er + '\n')
    j = 0
    print(tempos_indicativo[j] + '\n' + '==============')
    j+=1
    for i in range(6):        
        print(pronomes[i] + ' ' + radical + conjuga_er_presente[i])
    print('\n' + tempos_indicativo[j] + '\n' + '==================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_er_preteritop[i])
    print('\n' + tempos_indicativo[j] + '\n' + '====================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_er_preteritoi[i])
    print('\n' + tempos_indicativo[j] + '\n' + '==========================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_er_preteritomqp[i])
    print('\n' + tempos_indicativo[j] + '\n' + '==================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_er_futurop[i])
    print('\n' + tempos_indicativo[j] + '\n' + '===================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_er_futuropret[i])
    print('\n')
if terminacao=='ir':
    print('Gerúndio: ' + radical + conjuga_gerundio_ir)
    print('Particípio: ' + radical + conjuga_participio_ir + '\n')
    j = 0
    print(tempos_indicativo[j] + '\n' + '==============')
    j+=1
    radical_ir=radical.replace ('e','i')
    for i in range(6):
        if i==0:
            print(pronomes[i] + ' ' + radical_ir + conjuga_ir_presente[i])
        else:
            print(pronomes[i] + ' ' + radical + conjuga_ir_presente[i])
    print('\n' + tempos_indicativo[j] + '\n' + '==================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_ir_preteritop[i])
    print('\n' + tempos_indicativo[j] + '\n' + '====================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_ir_preteritoi[i])
    print('\n' + tempos_indicativo[j] + '\n' + '==========================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_ir_preteritomqp[i])
    print('\n' + tempos_indicativo[j] + '\n' + '==================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_ir_futurop[i])
    print('\n' + tempos_indicativo[j] + '\n' + '===================')
    j+=1
    for i in range(6): 
        print(pronomes[i] + ' ' + radical + conjuga_ir_futuropret[i])
    print('\n')

        
