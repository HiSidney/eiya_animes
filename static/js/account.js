button_editar = document.getElementById('button_editar');
button_salvar = document.getElementById('button_salvar');
button_excluir = document.getElementById('button_excluir');

axios.get('/retornaInfoAccount')
.then(function(response){
    console.log(response.data[0])
    email = document.getElementById('email').value = response.data[0][1];
    nome = document.getElementById('nome').value = response.data[0][0];
    senha = document.getElementById('senha').value = response.data[0][2];
})
.catch(function (error) {
    console.error(error);
})


button_editar.addEventListener('click', function () {
    nome = document.getElementById('nome');
    senha = document.getElementById('senha');
    if (nome.disabled == false) {
        nome.disabled = true;
        senha.disabled = true;
    } else {
        nome.disabled = false;
        senha.disabled = false;
    }
});

button_salvar.addEventListener('click', function () {
    nome = document.getElementById('nome').value;
    senha = document.getElementById('senha').value;
    UserAtualizado = {'nome':nome,'senha':senha}

    axios.post('/novoUsuario', UserAtualizado)
    .then(function(response){
    alert("Adicionado com sucesso!")
    })
    .catch(function (error) {
    console.error(error);
    })
});

button_excluir.addEventListener('click', function () {
    confirmacao = confirm("Realmente deseja excluir esta conta?")
    if (confirmacao == true){
        axios.post('/excluirUsuario')
        .then(function(response){
        alert("Adicionado com sucesso!")
        })
        .catch(function (error) {
        console.error(error);
        })
    } else {
        console.log('cancelado')
    }
});