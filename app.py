from flask import Flask,render_template,request,jsonify
app = Flask(__name__)

import pyodbc

#print(pyodbc.drivers())
def conecta_ao_banco(driver,server,database):
    string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database}"
    return pyodbc.connect(string_conexao)

cnxn = conecta_ao_banco('SQL Server','DESKTOP-306QNCK\SQLEXPRESS','eiya_animes')
print('Conexão bem sucedida')
cursor = cnxn.cursor()



@app.route('/')
def home():
    generos = pegar_generos()
    return render_template('home.html', generos=generos)

@app.route('/base')
def base():
    generos = pegar_generos()
    return render_template('base.html', generos=generos)

@app.route('/adm', methods=['GET', 'POST'])
def adm():
    generos = pegar_generos()

    if request.method == 'POST':
        req = request.get_json()
        print(req)

        if req['tipoCadastro'] == 'Anime':
            print(req['logoAnime'])
            logoAnime_cru = req['logoAnime']
            logoAnime = logoAnime_cru.replace('C:\\fakepath','/static/img/logo_animes')

            id_anime = proximo_id("animes")

            if req['nomeAnime'] == '' or req['data_lancamento_anime'] == '' or req['criador_anime'] == '' or logoAnime == '' or req['dublagem_anime'] == '' or req['descricaoAnime'] == '' or req['generos'] == '':
                print('erro. falta info para o insert')
            else:
                cursor.execute(f"insert into animes values('{id_anime}','{req['nomeAnime']}','{req['data_lancamento_anime']}','{req['criador_anime']}','{logoAnime}','{req['dublagem_anime']}','{req['descricaoAnime']}')")
                cursor.commit()
                print('Sucesso ao adicianor o ANIME')

                generos_do_anime = req['generos']
                i = 0
                for i in generos_do_anime:
                    print(id_anime,' e: ',i)
                    cursor.execute(f"insert into ligacao_generos values('{id_anime}','{i}')")
                    cursor.commit()
                    print('Sucesso ao adicianor os GENEROS do ANIME')

            info_anime = pegar_info_bancoDados('animes',id_anime)
            print(info_anime)
            return req['tipoCadastro']
        

        elif req['tipoCadastro'] == 'Capitulo':
            anime_que_capitulo_pertencente = req['anime_que_capitulo_pertencente']
            temporada_que_capitulo_pertencente = req['temporada_que_capitulo_pertencente']

            video_capitulo_cru = req['video_capitulo']
            video_capitulo = video_capitulo_cru.replace('C:\\fakepath',f'/static/Video/capitulos/{anime_que_capitulo_pertencente}/{temporada_que_capitulo_pertencente}')

            cursor.execute(f"insert into capitulos values('{req['anime_que_capitulo_pertencente']}','{req['temporada_que_capitulo_pertencente']}','{req['numero_capitulo']}','{req['data_lancamento_capitulo']}','{video_capitulo}')")
            cursor.commit()
            print('Sucesso ao adicianor o CAPITULO')

            info_capitulo = pegar_info_bancoDados('capitulos',req['numero_capitulo'])
            print(info_capitulo)
            return req['tipoCadastro']
        
        
        elif req['tipoCadastro'] == 'Temporada':
            anime_que_temporada_pertencente = req['anime_que_temporada_pertencente']
            img_temporada_cru = req['img_temporada']
            img_temporada = img_temporada_cru.replace('C:\\fakepath',f'/static/img/Temporadas\{anime_que_temporada_pertencente}')

            id_temporada = proximo_id('temporadas')

            cursor.execute(f"insert into temporadas values('{req['anime_que_temporada_pertencente']}','{req['num_temporada']}','{req['data_lancamento_temporada']}','{img_temporada}'")
            cursor.commit()
            print('Sucesso ao adicionar uma nova TEMPORADA')
            
            info_temporada = pegar_info_bancoDados('temporadas',id_temporada)
            print(info_temporada)

            return req['tipoCadastro']
        
        else:
            id_genero = proximo_id('generos')

            cursor.execute(f"insert into generos values('{id_genero}','{req['nome_genero']}'")
            cursor.commit()
            print('Sucesso ao adicionar um novo GENERO')

            return req['tipoCadastro']
    else:
        print('Fora')
        return render_template('adm.html',generos = generos)


@app.route('/animes/<id_anime>')
def anime(id_anime):

    CAnime = {}
    animes = cursor.execute(f'select nome_anime,logo_anime,descricao from animes where id_anime = {id_anime} ').fetchall()
    animes = [tuple(row) for row in animes]

    CAnime['NomeAnime'] = animes[0][0]
    CAnime['logo_anime'] = animes[0][1]
    CAnime['descricao'] = animes[0][2]
    CAnime['id_anime'] = id_anime

    capitulos = cursor.execute(f"select id_capitulos,data_lancamento_capitulo from capitulos where id_anime = {id_anime}").fetchall()
    capitulos = [tuple(row) for row in capitulos]

    generos = pegar_generos()

    ligacao_anime_genero = cursor.execute(f"select generos.id_genero,generos.nome_genero from ligacao_generos,generos where ligacao_generos.id_anime = {id_anime} and ligacao_generos.id_genero = generos.id_genero").fetchall()
    ligacao_anime_genero = [tuple(row) for row in ligacao_anime_genero]
    print(ligacao_anime_genero)

    return render_template('anime.html', anime = CAnime,capitulos = capitulos,generos = generos,ligacao_anime_genero = ligacao_anime_genero)


@app.route('/animes/<id_anime>/cap-<id_capitulo>')
def page_assistir_cap(id_anime,id_capitulo):

    capitulos = cursor.execute(f"select animes.id_anime,animes.nome_anime,capitulos.id_capitulos,capitulos.data_lancamento_capitulo,capitulos.video from animes,capitulos where animes.id_anime = {id_anime} and capitulos.id_capitulos = {id_capitulo} and animes.id_anime = capitulos.id_anime").fetchall()
    print(capitulos)

    return render_template('video.html', capitulos=capitulos)



@app.route('/animes')
def todos_animes():
    generos = pegar_generos()
    return render_template('todos_animes.html',generos=generos)

@app.route('/retornaAnimes')
def retornaAnimes():
    animes = cursor.execute('select * from animes').fetchall()
    animes = [tuple(row) for row in animes]

    return jsonify(animes)



@app.route('/animes/genero/<id_genero>')
def generos(id_genero):
    return f"Genero {id_genero}"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    if request.method == 'POST':
        req = request.get_json()
        print(req)
        if req[2] == req[3]:
            return 'Bom'
        else:
            return 'error'

    else:
        return render_template('cadastro.html')

@app.route('/historico')
def historico():
    return render_template('historico.html')







def pegar_info_bancoDados(tabela,pk):
    match tabela:
        case 'animes':
            campo = 'id_anime'
        case 'capitulos':
            campo = 'id_capitulo'
        case 'temporadas':
            campo = 'id_temporada'
        case 'generos':
            campo = 'id_genero'

    resposta = cursor.execute(f"select * from {tabela} where '{campo}'='{pk}'").fetchall
    return resposta

def pegar_generos():
    generos = cursor.execute(f"select * from generos").fetchall()
    generos = [tuple(row) for row in generos]
    return generos

def proximo_id(tabela):
    select_linhas = cursor.execute(f"select count(*) from {tabela}").fetchall()
    novo_id = select_linhas[0][0]+1
    return novo_id

app.run(debug=True)