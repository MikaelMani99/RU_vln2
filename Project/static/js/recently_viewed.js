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
    if(path[1] === "profile"){
        let ul_el = document.getElementById("recently_viewed");
        let recently_viewed = JSON.parse(localStorage.getItem("recently_viewed"));
        for (let i = 0; i < recently_viewed.length; i++) {
            let new_el = document.createElement("li");
            new_el.classList.add("recent-product-row");
            let image = recently_viewed[i]['image'];
            let id = recently_viewed[i]['id'];
            let name = recently_viewed[i]['name'];
            let description = recently_viewed[i]['description'];
            new_el.innerHTML =  "<a class =\"recent-image\" href=\"/product/"+ id + "\">" +
                                "<img src=\""+ image+"\">" + "</a>" +
                                "<div class =\"product-info-profile\">" +
                                "<a class =\"recent-name\" href=\"/product/"+ id + "\">"+ name +"</a>" +
                                "<p class =\"recent-description\">" + description + "</p>" + "</div>"
            ul_el.appendChild(new_el);
        } 
    }
})();