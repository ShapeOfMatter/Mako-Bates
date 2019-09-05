(clientName)=>{
    if(typeof window[clientName] === 'undefined'){

        const origin = (uri)=>{
            const parser = window.document.createElement('a');
            parser.href = uri;
            return `${parser.protocol}//${parser.host}`;
        };

        const loadTool = (uri)=>{
            return new Promise((resolve, reject)=>{
                const tag = window.document.createElement('iframe');
                tag.src = uri;
                tag.width = 0;
                tag.height = 0;
                tag.style = "visibility: hidden";
                window.addEventListener("message",
                    (e)=>{
                        if(e.origin == origin(uri)){ //it may be possible to refine the origin check.
                            resolve(e.data);
                        }
                    }, 
                    false);
                window.document.body.appendChild(tag);
            });   // add error handler?
        };

        const requestOverPort = (port, resource)=>{
            return new Promise((resolve, reject)=>{
                disposableChannel = new MessageChannel();
                disposableChannel.port1.onmessage = (e)=>{
                    resolve(e.data);
                    disposableChannel.port1.close();
                };
                port.postMessage(
                    {
                        resource: resource,
                        port: disposableChannel.port2
                    },
                    disposableChannel.port2);
            });
        };

        const defaultClient = document.currentScript.getAttribute("data-default") || '';
        const gotClientPort = loadTool(`https://402receipts.info/client_uri_getter_version_N1.html#${defaultClient}`)
            .then(
                (uri)=>{
                    return loadTool(uri);
                }, 
                (reason)=>{
                    //handle db-read error
                });

        window[clientName] = {
            fetch: (request)=>{
                return gotClientPort
                    .then((clientPort)=>{
                        return requestOverPort(
                            clientPort,
                            {
                                url: request.url,
                                method: request.method
                            });
                    }).then((receipt)=>{
                        return window.fetch(
                            request,
                            {
                                headers: new Headers({ 'Receipts-Receipt': receipt });
                            });
                    });
            }
        }

    }
}(document.currentScript.getAttribute("data-name") || "FOTR")

