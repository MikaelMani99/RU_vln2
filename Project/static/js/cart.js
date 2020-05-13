(function(){
    let url = "/cart/"
    function updateCartInput(){
        let cart = localStorage.getItem("cart");
        let input_cart = document.getElementById("cart_storage");
        input_cart.value = cart;
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
        cart[product_inedx].amount -= amount;
        if(cart[product_inedx].amount <= 0){
            cart.splice(product_inedx, 1);
        }
        localStorage.setItem("cart", JSON.stringify(cart));
        updateCartInput();
        updateCartSize();
    }
    function addOnClick(){
        let buttons = document.getElementsByClassName("btn-cart");
        for(let i=0; i < buttons.length; i++){
            buttons[i].onclick = function(){
                addToCart(buttons[i].id);
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
            }
            rem[i].onclick = function(){
                removeFromCart("p" + rem[i].id.substring(1));
            }
        }
    }
    
    addAmountClick();
    chestClicked();
    updateCartSize();
    initCart();
    addOnClick();
    updateCartInput();
})();

