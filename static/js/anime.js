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