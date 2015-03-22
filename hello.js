var page = require('webpage').create();
var showdown = 'http://play.pokemonshowdown.com/';
var output = 'example.png';
var username = 'zarly';
var password = 'phantom';

openPage(showdown, function() {
    var login;
    page.evaluate(function() {
        login = document.querySelector("button[name='login']");
    });
    console.log("login: " + login);
    eventFire(login,'click');
    window.setTimeout(function () {
        page.evaluate(function() {
            console.log(document.querySelector("form").innerHTML);
        });
        phantom.exit();
    }, 1000);
});


function openPage(url,callback) {
    console.log("Loading URL: "+url);
    page.open(url, function(status) {
        if (status!=="success") {
            console.log("Page load failed");
            phantom.exit();
        }
        console.log("Page load succeeded");
        callback();
    });
}


function eventFire(el, etype){
    if (el.fireEvent) {
        el.fireEvent('on' + etype);
    } else {
        var evObj = document.createEvent('Events');
        evObj.initEvent(etype, true, false);
        el.dispatchEvent(evObj);
    }
}