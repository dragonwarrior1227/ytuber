function GetSettings() {
    0 == localStorage.getItem("Onlike") || "" == localStorage.getItem("Onlike") || null == localStorage.getItem("Onlike") ? $("#onlike").prop("checked", !0) : $("#onlike").prop("checked", !1), 0 == localStorage.getItem("Onsubscribe") || "" == localStorage.getItem("Onsubscribe") || null == localStorage.getItem("Onsubscribe") ? $("#onsubscribe").prop("checked", !0) : $("#onsubscribe").prop("checked", !1), 0 == localStorage.getItem("Oncomment") || "" == localStorage.getItem("Oncomment") || null == localStorage.getItem("Oncomment") ? $("#oncomment").prop("checked", !0) : $("#oncomment").prop("checked", !1), 0 == localStorage.getItem("Onlikecomment") || "" == localStorage.getItem("Onlikecomment") || null == localStorage.getItem("Onlikecomment") ? $("#onlikecomment").prop("checked", !0) : $("#onlikecomment").prop("checked", !1)
}
$("#onlike").on("change", function() {
    $(this).is(":checked") ? chrome.storage.sync.set({
        Onlike: 0
    }, function() {
        localStorage.setItem("Onlike", "0")
    }) : chrome.storage.sync.set({
        Onlike: 1
    }, function() {
        localStorage.setItem("Onlike", "1")
    }), GetSettings()
}), $("#onsubscribe").on("change", function() {
    $(this).is(":checked") ? chrome.storage.sync.set({
        Onsubscribe: 0
    }, function() {
        localStorage.setItem("Onsubscribe", "0")
    }) : chrome.storage.sync.set({
        Onsubscribe: 1
    }, function() {
        localStorage.setItem("Onsubscribe", "1")
    }), GetSettings()
}), $("#oncomment").on("change", function() {
    $(this).is(":checked") ? chrome.storage.sync.set({
        Oncomment: 0
    }, function() {
        localStorage.setItem("Oncomment", "0")
    }) : chrome.storage.sync.set({
        Oncomment: 1
    }, function() {
        localStorage.setItem("Oncomment", "1")
    }), GetSettings()
}), $("#onlikecomment").on("change", function() {
    $(this).is(":checked") ? chrome.storage.sync.set({
        Onlikecomment: 0
    }, function() {
        localStorage.setItem("Onlikecomment", "0")
    }) : chrome.storage.sync.set({
        Onlikecomment: 1
    }, function() {
        localStorage.setItem("Onlikecomment", "1")
    }), GetSettings()
}), GetSettings();