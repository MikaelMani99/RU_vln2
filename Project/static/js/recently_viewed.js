(function(){
    let path = window.location.pathname.split("/");
    if(path[1] === "product"){
        let id = path[2];
        if(localStorage.getItem("recently_viewed") == undefined){
            localStorage.setItem("recently_viewed", "[]");
        }
        let recently_viewed = JSON.parse(localStorage.getItem("recently_viewed"));
        // mynd, nafn, long description, og id
        let name = document.getElementsByClassName("product-detail-name")[0].innerText;
        let description = document.getElementsByClassName("product-detail-description")[0].innerText;
        let image = document.getElementsByClassName("product-detail-img")[0].src;
        let obj = {'id': id,
                   'name': name, 
                   'description': description,
                   'image': image};

        recently_viewed.push(obj);
        localStorage.setItem("recently_viewed", JSON.stringify(recently_viewed));
    }
})();