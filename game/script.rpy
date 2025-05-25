# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alex")
define y = Character("Tu")
define n = Character("Narrador")
define l = Character("Neves")
define t = Character("Tomás")
define r = Character("Rodrigo")
define p = Character("Polícia")
define f = Character("Fred")
define b = Character("Bea")
define s = Character("Ana")

image alex normal = "images/alexnormal.png"
image alex feliz = "images/alexfeliz.png"
image bg ex = "images/bg ex.png"
image bg casa = "images/bg casa.jpeg"
image alex trol = "images/alextrol.png"
image tel = "images/tel.png"
image bg sala = "images/bg sala.jpg"
image alex ff = "images/alexff.png"
image rodrigo = "images/rodrigo.png"
image bg bib = "images/bg bib.jpg"
image bg leoes = "images/bg leoes.jpg"
image neves = "images/neves.png"
image rodrigo = "images/rodrigo.png"
image bg carro = "images/bg carro.jpg"
image bg son = "images/bg don.jpg"
image bg inter = "images/bg inter.jpg"
image alex assu = "images/alexassu.png"
image bg poli = "images/bg poli.jpg"
image bg cab = "images/bg cab.jpg"
image bea = "images/bea.png"
image ana = "images/ana.png"
image bg inicio = "images/bg inicio.jpg"
image fred = "images/fred.png"
image bg disco = "images/disco.jpeg"
image bg ferro = "images/bg ferro.jpg"
image bg cilindro = "images/bg cilindro.jpg"
image bg igreja = "images/bg igreja.jpg"
image bg capela = "images/bg capela.jpg"
image bg cozinha = "images/bg cozinha.JPg"
image cristina = "images/cristina.png"
image msg = "images/msg.png"
image msg1 = "images/msg1.png"
image msg2 = "images/msg2.png"
image msg3 = "images/msg3.png"
image msg4 = "images/msg4.png"
image bg mc = "images/bgmc.jpg"
image bg cemi = "images/bg cemi.jpg"
image bg rib = "images/bg rib.jpg"
image bg hosp = "images/bg hosp.jpg"
label start:


    play music "audio/exsom.mp3"

    scene bg ex:
        zoom 2

    n "Estavas tu na ex..."
    n "Era uma quinta academica..."
    n "Quando de repente..."


    show alex feliz at truecenter:
        zoom 0.5

    a "Olá vi-te ali de cima, tudo bem?"
    a "Chamas te me á atenção"
    a "Queres vir comigo para casa hoje?"

    menu:
        "Pode ser, vá":
            show alex feliz
            a "Ui Ui bora lá"
            stop music
            jump casa

        "Nah deixa tar , hoje não":
            show alex normal
            a "Ah ok na boa"
            a "Dá me pelo menos o teu insta"
            y "OK..."
            stop music
            jump tuacasa

label casa:
    
    hide bge ex
    scene bg casa:
        zoom 0.5
    show alex feliz  at right:
        zoom 0.45


    a "Pronto chegamos"
    a "São 10€ pelo taxi"
    a "Vamos para o meu quarto?"
    menu:
        "Sim":
            hide alex feliz
            n "..."
            n "..."
            n "..."
            show alex trol at right:
                zoom 0.4
            a "Foste muito facil"
            a "Podes bazar"
            n "FINAL PUTINHA"
            jump final
        "Não":
            show alex normal at right:
                zoom 0.5
            a "Ahh ok então baza"
            jump tuacasa



label tuacasa:

    scene bg sala:
     zoom 1.5
    n "Chegaste a casa"
    n "2 DIAS DEPOIS"
    play music "audio/toque.mp3"
    y "..."
    y "..."
    y "..."
    stop music
    show tel at right:
        zoom 1.7
    with zoomin
    a "Boas , olha queres vir à biblioteca Hoje?"
    menu:
        "Ya pode ser":
            a "Ok"
            a "Então mais logo vou te ai buscar"
            a "Até já"
            jump bib
        "Nah tou tenho muita cena para fazer":
            a "Na boa"
            a "Então xau"
            jump tuacasa2

label bib:
    scene bg bib:
        zoom 2
    show alex normal:
        zoom 0.5

    a "Bem,chegamos"
    a "Vamos procurar uma mesa..."
    hide alex normal
    y "*a olhar em volta*"
    y "*a olhar em volta*"
    y "*a olhar em volta*"
    show alex feliz:
        zoom 0.5
    a "Olha ali o meu amigo!! "
    hide alex feliz
    show fred:
     zoom 2
    f "Olá"
    f "Como estão?"
    f "Já vi que não há mesas"
    f "Querem estudar comigo?"
    menu:
        "Sim, pode ser":
            hide fred
            show alex normal:
                zoom 0.5
            a "Isto é uma seca mas prontos"
            n "*a estudar*"
            n "*a estudar*"
            n "*a estudar*"
            a "Já tou farto disto vou bazar"
            n "FINAL SECANTE"
            jump final

        "Nah , nos vamos aos Leões":
            f "Na boa mano vai lá"
            hide fred
            a "Xau mano"
            y "Adeus Fred"
            jump leoes
label leoes:
    scene bg leoes:
        zoom 2
    show alex feliz:
        zoom 0.5
    play music "audio/pessoas.mp3"
    a "Bem vamos beber uns finos"
    a "Tambem queres?"
    menu:
        "Ya pode ser":
            a "Então es tu que pagas a rodada hahah"
        "Nah estou bem":
            a "Ainda bem que eu n tinha dienhrio para pagar te"
    n "*Bebendo*"
    n "*Bebendo*"
    hide alex feliz
    show alex ff:
        zoom 3
    a "Bem ja tou todo morto"
    a "Temos que ir andando"
    stop music
    jump tuacasa2

label tuacasa2:

    scene bg sala:
     zoom 1.5
    n "1 DIAS DEPOIS"
    play music "audio/toque.mp3"
    y "..."
    y "..."
    y "..."
    stop music
    show tel at right:
        zoom 1.5
    with zoomin
    a "Ola tudo bem?"
    a "Era so para te dizer que hoje tenho treino"
    a "Então nao podemos sair"
    menu:
        "Mas eu quero ir ao teu treino":
            a "Ah...."
            a "Tens a certeza?"
            a "Até já"
            jump treino
        "Ah ok saimos outro dia":
            a "Desculpa"
            a "Depois saimos"
            a "Xau"
            jump tuacasa3

label treino:
    play music "audio/carrodentro.mp3"
    scene bg carro:
        zoom 3.5
    show alex feliz at right:
        zoom 0.4
    show rodrigo at left:
        zoom 2.1
    a "Pensava que se podia meter aqui"
    r "Nunca"
    a "ahahahah"
    r "hahahahah"
    hide alex feliz
    show alex trol at right:
        zoom 0.4
    n "FINAL TROCADO PELO RODRIGO"
    stop music
    jump final

label tuacasa3:

    scene bg sala:
     zoom 1.5
    n "3 DIAS DEPOIS"
    play music "audio/toque.mp3"
    y "..."
    y "..."
    y "..."
    stop music
    show tel at right:
        zoom 1.5
    with zoomin
    a "Ola tudo bem?"
    a "Queria ir sair hoje"
    a "Queres vir comigo?"
    menu:
        "Sim Pode ser!":
            a "Ahhh muito bem"
            a "Onde queres ir?"
            menu:
                "Don Papão":
                    a "Ok ja te vou buscar"
                    jump don
                "Passear ao Ferro":
                    a "Já ai vou então"
                    jump ferro
        "Nah, não me aptece":
            a "Foda-se esta muito dificil"
            a "Adeus"
            n "FINAL DICIL DE MAIS"

            jump final
label don:
    play music "audio/pessoas.mp3"
    scene bg don:
        zoom 3.5
    show alex feliz:
        zoom 0.5
    a "Chegamos"
    a "Vamos nos sentar ali"
    a "Já ai vem o empregado"
    hide alex feliz
    show ana at truecenter:
        zoom 2.0
    s "Qué Picanha?"
    menu:
        "Sim,Claro":
            s "Muito bem"
            s "Já trago"
            s "..."
            s "Aqui têm"
            hide ana
            show alex feliz:
                zoom 0.5
            a "Muito bom"
            a "Aposto que foi o Helder que fez"
            a "E ainda fica melhor com este vinho"
            n "*Comendo*"
            n "*Comendo*"
            a "Bem , vamos embora"
            stop music
            jump policia

        "Não":
            a "Ah, Então vaza caraio"
            stop music
            jump inter

label inter:
    scene bg inter:
        zoom 4
    show alex normal:
        zoom 0.5
    a "Já que não queres comer vamos passear?"
    menu:
        "Sim":
            a "Entao vamos lá"
            jump ferro
        "Não":
            a "Então vai te fuder"
            a "Baza!"
            n "FINAL SÓ E COM FOME"
            jump final

label policia:
    scene bg poli:
        zoom 0.8
    play music "audio/policia.mp3"
    show alex assu at left:
        zoom 0.4

    a "..."
    a "..."
    a "Porra eu bebi o vinho"
    a "Tou fodido"
    p "Sai do carro e sopre"
    a "*Soprando*"
    a "*Soprando*"
    p "Você tem 2.8"
    p "Você esta preso!"
    a "Foda-se"
    n "FINAL NA PRISAO"
    jump final



label ferro:
    play music "audio/carrodentro.mp3"
    scene bg cab:
        zoom 1.5
    n "..."
    n "..."
    show bea at truecenter:
        zoom 1.7
    b "Olá"
    menu:
        "Vamos para a Madeira ?":
            a "Olha uma Madeirense Bilahrdeira"
            b "Querem veir Comigue quemer Bananes?"
            b "Que andam fazainde?"
            b "Onde voces vam?"
            b "Vames quemer iogurte com aveia e slades todes os dias?"
            b "Queonhecem o Nero? Venham vê-le ao Arque da Calheta"
            a "Foda-se que me raptar para ir a  Madeira aquela Bilhardeira"
        "Deixa a ai tar com o argentino":
            a "Ainda bem"
            a "Senão tinhamos de ir á Madeira"
    stop music
    jump inicio

label inicio:
    scene bg inicio:
        zoom 1.5
    show alex feliz at truecenter:
        zoom 0.5
    play music "audio/paul.mp3"
    a "Chegamos"
    a "Para onde queres ir?"
    menu:
        "Esquerda":
            a "Vamos lá"
            jump bob
        "Direita":
            a "Ok, Bora "
            jump neves
label neves:
    scene bg ferro:
        zoom 1.5
    show neves:
        zoom 2
    l "Olá amigos"
    l "Querem fazer panquecas?"
    l "Venham á festa na casa da minha avó"
    menu:
        "Bora fazer panquecas!":
            l "Fixe"
            l "Então bora"
            l "Eu levo vos lá"
            jump casaavo
        "Nah deixa":
            l "Na boa então"
            l "Adeus"
            jump sant
label casaavo:
    scene bg casaavo:
        zoom 1.5
    show neves:
        zoom 2
    l "É aqui"
    l "Entrem"
    menu:
        "Bora entrar":
            stop music
            jump cozinha
        "Fugir para o a igreja":
            l "corre!"
            jump sant

label sant:
    scene bg igreja:
        zoom 2
    show alex feliz:
        zoom 0.5
    a "Ui ja estamos longe"
    a "Vamos voltar"
    menu:
        "Ir ao cilindro":
            a "bora então"
            jump igreja
        "Ir ao campo":
            a "Ok ok bora lá"
            jump bob
        "Ir embora":
            y "Vamos embora"
            jump tuacasa4

label igreja:
    scene bg cilindro:
        zoom 1.5
    show alex feliz:
        zoom 0.5
    a "Adoro este café"
    a "Vamos Continuar a andar"
label bob:
    scene bg capela:
        zoom 1.5
    show alex feliz:
        zoom 0.5
    n "*Alex olha estranhamente para o horizonte*"
    y "O que se passa?"
    show alex normal:
        zoom 0.5
    a "Tenho que te contar uma cena"
    a "A verdade é que eu não gosto de ti"
    a "Tenho alegm melhor"
    hide alex normal
    show cristina:
        zoom 2
    a "Tenho esta menina"
    a "Por isso baza"
    n "FINAL VERDADEIRO"
    jump final

label cozinha:
    play music "audio/cozinha.mp3"
    scene bg cozinha:
        zoom 2.7
    show neves at left:
        zoom 2
    l "as panquecas estão feitas"
    l "podem comer"
    hide neves
    n "*comendo*"
    n "*comendo*"
    n "*comendo*"
    show alex ff:
        zoom 3
    a "Tou me senti mal"
    a "Muito mal"
    a "*Leo morre*"
    n "FINAL ENVENENADO"
    jump final

label tuacasa4:

    stop music
    scene bg sala:
     zoom 1.5
    n "Chegaste a casa"
    n "Começas a ver uma série"
    play music "audio/msg.mp3"
    y "..."
    y "..."
    y "..."
    stop music
    show msg at right:
        zoom 0.7
    with zoomin
    y "..."
    menu:
        "Olá achei te Giro":
            show msg1 at right:
                zoom 0.7
            n "Neves convida-te para ires a casa dele"
            menu:
             "Ir":
                l "Ui bora la então"
                jump nevescasa
             "Não ir":
                l "Ah ok na boa vms outro dia"
                l "Vamos antes á Ribeira"
                jump rib
            n "..."
        "Olá , o que queres??":
            show msg2 at right:
                zoom 0.7
            n "..."
            n "Vocês falam por dias..."
            n "Até que ele te convida para a Ribeira"
            menu:
                "Ir":
                    l "Nice, Bora lá"
                    jump rib
                "Não Ir":
                    play music "audio/toque.mp3"
                    y "..."
                    y "..."
                    y "..."
                    stop music
                    hide msg2
                    show tel at right:
                        zoom 1.7
                    a "O Neves contou me que vocês andam a falar"
                    a "Por isso esta tudo acabado entre nós"
                    a "Adeus"
                    n "FINAL REGEITADO PELOS DOIS"
                    jump final
        "Baza Feio":
            show msg3 at right:
                zoom 0.7
            n "..."
            play music "audio/toque.mp3"
            y "..."
            y "..."
            y "..."
            stop music
            hide msg3
            show tel at right:
                zoom 1.7
            a "Porque estás a falar mal do meu amigo!?"
            a "Não acredito que estive com uma pessoa como tu"
            a "Adeus!"
            n "FINAL AZIADO"
            jump final 
        "*Ignorar*":
            show msg4 at right:
                zoom 0.7
            n "..."
            menu:
                "(Proxima DLC)":
                    n "FINAL BREVEMENTE"
                    jump final  

label nevescasa:
    scene bg casaavo:
        zoom 1.5
    show neves:
        zoom 2
    l "Aqui estamos nós"
    l "Vamos para dentro"
    jump casaneves
label casaneves:
    scene bg mc:
        zoom 1.7
    show neves:
        zoom 2
    l "Que quarto lindo"
    l "Não é?"
    l "Bem preciso de ir cagar"
    hide neves
    n "Dá te uma vontade enorme de mexer nas coisas dele"
    menu:
        "Mexer no Telemovel":
            n "Vês uma rapariga chamada Bia no telemovel dele"
            menu:
                "Contar que tas em casa do Neves á Bia":
                    show neves:
                        zoom 2
                    l "Meu deus o que foste fazer!"
                    l "..."
                    jump cemi
                "Não Contar":
                    n "*Neves Volta*"
        "Mexer no roupeiro":
            n "Nada de mais so roupa"
            n "*Neves Volta*"
        "Mexer no PC":
            n "Só cenas de trabalho da Layout "
            n "*Neves Volta*"
    l "Não acredito que estvas a mexer nas minhas coisas"
    l "Baza daqui já"
    n "FINAL CUSCO"
    jump final
label cemi:
    scene bg cemi:
        zoom 2
    n "*Bia mata Neves*"
    n "FINAL TRÁGICO"
    jump final
label rib:
    scene bg rib:
        zoom 3.5
    show neves:
        zoom 2
    l "Que dia bonito Hoje tá"
    l "Vamos saltar para a água?"

    menu:
        "Saltar":
            hide neves
            play music "audio/salto.mp3" noloop
            n "..."
            n "..."
            n "Neves não vem a cima"
            menu:
                "Chamar 112":
                    jump hosp
                "Cagar só":
                    n "As outras pessoas ajudam Neves"
                    n "E tu és preso por não o ajudares"
                    n "FINAL DE MERDA"
                    jump final

        "Não saltar":
            y "É melhor, não ha ali muitas pedras"
            l "Pois é realmente"
            n "*Sentes o cheiro a ganza*"
            hide neves
            n "*Neves vai embora ter com os seu amigos*"
            n "E ele fuma tanto que percebe que na verdade"
            n "Ele é gay"
            n "FINAL FORA DO ARMÁRIO"
            jump final
label hosp:
    scene bg hosp:
        zoom 3
    n "Salvaste a vida de Neves "
    n "Mas ele fica paraplegico"
    n "FINAL SOBRE RODAS"
    jump final
label final:
