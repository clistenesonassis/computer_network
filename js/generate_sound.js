// Convert binary
function convert() {
    var output = document.getElementById("ti2");
    var input = document.getElementById("ti1").value;
    output.value = "";
    for (var i = 0; i < input.length; i++) {
        output.value += input[i].charCodeAt(0).toString(2) + " ";
    }
}

// Delay
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function imprime(){
    var binary = document.getElementById("ti2").value;
    var count = binary.length - 1;
    for(var i = 0; i < count; i++){
        if(binary[i] == 1){
            start();
            await sleep(100);
        }
    }
}

// Generate Sound
let context,
	oscillator,
    contextGain;

function start(){
    context = new AudioContext();
    oscillator = context.createOscillator();
    contextGain = context.createGain();

    oscillator.type = 'square';
    oscillator.connect(contextGain);
    contextGain.connect(context.destination);
    oscillator.start(0);
    stop();
}

function stop(){
    console.log(333, contextGain);
    contextGain.gain.exponentialRampToValueAtTime(0.00001, context.currentTime + 1);
}



/*
var recorder = document.getElementById('recorder');
var player = document.getElementById('player');

recorder.addEventListener('change', function(e) {
    var file = e.target.files[0];
    // Do something with the audio file.
    player.src =  URL.createObjectURL(file);
});
*/