#def conecta_ao_banco(driver,server,database):
#    string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database}"
#    return pyodbc.connect(string_conexao)

#cursor = cnxn.cursor()
import pyodbc
from datetime import datetime, timedelta

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-306QNCK\SQLEXPRESS;DATABASE=eiya_animes')
cursor = cnxn.cursor()

def pegar_todas_infos_da_tabela(tabela):
    info = cursor.execute(f"select * from {tabela}").fetchall()
    info = [tuple(row) for row in info]
    return info

def pega_top_10_animes_mais_recentes():
    info = cursor.execute(f"select top(10) * from animes order by data_lancamento_anime desc").fetchall()
    info = [tuple(row) for row in info]
    return info

def pegar_todas_infos_da_tabela_com_desc(tabela):
    info = cursor.execute(f"select * from {tabela} order by data_lancamento_capitulo desc").fetchall()
    info = [tuple(row) for row in info]
    return info

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

def pega_resutados_pesquisa(pesquisa):
    resultado_pesquisa = cursor.execute(f"select * from animes where nome_anime like '%{pesquisa}%'").fetchall()
    resultado_pesquisa = [tuple(row) for row in resultado_pesquisa]
    return resultado_pesquisa

def proximo_id(tabela):
    select_linhas = cursor.execute(f"select count(*) from {tabela}").fetchall()
    novo_id = select_linhas[0][0]+1
    return novo_id

def adiciona_anime_bancoDados(nomeAnime,data_lancamento_anime,logoAnime_cru,dublagem_anime,descricaoAnime,generos):
    logo_anime_cru = logoAnime_cru
    logoAnime = logo_anime_cru.replace('C:\\fakepath','/static/img/logo_animes')
    print(logoAnime)

    id_anime = proximo_id("animes")
#casa 
    cursor.execute(f"insert into animes values('{id_anime}','{nomeAnime}','{data_lancamento_anime}','{logoAnime}','{dublagem_anime}','{descricaoAnime}')")

#escola    cursor.execute(f"insert into animes values('{id_anime}','{nomeAnime}','{data_lancamento_anime}','{criador_anime}','{logoAnime}','{dublagem_anime}','{descricaoAnime}')")

    cursor.commit()
    print('Sucesso ao adicianor o ANIME')

    generos_do_anime = generos
    i = 0
    for i in generos_do_anime:
        cursor.execute(f"insert into ligacao_generos values({id_anime},{i})")
        cursor.commit()
        print('Sucesso ao adicianor os GENEROS do ANIME')

def adiciona_capitulo_bancoDados(anime_que_capitulo_pertencente,temporada_que_capitulo_pertencente,numero_capitulo,video_capitulo,thumbnail):
    data_hora = datetime.today()
    data_e_hora = str(data_hora).split(' ')
    data = data_e_hora[0]
    hora = data_e_hora[1]

    video_capitulo_cru = video_capitulo
    novo_video_capitulo = video_capitulo_cru.replace('C:\\fakepath',f'\\static\\Video\\capitulos\\{anime_que_capitulo_pertencente}\\{temporada_que_capitulo_pertencente}')
    
    cursor.execute(f"insert into capitulos values('{anime_que_capitulo_pertencente}','{temporada_que_capitulo_pertencente}','{numero_capitulo}','{novo_video_capitulo}','{data}','{hora}', '{thumbnail}')")
    cursor.commit()
    print('Sucesso ao adicianor o CAPITULO')

def adicionar_temporada_bancoDados(anime_que_temporada_pertencente,num_temporada,data_lancamento_temporada,trailer):
    id_temporada = proximo_id('temporadas')
    print(data_lancamento_temporada)
    cursor.execute(f"insert into temporadas values({anime_que_temporada_pertencente},{num_temporada},'{data_lancamento_temporada}',{id_temporada})")
    cursor.commit()
    cursor.execute(f"insert into trailers values({anime_que_temporada_pertencente},'{trailer}',{num_temporada})")
    cursor.commit()
    print('Sucesso ao adicionar uma nova TEMPORADA')

def adicionar_genero_bancoDados(nome_genero):
    id_genero = proximo_id('generos')

    cursor.execute(f"insert into generos values('{id_genero}','{nome_genero}'")
    cursor.commit()
    print('Sucesso ao adicionar um novo GENERO')

def pega_nomeAnime_logoAnime_descricao_tabelaAnimes(id_anime):
    animes = cursor.execute(f"select nome_anime,logo_anime,descricao from animes where id_anime = {id_anime}").fetchall()
    animes = [tuple(row) for row in animes]
    return animes

def pega_idCapitulos_dataLancamento_capitulo_tabelaCapitulos(id_anime):
    capitulos = cursor.execute(f"select id_capitulos,data_lancamento_capitulo,num_temporada,id_anime from capitulos where id_anime = {id_anime}").fetchall()
    capitulos = [tuple(row) for row in capitulos]
    return capitulos

def pega_ligacaoAnime_genero(id_anime):
    ligacao_anime_genero = cursor.execute(f"select generos.id_genero,generos.nome_genero from ligacao_generos,generos where ligacao_generos.id_anime = {id_anime} and ligacao_generos.id_genero = generos.id_genero").fetchall()
    ligacao_anime_genero = [tuple(row) for row in ligacao_anime_genero]
    return ligacao_anime_genero

def pega_anime_capitulos(id_anime,id_temporada,id_capitulo):
    capitulos = cursor.execute(f"select animes.id_anime,animes.nome_anime,capitulos.id_capitulos,capitulos.data_lancamento_capitulo,capitulos.video,capitulos.num_temporada from animes,capitulos where animes.id_anime = {id_anime} and capitulos.id_capitulos = {id_capitulo} and capitulos.num_temporada = {id_temporada} and animes.id_anime = capitulos.id_anime").fetchall()
    capitulos = [tuple(row) for row in capitulos]
    return capitulos

def pega_info_tabelaAnime_tabelaCapitulo():
    capitulos = cursor.execute('select capitulos.id_anime,capitulos.num_temporada,capitulos.id_capitulos,capitulos.data_lancamento_capitulo,capitulos.video,animes.nome_anime,capitulos.hora_lancamento_capitulo from capitulos,animes where animes.id_anime = capitulos.id_anime order by data_lancamento_capitulo desc ,hora_lancamento_capitulo desc').fetchall()
    capitulos = [tuple(row) for row in capitulos]
    return capitulos

def pega_anime_por_genero(id_genero):
    animes = cursor.execute(f'select * from animes,ligacao_generos where animes.id_anime = ligacao_generos.id_anime and ligacao_generos.id_genero = {id_genero}').fetchall()
    animes = [tuple(row) for row in animes]
    return animes

def pega_animes_ligacaoGeneros_generos(id_genero):
    animes = cursor.execute(f'select * from animes,ligacao_generos,generos where animes.id_anime = ligacao_generos.id_anime and ligacao_generos.id_genero = generos.id_genero and ligacao_generos.id_genero = {id_genero}').fetchall()
    animes = [tuple(row) for row in animes]
    return animes

def pega_info_user(login):
    resposta = cursor.execute(f"select * from usuarios where email = '{login}'").fetchall()
    resposta = [tuple(row) for row in resposta]
    return resposta

def inserir_cadastro_bancoDados(email,login,senha,):
    cursor.execute(f"insert into usuarios values('{login}','{email}','{senha}','user')")
    cursor.commit()

def conta_numero_de_animes():
    num = cursor.execute(f"select count(*) from animes").fetchall()
    return num

def pega_info_do_historico(email):
    resposta = cursor.execute(f"select animes.nome_anime,historico.data_visualizacao,historico.hora_visualizacao,historico.id_anime,historico.num_temporada,historico.id_capitulo,capitulos.thumbnail from historico,animes,usuarios,capitulos where historico.id_anime = animes.id_anime and historico.id_anime = capitulos.id_anime and historico.num_temporada = capitulos.num_temporada and historico.id_capitulo = capitulos.id_capitulos and historico.email = usuarios.email and usuarios.email = '{email}' order by historico.hora_visualizacao desc, historico.data_visualizacao desc").fetchall()
    resposta = [tuple(row) for row in resposta]
    return resposta

def add_historico_usuario(email,id_anime,id_capitulo):
    data_hora = datetime.today()
    data_e_hora = str(data_hora).split(' ')
    data = data_e_hora[0]
    hora = data_e_hora[1]
    cursor.execute(f"insert into historico values ('{email}',{id_anime},1,{id_capitulo},'{data}','{hora}')")
    cursor.commit()

def quantidade_temporadas(id_anime):
    quant_temporadas = cursor.execute(f"select max(num_temporada) from capitulos where id_anime = {id_anime}").fetchall()
    quant_temporadas = [tuple(row) for row in quant_temporadas]
    quant_temporadas = quant_temporadas[0][0]
    return quant_temporadas

def apaga_historico(email):
    cursor.execute(f"delete historico where email = '{email}'")
    cursor.commit()

def addNovoUsuario(nome,email,senha):
    cursor.execute(f"update usuarios set senha = '{senha}', nome_login = '{nome}' where email = '{email}'")
    cursor.commit()

def excluirUsuario(email):
    cursor.execute(f"delete usuarios where email = '{email}'")
    cursor.commit()

def removeAnimeFavorito(email,id_anime):
    cursor.execute(f"delete animes_salvos where email = '{email}' and id_anime = {id_anime}")
    cursor.commit()

def addAnimeFavorito(email,id_anime):
    cursor.execute(f"insert into animes_salvos values('{email}', {id_anime})")
    cursor.commit()

def verifica_favoritos(email,id_anime):
    resposta = cursor.execute(f"select * from animes_salvos where email = '{email}' and id_anime = {id_anime}").fetchall()
    resposta = [tuple(row) for row in resposta]
    if resposta == []:
        return resposta
    else:
        return resposta[0][0]

def retornaAnimesSalvos(email):
    resposta = cursor.execute(f"select animes.id_anime,animes.nome_anime,animes.logo_anime,animes.dublagem,animes.descricao,animes.data_lancamento_anime from animes_salvos,animes where animes_salvos.id_anime = animes.id_anime and animes_salvos.email = '{email}'").fetchall()
    resposta = [tuple(row) for row in resposta]
    return resposta

def retornaInfoAccount(email):
    resultado = cursor.execute(f"select * from usuarios where email = '{email}'")
    resultado = [tuple(row) for row in resultado]
    return resultado

def quant_capitulos(id_anime, id_temporada):
    resultado = cursor.execute(f"select max(id_capitulos) from capitulos where id_anime = {id_anime} and num_temporada = {id_temporada}").fetchall()
    resultado = [tuple(row) for row in resultado]
    return resultado

def pesquisa_anime_que_capitulo_pertencente(conteudo):
    resultado = cursor.execute(f"select id_anime,nome_anime from animes where nome_anime like '%{conteudo}%' or id_anime like '{conteudo}%' ").fetchall()
    resultado = [tuple(row) for row in resultado]
    return resultado

def buscaTrailer(id_anime):
    resultado = cursor.execute(f"select id_temporada,trailer from trailers where id_anime = {id_anime}").fetchall()
    resultado = [tuple(row) for row in resultado]
    return resultado

