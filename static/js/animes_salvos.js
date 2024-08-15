//criar elemento no pagina todos os animes
fundo2 = document.getElementById('fundo2')
fundo2.innerHTML = ''

axios.get('/retorna_animes_salvos')
.then(function (response) {
//  console.log(response.data);
    response.data.forEach(element => {
    console.log(element)
    let div = document.createElement("div");
    div.setAttribute("class", "conteiner-anime");
    fundo2.appendChild(div);

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
})
.catch(function (error) {
  // manipula erros da requisição
  console.error(error);
})