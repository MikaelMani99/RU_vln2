(function () {
  // I hate this language
  // this function finds out where in the website it is 
  // and highlights the navbar accordingly 
  function highlightNavbar(){
    let path_split = window.location.pathname.split('/');
    if(path_split.length === 2 && path_split[1] === ""){
      document.getElementById("home").classList.add("active");
    }else{
      try{
        let highlight_this = document.getElementById(path_split[1]);
        highlight_this.classList.add("active");
      }catch{
        console.log("nothing to highlight");
      }
    }
  }
  highlightNavbar();

  //Adds some classes to the user login forms and register login forms created by django
  function addClassToLoginFormInputs(){
    if(window.location.href === "http://localhost:8000/profile/login") {

      let usernameInput = document.getElementById("id_username");
      let passwordInput = document.getElementById("id_password");

      usernameInput.classList.add("login-input");
      usernameInput.classList.add("user-input");
      passwordInput.classList.add("login-input");
      passwordInput.classList.add("pass-input");

      usernameInput.placeholder = "Username";
      passwordInput.placeholder = "Password";
    }
  }
  addClassToLoginFormInputs();

  function addClassToRegisterFormInputs(){
    if(window.location.href === "http://localhost:8000/profile/register") {
      let usernameInput = document.getElementById("id_username");
      let registerPasswordInput1 = document.getElementById("id_password1");
      let registerPasswordInput2 = document.getElementById("id_password2");

      usernameInput.classList.add("login-input");
      usernameInput.classList.add("user-input");

      registerPasswordInput1.classList.add("login-input");
      registerPasswordInput1.classList.add("pass-input");

      registerPasswordInput2.classList.add("login-input");
      registerPasswordInput2.classList.add("pass-input");

      usernameInput.placeholder = "Username";
      registerPasswordInput1.placeholder = "Password";
      registerPasswordInput2.placeholder = "Confirm Password";
    }
  }
  addClassToRegisterFormInputs();

  $(".qty-button").on("click", function() {

    var $button = $(this);
    var oldValue = $button.parent().find("input").val();

    if ($button.text() == "+") {
        var newVal = parseFloat(oldValue) + 1;
      } else {
     // Don't allow decrementing below zero
      if (oldValue > 0) {
        var newVal = parseFloat(oldValue) - 1;
      } else {
        newVal = 0;
      }
    }

    $button.parent().find("input").val(newVal);

  });
  // clear the localstorage if logged out
  function clearLocalStorage(){
    let logout = document.getElementById("logout");
    logout.onclick = function(){
      window.localStorage.clear();
    }
  }
  clearLocalStorage();
})();

$(document).ready(function () {
  $('#apply-button').on('click', function (e) {
    e.preventDefault();
    let params = document.location.search;
    $.ajax({
      url: '/search/'+params,
      type: 'POST',
      data: $('form').serialize(),
      dataType: 'json',
      success: function (data) {
        let newHTML = $.map(data['products'], function (p) {
          return `<div class="product">
                        <a href="/product/${ p.id }">
                            <div class="product_img">
                                <img src="${ p.firstImage }">
                                <div class="discountRibbon banner${ p.on_sale }">Discount ${ p.discount }</div>
                            </div>
                            <div class="product-info product-category"> ${ p.category }</div>
                            <div class="product-info product-name"> ${ p.name }</div>
                            <div class="product-info product-price"> <p class="sale-${ p.on_sale }">${ p.price }</p></div>             
                            <div class="product-info product-price display-sale-price-${ p.on_sale }"> ${ p.discount_price }</div>
                        </a>
                        <button id="p${ p.id }" type="submit" class="btn btn-primary btn-cart cart-button" action>Plunder</button>
                  </div>`
          });
          $('.products').html(newHTML.join(''));
      },
      error: function (xhr, status, error) {
        // TODO: Show toastr
        console.error(error);
      }

    });
  });
});