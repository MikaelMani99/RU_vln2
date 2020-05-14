(function(){
    let url = "/cart/"
    function updateCartInput(){
        let cart = localStorage.getItem("cart");
        let input_cart = document.getElementById("cart_storage");
        input_cart.value = cart;
        try{
            document.getElementById("checkout_cart").value = cart;
        }catch{
            return
        }
    }
    function updateCartSize(){
        let cart = JSON.parse(localStorage.getItem("cart"));
        let nav_cart = document.getElementById("nav_cart");
        let sum = 0;
        try{
            for(let i=0; i < cart.length; i++){
                sum += cart[i].amount;
            }
            // there's probably a better solution for this
            nav_cart.innerHTML= "Cart ("+ sum + ") <img src= \"/static/images/chest.svg\">";
        }catch{
            console.log("cart is empty");
        }
    }

    function initCart(){
        if(localStorage.getItem("cart") == null){
            localStorage.setItem("cart", JSON.stringify([]));
        }
    }
    function addToCart(product, amount = 1){
        let cart = JSON.parse(localStorage.getItem("cart"));
        // get the amount
        try{
            amount = parseInt(document.getElementById("q"+product.substring(1)).value);
            if(amount === NaN){
                return 
            }
        }catch{
            amount = 1;
        }
        // find the index, if it's not in cart returns -1
        product_inedx = cart.findIndex((obj => obj.id == product));
        if(product_inedx === -1){
            cart.push({id:product, amount:amount});
        }else{
            cart[product_inedx].amount += amount;
        }
        localStorage.setItem("cart", JSON.stringify(cart));
        updateCartInput();
        updateCartSize();
    }
    function removeFromCart(product, amount = 1){
        let cart = JSON.parse(localStorage.getItem("cart"));
        // find the index, if it's not in cart returns -1
        product_inedx = cart.findIndex((obj => obj.id == product));
        product_id = cart[product_inedx].id;
        cart[product_inedx].amount -= amount;
        if(cart[product_inedx].amount <= 0){
            cart.splice(product_inedx, 1);
        }
        localStorage.setItem("cart", JSON.stringify(cart));
        deleteElementIfZero(product_id.substring(1));
        updateCartInput();
        updateCartSize();
    }
    function deleteElementIfZero(id){
        let el = document.getElementById("inf"+id);
        if(el.value == 0){
            let to_remove = el.parentElement.parentElement.parentElement;  
            to_remove.classList.add("hidden");
        }
    }
    function addOnClick(){
        let buttons = document.getElementsByClassName("btn-cart");
        for(let i=0; i < buttons.length; i++){
            buttons[i].onclick = function(){
                addToCart(buttons[i].id);
                setTotalPrice();
                getTotalPrice();
            }
        }
    }
    function chestClicked(){
        let cart = localStorage.getItem("cart");
        let chest_btn = document.getElementById("nav_cart");
        chest_btn.onclick = function(){
            fetch('/chest/update', {method: 'POST', body: cart});
        }
    }
    function addAmountClick(){
        let add = document.getElementsByClassName("inc");
        let rem = document.getElementsByClassName("dec");

        for(let i=0; i < add.length; i++){
            add[i].onclick = function(){
                addToCart("p" + add[i].id.substring(1));
                setTotalPrice();
                getTotalPrice();
            }
            rem[i].onclick = function(){
                removeFromCart("p" + rem[i].id.substring(1));
                setTotalPrice();
                getTotalPrice();
            }
        }
    }
    function setTotalPrice(){
        try{
            let items = document.getElementsByClassName("product-price");
            let total_price = 0;
            for(let i = 0; i < items.length; i++){
                let price = (items[i].innerText).substring(1);
                let id = "inf" + (items[i].id).substring(5);
                let amount = document.getElementById(id).value;
                total_price += amount * price;
            }
            localStorage.setItem("total_price", total_price.toFixed(2));
        }catch{
            return;
        }
        
    }
    function getTotalPrice(){
        try{
            total_price = localStorage.getItem("total_price");
            let el = document.getElementById("total_price");
            el.innerHTML = total_price;
        }catch{
            return;
        }
        
    }
    if(window.location.pathname === "/chest/"){
        setTotalPrice();
        getTotalPrice();
        addAmountClick();
    }
    chestClicked();
    updateCartSize();
    initCart();
    addOnClick();
    updateCartInput();
})();

