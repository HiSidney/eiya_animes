servidor = "http://127.0.0.1:5000";
rota_cadastro = "/cadastro";
url_cadastro = servidor+rota_cadastro;

document.getElementById('button_novo_usuario').addEventListener('click', function () {
    login = document.getElementById('login').value;
    email = document.getElementById('email').value;
    senha = document.getElementById('senha').value;
    confirmarSenha = document.getElementById('confirmarSenha').value;
    Cadastro = {'login':login,'email':email,'senha':senha,'confirmarSenha':confirmarSenha}
  
    axios.post(url_cadastro, Cadastro)
    .then(function(response){
      console.log(response.data);
      alert("Cadastrado com sucesso!")
    })
    .catch(function(error){
      console.error(error);
      alert("Erro")
    })
  });