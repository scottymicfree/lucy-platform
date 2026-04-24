const { contextBridge } = require('electron');

contextBridge.exposeInMainWorld('lucy', {
  version: '0.1.0'
});
