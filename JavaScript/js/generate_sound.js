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
    var count = binary.length;

    for(var i = 0; i < count; i++){
        
        if(binary[i] == 1){
            frequency = 1000;
            start(frequency);
            await sleep(100);
        }
        else if (binary[i] == 0){
            frequency = 4000;
            start(frequency);
            await sleep(100);
        }

    }

}

// Generate Sound
let context,
	oscillator,
    contextGain,
    type = 'sine',
    x = 1,
    frequency;

function start(frequency){
    context = new AudioContext();
    oscillator = context.createOscillator();
    contextGain = context.createGain();

    oscillator.frequency.value = frequency;
    oscillator.type = type;
    oscillator.connect(contextGain);
    contextGain.connect(context.destination);
    oscillator.start(0);
    stop();
}

function stop(){
    console.log(333, contextGain);
    contextGain.gain.exponentialRampToValueAtTime(0.00001, context.currentTime + 1);
}

function reproduzir() {
    
    var synth = new Tone.FMSynth().toMaster()
    var binary = document.getElementById("ti2").value;
    var count = binary.length;
    /*
    for(var i = 0; i < count; i++){
        
        if(binary[i] == 1){
            synth.triggerAttackRelease('C4', 0.5, i);
            console.log('reproduzindo: ' + i);
        }
        else if (binary[i] == 0){
            synth.triggerAttackRelease('B4', 0.5, i);
            console.log('reproduzindo: ' + i);
        }

    }
    */
    //schedule a series of notes, one per second
    synth.triggerAttackRelease('C4', 0.5, 0)
    synth.triggerAttackRelease('E4', 0.5, 1)
    synth.triggerAttackRelease('G4', 0.5, 2)
    synth.triggerAttackRelease('B4', 3, 3)
    
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