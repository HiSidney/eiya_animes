servidor = "http://127.0.0.1:5000";
rota_login = "/login";
url_login = servidor+rota_login;


document.getElementById('button_login').addEventListener('click', function () {
    login_mail = document.getElementById('login_mail');
    senha = document.getElementById('senha');
    Login = {'login_mail':login_mail,'senha':senha}
  
    axios.post(url_login, Login)
    .then(function(response){
      console.log(response.data);
      alert("Sucesso!")
    })
    .catch(function(error){
      console.error(error);
      alert("Login/Email ou senha incorretos")
    })
  });