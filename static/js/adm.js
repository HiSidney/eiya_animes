servidor = "http://127.0.0.1:5000";
rota_adm = "/adm";

url_adm = servidor+rota_adm;
//console.log(url_adm);

//NOVO ANIME
document.getElementById('button_anime').addEventListener('click',function () {
    nomeAnime = document.getElementById('nome_anime').value;
    data_lancamento_anime = document.getElementById('data_lancamento_anime').value;
    criador_anime = document.getElementById('criador_anime').value;
    logoAnime = document.getElementById('logo_anime').value;
    dublagem_anime = document.getElementById('dublagem_anime').value;
    descricaoAnime = document.getElementById('descricao').value;

    checkboxes = document.querySelectorAll('input[name="generos"]:checked');
    generos = [];
    Array.from(checkboxes).map(i => generos.push(parseInt(i.value)));
    console.log(generos)

    Anime = {'tipoCadastro':'Anime','nomeAnime':nomeAnime,'data_lancamento_anime':data_lancamento_anime, 
    'criador_anime':criador_anime,'logoAnime':logoAnime,'dublagem_anime':dublagem_anime,'generos':generos,
    'descricaoAnime':descricaoAnime}
    
    axios.post(url_adm, Anime)
    .then(function(response){
    //console.log(response.data);
    alert(response.data," adicionado com sucesso!")
    })
    .catch(function (error) {
    // manipula erros da requisição
    console.error(error);
  })
});

//NOVO CAPITULO
document.getElementById('button_capitulo').addEventListener('click', function () {
    anime_que_capitulo_pertencente = document.getElementById('anime_que_capitulo_pertencente').value;
    temporada_que_capitulo_pertencente = document.getElementById('temporada_que_capitulo_pertencente').value;
    numero_capitulo = document.getElementById('numero_capitulo').value;
    video_capitulo = document.getElementById('video_capitulo').value;
    
    Capitulo = {'tipoCadastro':'Capitulo','anime_que_capitulo_pertencente':anime_que_capitulo_pertencente,
    'temporada_que_capitulo_pertencente':temporada_que_capitulo_pertencente,'numero_capitulo':numero_capitulo,
    'video_capitulo':video_capitulo}

    axios.post(url_adm, Capitulo)
      .then(function(response){
    //  console.log(response.data);
      alert("Capítulo adicionado com sucesso!")
      
      })
      .catch(function (error) {
      // manipula erros da requisição
      console.error(error);
    })
});

//NOVA TEMPORADA
document.getElementById('button_temporada').addEventListener('click', function (){
    anime_que_temporada_pertencente = document.getElementById('anime_que_temporada_pertencente').value;
    num_temporada = document.getElementById('num_temporada').value;
    data_lancamento_temporada = document.getElementById('data_lancamento_temporada').value;
    trailer_temporada = document.getElementById('trailer_temporada').value;

    Temporada = {'tipoCadastro':'Temporada','anime_que_temporada_pertencente':anime_que_temporada_pertencente,
    'num_temporada':num_temporada,'data_lancamento_temporada':data_lancamento_temporada,'trailer_temporada':trailer_temporada}

    axios.post(url_adm, Temporada)
    .then(function(response){
    //console.log(response.data);
    alert("Temporada adicionado com sucesso!")
    })
    .catch(function (error) {
    // manipula erros da requisição
    console.error(error);
  })
});

//NOVO GENERO
document.getElementById('button_genero').addEventListener('click', function () {
  nome_genero = document.getElementById('nome_genero').value;
  Genero = {'tipoCadastro':'Genero','nome_genero':nome_genero}

  axios.post(url_adm, Genero)
    .then(function(response){
    //console.log(response.data);
    alert("Gênero adicionado com sucesso!")
    })
    .catch(function (error) {
    // manipula erros da requisição
    console.error(error);
    })
});

anime_que_capitulo_pertencente = document.getElementById('anime_que_capitulo_pertencente');
anime_que_capitulo_pertencente.addEventListener('keyup', function () {
  console.log(anime_que_capitulo_pertencente.value)
  Conteudo = {"anime_que_capitulo_pertencente":anime_que_capitulo_pertencente.value}
  
  if (anime_que_capitulo_pertencente.value == ''){
    document.getElementById('dropdown-content-search-search').style.display = 'none';
  } else{
    axios.post('pesquisa_anime_que_capitulo_pertencente', Conteudo)
    .then(function(response){
      document.getElementById('ul').innerHTML = '';
        response.data.forEach(element => {
          console.log(element[1]);
            document.getElementById('dropdown-content-search-search').style.display = 'block';
        
            let li = document.createElement('li');
            ul.insertBefore(li, ul.firstChild);

            let titlo = document.createElement('p');
            text = document.createTextNode('('+element[0]+') '+element[1]);
            titlo.appendChild(text);
            li.appendChild(titlo);
        })
    })
    .catch(function(error){
      console.error(error);
    })
  }
})