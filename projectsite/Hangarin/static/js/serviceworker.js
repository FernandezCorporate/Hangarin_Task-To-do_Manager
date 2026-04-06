self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open('hangarin-cache-v1').then(function(cache) {
            return cache.addAll([
            '/',
            '/static/css/stylesheet.css',
            'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js',
            'https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css',
            ]);
        })
    );
});
self.addEventListener('fetch', function(e) {
    e.respondWith(
        caches.match(e.request).then(function(response) {
            return response || fetch(e.request);
        })
    );
});