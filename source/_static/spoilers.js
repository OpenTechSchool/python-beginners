(function ($) {
    'use strict';
    $.fn.showHide = function (options) {

        //default vars for the plugin
        var defaults = {
            speed: 500,
            easing: '',
            changeText: true,
            showText: 'Show',
            hideText: 'Hide'

        };
        options = $.extend(defaults, options);

        $(this).hide().data('hidden', true);

        $(this).last().after('<button class="btn btn-warning _show_hide" type="button">' + options.showText + '</button>');

        $('._show_hide').click(function () {
            var me = $(this);
            var el = $(this).prevUntil("h3");
            el.slideToggle(options.speed, function() {
                if (options.changeText) {
                    if (el.data('hidden')) {
                        el.data('hidden', false);
                        me.text(options.hideText);
                    } else {
                        el.data('hidden', true);
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
    $(".solution h3").nextUntil("h3").showHide();
  });
})(jQuery);
