var audioContext, microphoneStream;

function getUserMedia_Success(mediaStream) {
    microphoneStream = audioContext.createMediaStreamSource(mediaStream);
    //Conecta o microfone à saída
    microphoneStream.connect(audioContext.destination);
    return true;
}

function getUserMedia_Error(error) {
    alert("Erro ao obter acesso ao microfone: " + error);
    return true;
}

//Valida a capacidade do browser de capturar mídia
if (!navigator.getUserMedia) {
    navigator.getUserMedia = (navigator.webkitGetUserMedia ||
        navigator.mozGetUserMedia ||
        navigator.msGetUserMedia);
}
if (!navigator.getUserMedia) {
    alert("Aparentemente seu browser não possui a API necessária para capturar mídia :(");
}

//Tenta criar o contexto de áudio para capturar e reproduzir o áudio
audioContext = (window.AudioContext ? new AudioContext() : (window.webkitAudioContext ? new webkitAudioContext() : null));
if (!audioContext) {
    alert("Aparentemente seu browser não possui a API necessária para trabalhar com áudio! :(");
} else {
    //Tenta obter acesso ao microfone
    navigator.getUserMedia({ audio: true }, getUserMedia_Success, getUserMedia_Error);
}