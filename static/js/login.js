batao_entrada = document.getElementById('button_login')

batao_entrada.addEventListener('click', function () {

  login_mail = document.getElementById('login_mail').value;
  senha = document.getElementById('senha').value;

  Login = {'login_mail':login_mail,'senha':senha}

  axios.post('/login', Login)
  .then(function(response){
//    console.log(response.data);
    if (response.data == 'adm') {
      window.location.href = "http://127.0.0.1:5000/adm"
    } else if (response.data == 'user') {
      window.location.href = "http://127.0.0.1:5000/"
    } else {
      alert('Email ou senha invalido');
    }
  })
  .catch(function(error){
    console.error(error);
    alert("2 - Email ou senha incorretos")
  })
});