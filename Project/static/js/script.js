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
})();

$(document).ready(function () {
  $('.apply').on('click', function (e) {
    e.preventDefault();
    let params = document.location.search;
    $.ajax({
      url: '/search/'+params,
      type: 'POST',
      data: $('form').serialize(),
      dataType: 'json',
      success: function (data) {
        console.log(data);
        let newHTML = $.map(data['products'], function (p) {
          return `<div class="product">
                        <a href="/product/${ p.id }">
                            <div class="product_img">
                                <img src="${ p.firstImage }">
                            </div>
                            <h4> ${ p.name }</h4>
                            <p> ${ p.price }</p>
                        </a>
                        <button type="button" class="btn btn-primary">plunder</button>
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
