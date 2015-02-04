/** mock object for use with Qunit testing **/
/*global $ */

var initialize = function (navigator, user, token, urls) {
   $('#id_login').on('click', function() {
         navigator.id.request();
   });

    navigator.id.watch({
        loggedInUser: user,
        onlogin: function(assertion) {
            $.post(
                urls.login,
                    {
                        assertion: assertion,
                        csrfmiddlewaretoken: token
                    })
                .done(function () {
                  window.location.reload();
                })
                .fail(function () {
                    navigator.id.logout();
                });
        },
        onlogout: function() {}
    });

};

window.Goat = {
   Accounts: {
       initialize: initialize
   }
};

