onmessage = function(e) {
    console.log('Message received from main script')
    var workerResult = new FileReader()
    workerResult.readAsText("../../dbStore.txt")
    console.log('Load file')
    postMessage(workerResult)
}