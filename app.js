let cart = {}
let prices = {}

fetch("/menu")
.then(res => res.json())
.then(data => {
    let menu = document.querySelector(".menu")
    data.forEach(item => {
        prices[item[0]] = item[2]
        let block = `
        <div class="item">
        <img src="${item[3]}">
        <h3>${item[1]}</h3>
        <p>${item[2]} сум</p>
        <div class="counter">
            <button onclick="minus(${item[0]})">-</button>
            <span id="${item[0]}">0</span>
            <button onclick="plus(${item[0]})">+</button>
        </div>
        </div>`
        menu.innerHTML += block
    })
})

function plus(id){
    if(!cart[id]) cart[id]=0
    cart[id]++
    document.getElementById(id).innerText = cart[id]
}

function minus(id){
    if(cart[id]>0) cart[id]--
    document.getElementById(id).innerText = cart[id]
}

function openCart(){
    let cartDiv = document.querySelector(".cart-container")
    cartDiv.style.display = "block"

    let itemsDiv = document.getElementById("cart-items")
    itemsDiv.innerHTML = ""
    let total = 0

    for(let id in cart){
        if(cart[id]>0){
            let item = document.querySelector(`span[id='${id}']`).parentNode.parentNode.querySelector("h3").innerText
            itemsDiv.innerHTML += `<p>${item} x${cart[id]}</p>`
            total += cart[id]*prices[id]
        }
    }

    document.getElementById("total").innerText = total
}

function submitOrder(){
    let name = document.getElementById("name").value
    let phone = document.getElementById("phone").value
    let address = document.getElementById("address").value

    fetch("/order", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({cart, name, phone, address})
    })
    .then(res=>res.json())
    .then(data=>{
        alert("Заказ отправлен!")
        location.reload()
    })
}