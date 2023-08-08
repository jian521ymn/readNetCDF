// 在 preload 脚本中。
const { ipcRenderer, contextBridge, dialog  } = require('electron')
let i = 1
let webSocket = {}

contextBridge.exposeInMainWorld('electronAPI', {
    initWebSocket: (socket) => {
        webSocket = socket
    },
    openFile: ()=> ipcRenderer.invoke('dialog:openFile')
})
console.log(dialog,'dialog');

