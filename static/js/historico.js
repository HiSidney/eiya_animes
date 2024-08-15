excluir_historico = document.getElementById('excluir_historico');

excluir_historico.addEventListener('click', function () {
    confirmacao = confirm("Realmente deseja excluir seu histórico?")
    if (confirmacao == true){
        axios.get('/apagar_historico')
        .then(function (response){
            console.log(response.data)
            if (response.data == "ok") {
                window.location.reload();
            } else {
                console.error(response.data);
            }
        })
        .catch(function(error){
            console.error(error);
        });
    } else {
        alert.alert("Histórico não foi excluido.")
    }
        
})
