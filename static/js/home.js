//criar elemento no pagina todos os animes
sidebar = document.getElementById('sidebar');
sidebar.innerHTML = '';
fundo2 = document.getElementById('fundo2');
fundo2.innerHTML = '';

axios.get('/retornaAnimes_e_Capitulos')
.then(function (animes) {
  animes.data[0].forEach(element => {
//    console.log(element)
    let div = document.createElement("div");
    div.setAttribute("class", "conteiner-anime");
    sidebar.appendChild(div);

    let link1 = document.createElement("a");
    link1.setAttribute("href",'/animes/'+ element[0])
    let img = document.createElement("img");
    img.setAttribute("src", element[2]);
    link1.appendChild(img);
    div.appendChild(link1);

    let link2 = document.createElement("a");
    link2.setAttribute("href", '/animes/'+element[0])
    nome_anime = document.createTextNode(element[1]);
    link2.appendChild(nome_anime);
    div.appendChild(link2);
  });
 
  animes.data[1].forEach(element => {
    //console.log(element)
    let div = document.createElement("div");
    div.setAttribute("class", "conteiner");
    fundo2.appendChild(div);
  
    let link1 = document.createElement("a");
    link1.setAttribute("href","/animes-"+ element[0]+"/tem-"+element[1]+"/cap-"+ element[2])

    let img = document.createElement("img");
    img.setAttribute("src",element[4]);
    img.setAttribute("alt",element[5]);

    link1.appendChild(img);
    div.appendChild(link1);

    let link2 = document.createElement("a");
    link2.setAttribute("href","/animes-"+ element[0]+"/tem-"+element[1]+"/cap-"+ element[2]);
    nome_anime = document.createTextNode(element[5]);
    link2.appendChild(nome_anime);
    div.appendChild(link2);

    let text_num_ep = document.createElement("p");
    num_ep = document.createTextNode("Episódio "+element[2]);
    text_num_ep.appendChild(num_ep);
    div.appendChild(text_num_ep);
    
    let texto_data_lancamento = document.createElement("p");
    data_lancamento = document.createTextNode(element[3]);
    texto_data_lancamento.appendChild(data_lancamento);
    texto_data_lancamento.setAttribute("title", element[6]);
    div.appendChild(texto_data_lancamento);
  });

})
.catch(function (error) {
  // manipula erros da requisição
  console.error(error);
})