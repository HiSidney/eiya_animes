document.getElementById('button_novo_usuario').addEventListener('click', function () {
    login = document.getElementById('login').value;
    email = document.getElementById('email').value;
    senha = document.getElementById('senha').value;
    confirmarSenha = document.getElementById('confirmarSenha').value;
    Cadastro = {'login':login,'email':email,'senha':senha,'confirmarSenha':confirmarSenha}
  
    axios.post('/cadastro', Cadastro)
    .then(function(response){
      console.log(response.data);
      if (response.data === 'ok'){
        alert("Cadastrado com sucesso!")
        window.location.href = "http://127.0.0.1:5000/"
      } else {
        alert("erro")
      }
    })
    .catch(function(error){
      console.error(error);
      alert("Erro 2")
    })
  });