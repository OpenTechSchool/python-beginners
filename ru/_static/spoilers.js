(function ($) {
    'use strict';
    $.fn.showHide = function (options) {

        //default vars for the plugin
        var defaults = {
            speed: 400,
            easing: 'swing',
            changeText: true,
            showText: 'Show',
            hideText: 'Hide'

        };
        options = $.extend(defaults, options);

        var button = $('<button class="btn btn-info btn-sm _show_hide" type="button"></button>');
        button.text(options.showText);
        button.data('el', $(this));

        $(this).last().after(button);
        $(this).hide();

        button.click(function () {
            var me = $(this);
            var el = me.data('el');
            el.slideToggle(options.speed, options.easing, function() {
                if (options.changeText) {
                    if (el.is(':visible')) {
                        me.text(options.hideText);
                    } else {
                        me.text(options.showText);
                    }
                }
            });
        });
    };
})(jQuery);

(function ($) {
  $(document).ready(function() {
    'use strict';
    $('.solution h3').each(function() {
        $(this).nextAll().showHide();
    });
  });
})(jQuery);
