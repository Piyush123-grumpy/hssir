var updateBtn=document.getElementsByClassName("update-cart")
for(var i=0;i<updateBtn.length;i++){
    updateBtn[i].addEventListener('click',function(){
        var productId=this.dataset.product;
        var action=this.dataset.action;
        console.log('productId:',productId,'action:',action);
        console.log('USER',user)
        if(user=='AnonymousUser'){
            console.log("User not logged in")
        }
        else{
            User_Order(productId,action)
        }
    })

}
function User_Order(productId,action){
    console.log('User logged sending data')
    var url='/update_item/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId,'action':action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:',data)
        location.reload()
    })
}