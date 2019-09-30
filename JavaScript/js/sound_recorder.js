/*
var gum = navigator.getUserMedia || 
          navigator.webkitGetUserMedia ||
          navigator.mozGetUserMedia || 
          navigator.msGetUserMedia;

var audioContext,
    microphoneStream,
    recorder = null;

gum({ video:false, audio: true }, getUserMedia_Success, getUserMedia_Error);

function getUserMedia_Success(mediaStream) {
    microphoneStream = audioContext.createMediaStreamSource(mediaStream);
    //Conecta o microfone à saída
    microphoneStream.connect(audioContext.destination);
    recorder = new Recorder(microphoneStream);
    recorder.record();
    return true;
}

function getUserMedia_Error(error) {
    alert("Erro ao obter acesso ao microfone: " + error);
    return true;
}
*/

//window.addEventListener("load", initMp3Player, false);

function initMp3Player(){

    // inserindo audio.
    let audio = document.getElementById('player');
    audio.src = "./assets/audio1.mp3";

    
    
    let audioCTX = new AudioContext(); 
    let analyser = audioCTX.createAnalyser();

    let source = audioCTX.createMediaElementSource(audio);
    source.connect(analyser);
    source.connect(audioCTX.destination);

    analyser.fftSize = 2048;
    let bufferLength = analyser.fftSize;
    let dataArray = new Uint8Array(bufferLength);

    // INSERE NO dataArray A FORMA DE ONDA
    analyser.getByteTimeDomainData(dataArray);

    for (let i = 0; i < bufferLength; i++) {
        console.log(dataArray[i]);
    }

}