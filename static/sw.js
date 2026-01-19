const CACHE_NAME = 'kiis-app-v1';
const ASSETS_TO_CACHE = [
    '/',
    '/static/manifest.json',
    '/static/images/grid-1x2-fill.svg',
    'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
    'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css'
];

// インストール時にキャッシュする
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => cache.addAll(ASSETS_TO_CACHE))
    );
});

// 通信時にキャッシュがあればそれを使い、なければ取りに行く
self.addEventListener('fetch', (event) => {
    // API（バスのデータ）はキャッシュせず、毎回最新を取りに行く
    if (event.request.url.includes('/api/')) {
        return;
    }

    event.respondWith(
        caches.match(event.request)
            .then((response) => response || fetch(event.request))
    );
});