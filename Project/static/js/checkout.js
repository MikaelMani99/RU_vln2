(function(){
    function contactSaveLocalstorage(){
        let name = document.getElementById("contact_name").value;
        let address = document.getElementById("contact_address").value;
        let city = document.getElementById("contact_city").value;
        let postal_code = document.getElementById("contact_post_code").value; 
        let country_element = document.getElementById("contact_country");
        let country = country_element.options[country_element.selectedIndex].value;
        localStorage.setItem("contact_name", name);
        localStorage.setItem("contact_address", address);
        localStorage.setItem("contact_city", city);
        localStorage.setItem("contact_country", country);
        localStorage.setItem("contact_post_code", postal_code);
    }
    function addSaveOnClick(){
        let form = document.getElementById("contact_form");
            form.onsubmit = function(){
                contactSaveLocalstorage();
            }
    }
    function contactLocalStorage(){
        if(localStorage.getItem("contact_name")){
            document.getElementById("contact_name").value = localStorage.getItem("contact_name");
        }
        if(localStorage.getItem("contact_address")){
            document.getElementById("contact_address").value = localStorage.getItem("contact_address");
        }
        if(localStorage.getItem("contact_city")){
            document.getElementById("contact_city").value = localStorage.getItem("contact_city");
        }
        if(localStorage.getItem("contact_post_code")){
            document.getElementById("contact_post_code").value = localStorage.getItem("contact_post_code"); 
        }
        if(localStorage.getItem("contact_country")){
            document.getElementById("contact_country").value = localStorage.getItem("contact_country");
        }
    }
    function paymentSaveLocalstorage(){
        let name = document.getElementById("payment_name").value;
        let exp_end = document.getElementById("payment_exp_date").value;
        let card = document.getElementById("payment_card_nr").value;
        let last_four = card.substring(card.length-4, card.length);
        localStorage.setItem("payment_name", name);
        localStorage.setItem("payment_exp_date", exp_end);
        localStorage.setItem("payment_last_four", last_four);
    }
    function addSaveOnClickPayment(){
        let payment_form = document.getElementById('payment_form')
        payment_form.onsubmit = function(){
            paymentSaveLocalstorage();
        }
    }
    function populateCardInfo(){
        let parent = document.getElementById("card_info");
        let children = [localStorage.getItem("payment_name"), 
                        localStorage.getItem("payment_exp_date"), 
                        localStorage.getItem("payment_last_four")];
        for (let i = 0; i < children.length; i++){
            let el = document.createElement("div")
            el.setAttribute('class', 'review-row');
            el.innerText = children[i]
            parent.appendChild(el);
        } 
        
    }
    if(window.location.pathname === "/checkout/"){
        addSaveOnClick();
        contactLocalStorage();
    }
    if(window.location.pathname === "/checkout/payment/"){
        addSaveOnClickPayment();
    }
    if(window.location.pathname === "/checkout/review/"){
        populateCardInfo();
    }
})();