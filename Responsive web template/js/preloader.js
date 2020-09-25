var preload = document.createElement("div");
    preload.className = "preloader";
    preload.innerHTML =
      '<p class="hello"></p><div id="preloader"><div id="loader"></div></div>';
    document.body.appendChild(preload);
    window.addEventListener("load", function() {
      preload.className += " fade";
      setTimeout(function() {
        preload.style.display = "none";
      }, 1000);
    });