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