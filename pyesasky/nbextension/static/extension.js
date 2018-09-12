define(function() {
    "use strict";

    window['requirejs'].config({
        map: {
            '*': {
                'pyesasky': 'nbextensions/pyesasky/index',
            },
        }
    });
    // Export the required load_ipython_extention
    return {
        load_ipython_extension : function() {}
    };
});
