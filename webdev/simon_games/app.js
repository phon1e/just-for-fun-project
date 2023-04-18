var gamePattern = [];
var buttonColors = ['red','blue', 'green', 'yellow'];
var userClickedPattern=[];

var started = false;
var lv = 0;

$(document).keypress(function(){
    if(!started){
        $("#level-title").html("level"+ ' ' + lv);
        nextSeq();
        started = true;
    }
  
});

$(".btn").click(function() {
    var userChosenColor = $(this).attr("id");
    userClickedPattern.push(userChosenColor);

    playAudio(userChosenColor);
    animatePress(userChosenColor);

    checkAns(userClickedPattern.length-1);

});

checkAns = (curLv) =>{
    if(gamePattern[curLv] === userClickedPattern[curLv]){
        // console.log("success");
        
        if(userClickedPattern.length === gamePattern.length){
            setTimeout(() => {
                nextSeq();
            }, 1000);
        }
    }else{
        // console.log("wrong");
        playAudio("wrong");

        $("body").addClass("game-over");
        setTimeout(() => {
            $("body").removeClass("game-over");
        }, 200);

        $("#level-title").html("Game Over, Press Any Key to Restart")
        startOver();
    }
}

nextSeq=()=>{
    userClickedPattern = [];
    lv++;
    $("#level-title").text("level " + lv);

    var max = 4;
    var randomNum = (Math.floor(Math.random() *(max)));
    var randomChosenColor = buttonColors[randomNum];
    gamePattern.push(randomChosenColor);

    $('#' + randomChosenColor).fadeIn(100).fadeOut(100).fadeIn(100);
    playAudio(randomChosenColor);

}


playAudio = (name) => {
    var btnSound = new Audio('sounds/' + name +'.mp3');
    btnSound.play();
}


animatePress = (curColor) => {
    $('#' + curColor).fadeOut(100).fadeIn(100);
    $('#'+ curColor).addClass("pressed")

    setTimeout(() => {
        $("#" + curColor).removeClass("pressed");
      }, 100);
}

startOver =() =>{
    lv = 0;
    gamePattern= [];
    started = false;
}