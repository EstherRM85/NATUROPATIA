window.addEventListener('scroll', function() {
    let animacion = document.getElementById('animado');
    let posicionObj1 = animacion.getBoundingClientRect().top;
    console.log(posicionObj1);
    let tamañoDePantalla = window.innerHeight / 2;
    console.log('tamPantalla: ' + tamañoDePantalla);

    if (posicionObj1 < tamañoDePantalla) {

        animacion.style.animation = 'slidein 2s ease-out'
    } else {
        animacion.style.animation = ''

    }
})













/*function apareceScroll() {
    var html = document.getElementsByTagName("html")[0];
    var elementosAparece = document.getElementsByClassName("imgover");

    document.addEventListener("wheel", function() {
        var topVent = html.scrollTop;
        for (i = 0; i < elementosAparece.length; i++) {
            var topelemAparece = elementosAparece[i].offsetTop;
            if (topVent > topelemAparece - 400) {
                elementosAparece[i].style.opacity = 1;
            }
        }
    })

}
apareceScroll();*/

/*$(document).ready(function() {
    $("#banner").css({ "height": $(window).height() + "px" });
    var flag = false;
    var scroll;

    $(window).scroll(function() {
        scroll = $(window).scrollTop();
        if (scroll > 200) {
            if (!flag) {
                $("#logo").css({ "margin-top": "-5px", "width": "50px", "height": "50px" });
                flag = true;
            }
        } else {
            if(flag){
                $("#logo").css({ "margin-top": "150px", "width": "250px", "height": "250px" });
                flag=false;s
            }
            

        }

    });
});*/








/*var text = $(".split");

var split = new SplitText(text);

function random(min, max) {
    return (Math.random() * (max - min)) + min;
}

$(split.chars).each(function(i) {
    TweenMax.from($(this), 2.5, {
        opacity: 0,
        x: random(-500, 500),
        y: random(-500, 500),
        z: random(-500, 500),
        scale: .1,
        delay: i * .02,
        yoyo: true,
        repeat: -1,
        repeatDelay: 10
    });
});*/