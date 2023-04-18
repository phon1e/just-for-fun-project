function initiate(){
    for(var i=0; i< document.querySelectorAll(".drum").length; i++){
        document.querySelectorAll("button")[i].addEventListener("click", function(){
            var btnName = this.innerHTML;
            makeSound(btnName);

            buttonAnimation(btnName);
        });
    }
    document.addEventListener("keydown", function(e){
        makeSound(e.key);
        buttonAnimation(e.key);
    });
}



function makeSound(key){
    switch (key) {
        case "w":     
            var crash = new Audio('sounds/crash.mp3');
            crash.play();
            break;

        case "a":     
            var t1 = new Audio('sounds/tom-1.mp3');
            t1.play();
            break;

        case "s":     
            var t2 = new Audio('sounds/tom-2.mp3');
            t2.play();
            break;

        case "d":     
            var t3 = new Audio('sounds/tom-3.mp3');
            t3.play();
            break;
            
        case "j":     
            var t4 = new Audio('sounds/tom-4.mp3');
            t4.play();
            break;

        case "k":     
            var snare = new Audio('sounds/snare.mp3');
            snare.play();
            break;

        case "l":     
            var kick = new Audio('sounds/kick-bass.mp3');
            kick.play();
            break;

        default: console.log();
            break;
    }

}

function buttonAnimation(curKey){

    var activeBtn = document.querySelector("." + curKey);
    activeBtn.classList.add("pressed");

    setTimeout(function(){
        activeBtn.classList.remove("pressed");
    }, 100);

}

initiate();