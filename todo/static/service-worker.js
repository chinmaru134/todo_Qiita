"use strict"

if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js', { scope: "/" })
        .then((reg) => {
            console.log('Service worker registered.', reg);
        });
}