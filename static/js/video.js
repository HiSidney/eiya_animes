botoes = document.querySelectorAll('.botao')
botoes.forEach(element => {
    element.addEventListener('click',function(e){
        botao = e.target.id;

        id_capitulo = e.target.getAttribute('id_capitulo')
        id_anime = e.target.getAttribute('id_anime')
        id_temporada = e.target.getAttribute('id_temporada')
        id_capitulo = parseInt(id_capitulo)
        quant_capitulos = document.getElementById('quant_capitulos').textContent;

        if (botao == 'botao_esquerda' & id_capitulo != 1){
            window.location.href = "http://127.0.0.1:5000/animes-"+id_anime+"/tem-"+id_temporada+"/cap-"+(id_capitulo-1);
        }
        else if (botao == 'botao_esquerda' & id_capitulo == 1){
            window.location.href = "http://127.0.0.1:5000/animes-"+id_anime+"/tem-"+id_temporada+"/cap-"+id_capitulo;
        } else if (botao == 'botao_direita' & id_capitulo == quant_capitulos){
            window.location.href = "http://127.0.0.1:5000/animes-"+id_anime+"/tem-"+id_temporada+"/cap-"+id_capitulo;
        } else {
            window.location.href = "http://127.0.0.1:5000/animes-"+id_anime+"/tem-"+id_temporada+"/cap-"+(id_capitulo+1);
        }
    });
});
