search = document.getElementById('search_conteudo');
login = document.getElementById('mostrarInfoUser');
cadastro = document.getElementById('button-login-cadastro');

axios.get('/base')
.then(function (response){
//    console.log(response.data)
    if (response.data != "naoExiste"){
//        console.log(response)
        login.href = "#";
        login.id = "novo_mostrarInfoUser"
        cadastro.href = "#";
        document.getElementById("nome_usuario").innerHTML = response.data["nome"];
    } else {
//        console.log(response.data)
        login.href = "/login";
        login.id = "mostrarInfoUser"
        cadastro.href = "/cadastro";
    }
})
.catch(function(error){
    console.error(error);
    alert(error)
});

login.addEventListener('click', function () {
    const div = document.getElementById('sidebar_info_usuario');
    const display = window.getComputedStyle(div, null).display;
    if (display === 'none' && login.id === "novo_mostrarInfoUser") { 
        div.style.display = 'block';
    } else {
        div.style.display = 'none';
    } 
});

document.addEventListener('click', function(event) {
    const div = document.getElementById('sidebar_info_usuario');
    const isClickedInsideDiv = div.contains(event.target); // Verifica se o clique foi dentro do 'sidebar_info_usuario'
    const isClickedInsideLogin = login.contains(event.target)
//    const display = window.getComputedStyle(div, null).display;

    if (!isClickedInsideLogin) { // Se o clique não foi dentro do 'sidebar_info_usuario', oculta-o
        if (div.style.display == 'none') {
            div.style.display = 'block';
        }
        if (isClickedInsideDiv === false) {
            div.style.display = 'none'
        }
    } 
});

search.addEventListener('keyup', function (){
    Conteudo = {"search":search.value}
    if (search.value == ''){
        document.getElementById('dropdown-content-search-search').style.display = 'none';
    } else {
        axios.post('/pesquisa_dinamica', Conteudo)
        .then(function(response){
//        console.log(response.data);
        document.getElementById('ul').innerHTML = '';
        response.data.forEach(element => {
            document.getElementById('dropdown-content-search-search').style.display = 'block';
        
            let li = document.createElement('li');
            ul.insertBefore(li, ul.firstChild);

            let div = document.createElement('div');
            div.setAttribute('class', 'div_pesquisa')
            li.appendChild(div)

            let link = document.createElement('a');
            link.setAttribute('href','/animes/'+element[0]);
            div.appendChild(link)

            let div2 = document.createElement('div');
            div2.setAttribute('class','div2')
            link.appendChild(div2)

            let img = document.createElement('img');
            img.setAttribute('src',element[2]);
            img.setAttribute('class','img_pesquisa')
            div2.appendChild(img);

            let titlo = document.createElement('p');
            text = document.createTextNode(element[1]);
            titlo.appendChild(text);
            div2.appendChild(titlo);
        });
    })
    .catch(function(error){
        console.error(error);
    })
    }
});

axios.get('/ver')
.then(function(resposta) {
  if (resposta.data['status'] === 'adm' ){
    ul_recebe_info_usuario = document.getElementById("ul_recebe_info_usuario");

    let list = document.createElement("li");
    ul_recebe_info_usuario.appendChild(list);

    let link_adm = document.createElement("a");
    link_adm.setAttribute("href", "/adm");
    text_adm = document.createTextNode("Adm Page");
    link_adm.appendChild(text_adm);
    list.appendChild(link_adm);
  }
})
.catch(function(error){
  console.error(error)
});