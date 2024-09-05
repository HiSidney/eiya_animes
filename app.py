from flask import Flask,render_template,request,jsonify,redirect,make_response
app = Flask(__name__)

import bancoDados
import cv2
import os
from random import randint
from datetime import datetime, timedelta

@app.route('/')
def home():
    generos = bancoDados.pegar_todas_infos_da_tabela('generos')
    capitulos = bancoDados.pegar_todas_infos_da_tabela_com_desc('capitulos')

    for i in capitulos:
        frames_de_video(f'static/Video/capitulos/{i[0]}/{i[1]}/{i[2]}.mp4',f'static/Video/capitulos/{i[0]}/{i[1]}/thumbnails/',i[2])

    return render_template('home.html', generos=generos)

@app.route('/pesquisa_dinamica', methods=['GET', 'POST'])
def pesquisa_dinamica():
    generos = bancoDados.pegar_todas_infos_da_tabela('generos')
    if request.method == 'POST':
        req = request.get_json()
        resultado_pesquisa = bancoDados.pega_resutados_pesquisa(req['search'])
        return jsonify(resultado_pesquisa)
    else:
        return render_template('home.html',generos=generos)

@app.route('/base')
def base():
    esta_logado = verificar_usuario()
    if esta_logado == "sim":
        resposta = pega_cookies()
        return resposta
    else:
        return "naoExiste"

@app.route('/adm', methods=['GET', 'POST'])
def adm():
    cookies = request.cookies
    status_usuario = cookies.get("status")
    if status_usuario == "adm":
        generos = bancoDados.pegar_todas_infos_da_tabela('generos')

        if request.method == 'POST':
            req = request.get_json()

            if req['tipoCadastro'] == 'Anime':
                if req['nomeAnime'] == '' or req['data_lancamento_anime'] == '' or req['criador_anime'] == '' or req['logoAnime'] == '' or req['dublagem_anime'] == '' or req['descricaoAnime'] == '' or req['generos'] == '':
                    print('erro. Falta info para o insert')
                else:
                    bancoDados.adiciona_anime_bancoDados(req['nomeAnime'],req['data_lancamento_anime'],req['criador_anime'],req['logoAnime'],req['dublagem_anime'],req['descricaoAnime'],req['generos'])
                return req['tipoCadastro']
            
            elif req['tipoCadastro'] == 'Capitulo':

                pasta_com_idAnime = f"static/Video/capitulos/{req['anime_que_capitulo_pertencente']}"
                if os.path.isdir(pasta_com_idAnime):
                    print ('Ja existe uma pasta com esse nome!')
                else:
                    os.mkdir(pasta_com_idAnime) # aqui criamos a pasta caso nao exista
                    print ('Pasta criada com sucesso!')

                pasta_com_idTemporada = f"static/Video/capitulos/{req['anime_que_capitulo_pertencente']}/{req['temporada_que_capitulo_pertencente']}"
                if os.path.isdir(pasta_com_idTemporada):
                    print ('Ja existe uma pasta com esse nome!')
                else:
                    os.mkdir(pasta_com_idTemporada) # aqui criamos a pasta caso nao exista
                    print ('Pasta criada com sucesso!')

                pasta_com_thumbnail = (f"static/Video/capitulos/{req['anime_que_capitulo_pertencente']}/{req['temporada_que_capitulo_pertencente']}/thumbnails")
                if os.path.isdir(pasta_com_thumbnail):
                    print ('Ja existe uma pasta com esse nome!')
                else:
                    os.mkdir(pasta_com_thumbnail) # aqui criamos a pasta caso nao exista
                    print ('Pasta criada com sucesso!')

                #print(f"static/Video/capitulos/{req['anime_que_capitulo_pertencente']}/{req['temporada_que_capitulo_pertencente']}/{req['numero_capitulo']}.mp4",f"static/Video/capitulos/{req['anime_que_capitulo_pertencente']}/{req['temporada_que_capitulo_pertencente']}/thumbnails/{req['numero_capitulo']}")
                frames_de_video(f"static/Video/capitulos/{req['anime_que_capitulo_pertencente']}/{req['temporada_que_capitulo_pertencente']}/{req['numero_capitulo']}.mp4",f"static/Video/capitulos/{req['anime_que_capitulo_pertencente']}/{req['temporada_que_capitulo_pertencente']}/thumbnails/{req['numero_capitulo']}",req["numero_capitulo"])
                thumbnail = f"static/Video/capitulos/{req['anime_que_capitulo_pertencente']}/{req['temporada_que_capitulo_pertencente']}/thumbnails/{req['numero_capitulo']}.png"
                bancoDados.adiciona_capitulo_bancoDados(req['anime_que_capitulo_pertencente'],req['temporada_que_capitulo_pertencente'],req['numero_capitulo'],req['video_capitulo'],thumbnail)
                return req['tipoCadastro']
            
            elif req['tipoCadastro'] == 'Temporada':
                bancoDados.adicionar_temporada_bancoDados(req['anime_que_temporada_pertencente'],req['num_temporada'],req['data_lancamento_temporada'],req['trailer_temporada'])
                return req['tipoCadastro']
            
            else:
                bancoDados.adicionar_genero_bancoDados(req['nome_genero'])
                return req['tipoCadastro']
        else:
            return render_template('adm.html',generos = generos)
    else:
        return redirect('/')
    
@app.route('/animes/<id_anime>')
def anime(id_anime):
    generos = bancoDados.pegar_todas_infos_da_tabela('generos')

    CAnime = {}
    animes = bancoDados.pega_nomeAnime_logoAnime_descricao_tabelaAnimes(id_anime)
    print(animes)
    CAnime['NomeAnime'] = animes[0][0]
    CAnime['logo_anime'] = animes[0][1]
    CAnime['descricao'] = animes[0][2]
    CAnime['id_anime'] = id_anime

    capitulos = bancoDados.pega_idCapitulos_dataLancamento_capitulo_tabelaCapitulos(id_anime)
    ligacao_anime_genero = bancoDados.pega_ligacaoAnime_genero(id_anime)
    quant_temporadas = bancoDados.quantidade_temporadas(id_anime)
    trailers = bancoDados.buscaTrailer(id_anime)

    return render_template('anime.html', anime = CAnime,capitulos = capitulos,generos = generos,ligacao_anime_genero = ligacao_anime_genero,temporadas = quant_temporadas, trailers=trailers)

@app.route('/animes-<id_anime>/tem-<id_temporada>/cap-<id_capitulo>')
def page_assistir_cap(id_anime,id_temporada,id_capitulo):
    generos = bancoDados.pegar_todas_infos_da_tabela('generos')
    capitulos = bancoDados.pega_anime_capitulos(id_anime,id_temporada,id_capitulo)
    quant_capitulos = bancoDados.quant_capitulos(id_anime,id_temporada)
    user = pega_cookies()
    if user['email'] == None:
        print("ñ tem user")
    else:
        bancoDados.add_historico_usuario(user['email'], id_anime,id_capitulo)

    return render_template('video.html', capitulos=capitulos, generos=generos, quant_capitulos=quant_capitulos[0][0])

@app.route('/animes')
def todos_animes():
    generos = bancoDados.pegar_todas_infos_da_tabela('generos')
    return render_template('todos_animes.html',generos=generos)

@app.route('/random')
def random():
    numero_de_animes = bancoDados.conta_numero_de_animes()
    id_anime = randint(1,numero_de_animes[0][0])
    return redirect('/animes/'+str(id_anime))

@app.route('/retornaAnimes_e_Capitulos')
def retornaAnimes_e_Capitulos():
    animes = bancoDados.pega_top_10_animes_mais_recentes()
    neoCapitulo = []
    capitulos = bancoDados.pega_info_tabelaAnime_tabelaCapitulo()

    for i in capitulos:
        imagemPath = str(i[4]).replace((f'static\\Video\\capitulos\\{str(i[0])}\\{str(i[1])}\\{str(i[2])}.mp4'),(f'static\\Video\\capitulos\\{str(i[0])}\\{str(i[1])}\\thumbnails\\{str(i[2])}.png'))

        diferenca_de_tempo = calcula_diferenca_na_data_e_na_hora(i[3],i[6])

        item = (i[0], i[1], i[2], i[3], imagemPath, i[5], diferenca_de_tempo)
        neoCapitulo.append(item)
    return jsonify(animes,neoCapitulo)

@app.route('/retornaAnimes')
def retornaAnimes():
    animes = bancoDados.pegar_todas_infos_da_tabela("animes")
    return jsonify(animes)

@app.route('/retornaAnimes_por_genero')
def retornaAnimes_por_generos(id_genero):
    animes = bancoDados.pega_anime_por_genero(id_genero)
    return jsonify(animes)

@app.route('/animes/genero/<id_genero>')
def generos(id_genero):
    generos = bancoDados.pegar_todas_infos_da_tabela('generos')
    animes = bancoDados.pega_animes_ligacaoGeneros_generos(id_genero)

    return render_template('anime_genero.html',generos=generos,animes=animes)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        req = request.get_json()
        busca = bancoDados.pega_info_user(req['login_mail'])
        
        if busca == []:
            return 'erro'
        else:
            if req['senha'] == busca[0][2]:
                if busca[0][3] == 'adm':
                    resposta = make_response("adm")

                    expires = datetime.now() + timedelta(days=1)
                    resposta.set_cookie("email",busca[0][1], expires=expires)
                    resposta.set_cookie("login",busca[0][0], expires=expires)
                    resposta.set_cookie("status",busca[0][3], expires=expires)
                    return resposta
                else:
                    resposta = make_response("user")

                    resposta.set_cookie("email",busca[0][1])
                    resposta.set_cookie("login",busca[0][0])
                    resposta.set_cookie("status",busca[0][3])
                    return resposta
            else:
                print("Senha Incorreta")
                return 'erro'
    
    else:
        return render_template('login.html')

@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    if request.method == 'POST':
        req = request.get_json()
        if req['senha'] == req['confirmarSenha'] and len(req['senha']) >= 8:
            bancoDados.inserir_cadastro_bancoDados(req['email'],req['login'],req['senha'])
            
            resposta = make_response('ok')
            resposta.set_cookie("email",req['email'])
            resposta.set_cookie("login", req['login'])
            resposta.set_cookie("status","user")
            return resposta
        else:
            return 'error'
    else:
        return render_template('cadastro.html')

@app.route('/encerrar_sessao')
def encerrar_sessao():
    resposta = make_response(redirect('/'))
    resposta.set_cookie('email', '', expires=0)
    resposta.set_cookie('login', '', expires=0)
    resposta.set_cookie('senha', '', expires=0)
    resposta.set_cookie('status', '', expires=0)
    return resposta

@app.route('/historico/')
def historico():
    generos = bancoDados.pegar_todas_infos_da_tabela('generos')
    cookies = request.cookies
    email = cookies.get('email')

    historico = bancoDados.pega_info_do_historico(email)
    novo_historico = []

    for i in historico:
        diferenca_de_tempo = calcula_diferenca_na_data_e_na_hora(i[1],i[2])
        novo_i = (i[0],i[1],[2],i[3],i[4],i[5],i[6], diferenca_de_tempo)
        novo_historico.append(novo_i)
        
    return render_template('historico.html',generos=generos, historico=novo_historico)

@app.route('/apagar_historico')
def apagar_historico():
    cookies = request.cookies
    user = cookies.get("email")
    if user == None:
        return redirect('/')
    else:
        bancoDados.apaga_historico(user)
        return "ok"

@app.route('/novoUsuario', methods=['GET','POST'])
def novoUsuario():
    cookies = request.cookies
    email = cookies.get('email') 
    if email == None:
        return 'erro'
    else:
        if request.method == 'POST':
            req = request.get_json()
            if req['nome'] == '' or req['senha'] == '':
                return 'erro'
            else:
                print("adicionoi")
                bancoDados.addNovoUsuario(req['nome'],email,req['senha'])
                return 'ok'
        else:
            return 'erro'

@app.route('/excluirUsuario')
def excluir_usuario():
    cookies = request.cookies
    email = cookies.get('email') 
    if email == None:
        return 'erro'
    else:
        bancoDados.excluirUsuario(email)
        return 'ok'

@app.route('/ver')
def ver_cookie():
    cookies = request.cookies
    return cookies

@app.route('/account')
def account():
    generos = bancoDados.pegar_todas_infos_da_tabela('generos')
    cookies = request.cookies
    resposta = cookies.get('email')
    if resposta == None:
        return redirect('/')
    else:
        return render_template("account.html", generos=generos)

@app.route('/salva_animes', methods=['POST', 'GET'])
def salva_animes():
    if request.method == 'POST':
        cookies = request.cookies
        email = cookies.get('email')
        if email == None:
            return redirect('/')
        else: 
            req = request.get_json()
            if req['key'] == False:
                bancoDados.removeAnimeFavorito(email,req['id_anime'])
                return 'excluiu'
            else:
                bancoDados.addAnimeFavorito(email,req['id_anime'])
            return 'salvou'
    else:
        return render_template('home.html')
    
@app.route('/verifica_favoritos', methods=["POST","GET"])
def verifica_favoritos():
    if request.method == "POST":
        cookies = request.cookies
        email = cookies.get('email')
        if email == None:
            return redirect('/')
        else: 
            req = request.get_json()
            resposta = bancoDados.verifica_favoritos(email,req['id_anime'])
            if resposta != []:
                return "True"
            else:
                return "False"
    else:
        return redirect('/')

@app.route('/animes_salvos')
def animes_salvos():
    generos = bancoDados.pegar_todas_infos_da_tabela('generos')
    cookies = request.cookies
    email = cookies.get('email')
    if email == None:
        return redirect('/')
    else:
        return render_template('animes_salvos.html',generos=generos)

@app.route('/retorna_animes_salvos')
def retorna_animes_salvos():
    cookies = request.cookies
    email = cookies.get('email')
    if email == None:
        return redirect('/')
    else:
        animes = bancoDados.retornaAnimesSalvos(email)
        return jsonify(animes)

@app.route('/retornaInfoAccount')
def retornaEmail():
    cookies = request.cookies
    email = cookies.get('email')
    if email == None:
        return redirect('/')
    else:
        resultado = bancoDados.retornaInfoAccount(email)
        return resultado

@app.route('/pesquisa_anime_que_capitulo_pertencente', methods=['POST', 'GET'])
def pesquisa_anime_que_capitulo_pertencente():
    cookies = request.cookies
    email = cookies.get('email')
    if request.method == 'POST':
        if email == None:
            return redirect('/')
        else:
            req = request.get_json()
            resposta = bancoDados.pesquisa_anime_que_capitulo_pertencente(req['anime_que_capitulo_pertencente'])
            return resposta
    else:
        return 'erro'

def verificar_usuario():
    cookies = request.cookies
    email_usuario = cookies.get("email")
    if email_usuario == None:
        return "nao"
    else:
        return "sim"

def frames_de_video(entrada,caminho_saida,id_capitulo):
    entrada_capturada = cv2.VideoCapture(entrada)
    cont_0 = 0
    while entrada_capturada.isOpened() and cont_0 < 1:
        retorno, frame = entrada_capturada.read()
        cont_0 += 1
        cont = 0
        while retorno == True and cont < 1:
            #cv2.imwrite(os.path.join(caminho_saida,'%d.png') %cont,frame)
            cv2.imwrite(os.path.join(caminho_saida,'%d.png') %int(id_capitulo),frame)
            cont += 1
        
    cv2.destroyAllWindows()
    entrada_capturada.release()

def pega_cookies():
    cookies = request.cookies
    email = cookies.get("email")
    nome = cookies.get("login")
    User = {"email":email,"nome":nome}
    return User

def calcula_diferenca_na_data_e_na_hora(data_antiga,hora_antiga):
    time_capitulo_fragmentada = str(hora_antiga).split(':')
    nova_hora_min_atual = time_capitulo_fragmentada[0]+":"+time_capitulo_fragmentada[1]

    tempo = data_antiga+" "+nova_hora_min_atual
    data_capitulo = datetime.strptime(tempo,"%Y-%m-%d  %H:%M")
    data_atual = datetime.now()

    diferenca = data_atual - data_capitulo
    dias = diferenca.days
    semanas = dias / 7
    meses = diferenca.days / 30.44
    anos = diferenca.days / 365.25

    data_atual_fragmentada = str(data_atual).split(' ')
    horario_atual_fragmentado = data_atual_fragmentada[1].split(":")
    hora_atual = horario_atual_fragmentado[0]
    minuto_atual = horario_atual_fragmentado[1]

    data_capitulo_fragmentada = str(data_capitulo).split(' ')
    horario_data_capitulo_fragmentado = data_capitulo_fragmentada[1].split(":")
    hora_data_capitulo = horario_data_capitulo_fragmentado[0]
    minuto_data_capitulo = horario_data_capitulo_fragmentado[1]

    diferenca_de_hora = int(hora_atual) - int(hora_data_capitulo)
    diferenca_de_minutos = int(minuto_atual) - int(minuto_data_capitulo)


    if dias < 7 and dias > 0:
        if dias != 1:
            diferenca_do_tempo = str(int(dias))+ " dias atrás"
        else:
            diferenca_do_tempo = str(int(dias))+ " dia atrás"
    
    elif dias <= 0:
        if diferenca_de_hora <= 0:
            if diferenca_de_minutos != 1:
                diferenca_do_tempo = str(int(diferenca_de_minutos))+ " minutos atrás"
            else:
                diferenca_do_tempo = str(int(diferenca_de_minutos))+ " minuto atrás"
        else:
            if diferenca_de_hora != 1:
                diferenca_do_tempo = str(int(diferenca_de_hora))+ " horas atrás"
            else:
                diferenca_do_tempo = str(int(diferenca_de_hora))+ " hora atrás"            

    elif semanas < 4:
        if semanas != 1:
            diferenca_do_tempo = str(int(semanas))+ " semanas atrás"
        else:
            diferenca_do_tempo = str(int(semanas))+ " semana atrás"

    elif meses < 12 and meses >= 1:
        if meses != 1:
            diferenca_do_tempo = str(int(meses))+ " meses atrás"
        else:
            diferenca_do_tempo = str(int(meses))+ " mes atrás"

    else:
        if anos != 1:
            diferenca_do_tempo = str(int(anos))+ " anos atrás"
        else:
            diferenca_do_tempo = str(int(anos))+ " ano atrás"

    return diferenca_do_tempo

app.run(debug=True)