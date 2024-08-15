function troca_ep_info_trailer(tipo){
    console.log(tipo)
    const ep = document.getElementById("ep");
    const ep_click = document.getElementById("ep_click");
    const desc = document.getElementById("desc");
    const desc_click = document.getElementById("desc_click");
    const trai = document.getElementById("trai");
    const trai_click = document.getElementById("trai_click");

    const episodios = document.getElementById("episodios");
    const descricao = document.getElementById("descricao");
    const trailer = document.getElementById("trailer");

    if (tipo =="ep") {
        episodios.style.display = "block";
        descricao.style.display = "none";
        trailer.style.display = "none";

        ep.id = "ep_click";
        if (desc == null){
            desc_click.id = "desc";
        } else if (trai == null){
            trai_click.id = "trai";
        } else if (desc_click == null) {
            desc.id = desc.id;
        } else {
            trai.id = trai.id
        }
    } else if(tipo =="desc") {
        descricao.style.display = "block";
        episodios.style.display = "none";
        trailer.style.display = "none";

        desc.id = "desc_click";
        if (ep == null){
            ep_click.id = "ep";
        } else if (trai == null){
            trai_click.id = "trai";
        } else if (ep_click == null) {
            ep.id = ep.id;
        } else {
            trai.id = trai.id
        }
    } else if (tipo == "trai") {
        trailer.style.display = "block";
        episodios.style.display = "none";
        descricao.style.display = "none";

        trai.id = "trai_click";
        if (desc == null){
            desc_click.id = "desc";
        } else if (ep == null){
            ep_click.id = "ep";
        } else if (desc_click == null) {
            desc.id = desc.id;
        } else {
            ep.id = ep.id
        }
    }
}

salvar_anime = document.getElementById('anime_salvo').checked;
span_id_anime = document.getElementById('span_id_anime').textContent;
ValorFavoritar = {'key':salvar_anime, 'id_anime':parseInt(span_id_anime)}

axios.post('/verifica_favoritos', ValorFavoritar)
.then(function(response){
//console.log(response.data);
if (response.data === "True") {
    salvar_anime = document.getElementById('anime_salvo').checked = true;
} else {
    salvar_anime = document.getElementById('anime_salvo').checked = false;
}
})
.catch(function (error) {
// manipula erros da requisição
console.error(error);
})

document.getElementById('anime_salvo').addEventListener('click', function () {
    salvar_anime = document.getElementById('anime_salvo').checked;
    span_id_anime = document.getElementById('span_id_anime').textContent;
    ValorFavoritar = {'key':salvar_anime, 'id_anime':parseInt(span_id_anime)}

    axios.post('/salva_animes',ValorFavoritar)
    .then(function(response){
    console.log(response.data);
    })
    .catch(function (error) {
    // manipula erros da requisição
    console.error(error);
    })
})
