console.log('Hello world')

var updateBtns = document.getElementsByClassName('update-cart')

for(i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId', productId,'User', user ,'Action', action)
        if(user === 'AnonymousUser'){
            Swal.fire({
                icon:'error',
                title: 'Nyan cat disse que você só pode fazer pedidos com login!',
                width: 600,
                padding: '3em',
                color: '#dd6a72',
                backdrop: `
                  rgba(255, 0, 0, 0.4)
                  url("/images/nyan-cat-1.gif")
                  center top
                  no-repeat
                `
              }); 
        }else{
            updateUserOrder(productId = productId,action = action)
        }
    })
}

function updateUserOrder(productId,action){

    // Essa função ela servira para atualizar os items dentro do pedido do use

    console.log('User esta logado ! Ele agora e capaz de enviar dados!')
    var url = 'http://127.0.0.1:8000/cart/updateitem/'
    // Url = Seria a url la do backend para a qual essa resposta sera enviada
    // WARNING- EM DEPLOY - VAI PRECISAR ALTERAR
    fetch(url,{
        method:'POST',
        // Metodo a ser utilizado de envio, nesse caso vai ser um post method
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        // So definindo o conteudo que vai ser enviado nesse caso vai ser um json
        body:JSON.stringify({"productId":productId,"action":action})
        // Conteudo da resposta nesse caso o id do produto e a ação
    })

    // Isso daki seria a promessa de que a resposta json será retornada
    .then((response) =>{
        return response.json()

    })
    // Retornando a resposta em Json
    .then((data) =>{
        console.log('Dados que vieram do backend ',data)
        location.reload()
        // Recarrega a pagina depois que tivemos sucesso na chamadas
    })
    // Mostrando os dados retornados

}

