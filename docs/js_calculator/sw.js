const CACHE_NAME = "v1_cache_js_calculator";
const urlsToCache = [
    "./",
    "./pages/fallback.html",
    "./?umt_source=web_app_manifest",
    "/docs/js_calculator/assets/icons/16px_icon.png",
    "/docs/js_calculator/assets/icons/32px_icon.png",
    "/docs/js_calculator/assets/icons/48px_icon.png",
    "/docs/js_calculator/assets/icons/64px_icon.png",
    "/docs/js_calculator/assets/icons/128px_icon.png",
    "/docs/js_calculator/assets/icons/144px_icon.png",
    "/docs/js_calculator/assets/icons/192px_icon.png",
    "/docs/js_calculator/assets/icons/256px_icon.png",
    "/docs/js_calculator/assets/icons/512px_icon.png",
    "/docs/js_calculator/assets/icons/1024px_icon.png",
    "/docs/js_calculator/assets/icons/maskable_icon_x192.png",
    "/docs/js_calculator/js/Display.js",
    "/docs/js_calculator/js/Calculator.js",
    "/docs/js_calculator/js/index.js",
    "/docs/js_calculator/style.css",
    "/docs/js_calculator/manifest.json",
    "https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;700&display=swap"
]

// ServiceWorker Cache Install
self.addEventListener('install', e => {
    e.waitUntil(
        caches.open(CACHE_NAME).then(
            cache => cache.addAll(urlsToCache).then(
                () => skipWaiting()
            ).catch(
                err => console.log(err)
            )
        )
    )
})

// Cache verification
self.addEventListener('activate', e => {
    e.waitUntil(
        caches.keys().then(
            cacheNames => {
                return Promise.all(
                    cacheNames.map(
                        cacheName => {
                            if(cacheWhitelist.indexOf(cacheName) === -1) {
                                return caches.delete(cacheName)
                            }
                        }
                    )
                )
            }
        ).then(
            () => clients.claim()
        )
    )
})

// fetch that allows download de info
self.addEventListener('fetch', e => {
    e.respondWith(
        caches.match(e.request).then(
            res => {
                if(res) {
                    return res
                }

                return fetch(e.request)
            }
        ).catch(
            () => caches.match("./pages/fallback.html")
        )
    )
})