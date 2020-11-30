var CACHE_NAME = 'tcache'

var urlsToCache = [
    '/',
    '/static/modelo/css/style.css',
    '/static/modelo/css/Style_juegos.css',

    


]

//instalacion
self.addEventListener('install',function(event){
    event.waitUntil(
        caches.open(CACHE_NAME)
        .then(function(cache){
            console.log('Cache creado exitosamente');
            return cache.addAll(urlsToCache);
        })
    );
});

//Intersectadores
self.addEventListener('fetch',function(event){
    event.respondWith(
        caches.match(event.request).then(function(response){
            return fetch(event.request)
            .catch(function(rsp){
                return response;
            });
        })
    );

});