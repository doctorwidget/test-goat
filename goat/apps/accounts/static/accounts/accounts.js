/** mock object for use with Qunit testing **/
/*global $ */

var initialize = function (navigator) {
   $('#id_login').on('click', function() {
         navigator.id.request();
   });
};

window.Goat = {
   Accounts: {
       initialize: initialize
   }
}
