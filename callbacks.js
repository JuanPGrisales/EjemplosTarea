function download(x, callbackFin, ... arguments){
    console.log('Comienzo de la descarga ', x)
    setTimeout(() => 
    {
        console.log('Fin de la descarga')
        if(callbackFin)
            callbackFin(arguments.shift(2))
    }
    , 3000)
}



console.log('Comienzo del Programa')
var url = 'farrell.com/listaVideos.txt'
var urlVideo = 'farrell.com/detalleVideo.txt'
download
(
    url, 
    download,
        urlVideo,
        ()=>{console.log('Fin del Programa')}, 
        download,
            urlVideo,
            ()=>{console.log('Fin del Programa')}, 
            download,
                urlVideo,
                ()=>{console.log('Fin del Programa')}, 
                download,
                    urlVideo,
                    ()=>{console.log('Fin del Programa')}, 
                    download,
                        urlVideo,
                        ()=>{console.log('Fin del Programa')}, 
                        download,
                            urlVideo,
                            ()=>{console.log('Fin del Programa')}, 
                            download,
                                urlVideo,
                                ()=>{console.log('Fin del Programa')}, 
                                download,
                                    urlVideo,
                                    ()=>{console.log('Fin del Programa')}, 
                                    download,
                                        urlVideo,
                                        ()=>{console.log('Fin del Programa')}, 
                                        download,
                                            urlVideo,
                                            ()=>{console.log('Fin del Programa')}, 
                                            download,
                                                urlVideo,
                                                ()=>{console.log('Fin del Programa')}, 
                                                download,
                                                    urlVideo,
                                                    ()=>{console.log('Fin del Programa')}, 
                                                    download,
                                                        urlVideo,
                                                        ()=>{console.log('Fin del Programa')}
    
)
