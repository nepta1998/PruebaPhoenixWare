self.addEventListener("install", event => {
this.skipWaiting();
event.waitUntil(
caches.open(staticCacheName)
.then(cache => {
return cache.addAll(filesToCache);
})
)
});