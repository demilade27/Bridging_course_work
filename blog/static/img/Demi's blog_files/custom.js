(function ($) {
    "use strict";
    
    /* CALCULATE PAGE TITLE NEGATIVE MARGIN */
    var adjustPageTitle = function () {
        var distance = $('#django-main-container > .container').offset().left - 295;
        $('#django-main-container').find('.django-page-title').css('margin-right', -distance);
        $('#django-main-container').find('.django-page-title').css('padding-right', distance);
        $('#django-main-container').find('.django-page-title').css('opacity', 1);
    };

    /* HORIZONTAL CARD IMAGES */
    var cardImages = function () {
        $('body').find(".card-horizontal-right").each(function () {
            if ($(this).attr('data-img')) {
                var card_img = $(this).data('img');
                $(this).css('background-image', 'url("' + card_img + '")');
            }
        });
    };
    
    /* GO TO TOP BUTTON */
    $(window).on('scroll', function () {
        if ($(this).scrollTop() > 300) {
            $("#django-gototop").css('bottom', 0);
        } else {
            $("#django-gototop").css('bottom', '-50px');
        }
    });
    
    $("#django-gototop").on('click', function (e) {
        e.preventDefault();
        $("html, body").animate({
            scrollTop: 0
        }, 500);
        return false;
    });
    
    /* FULLSCREEN SEARCH */
    $("#django-open-search").on('click', function (e) {
        e.preventDefault();
        $("#django-fullscreen-search").fadeIn(200);
    });
    
    $("#django-close-search").on('click', function (e) {
        e.preventDefault();
        $("#django-fullscreen-search").fadeOut(200);
    });

    /* MAIN MENU */
    $('#django-main-menu').find(".django-menu-ul > li > a").on('click', function () {
        var nxtLink = $(this).next();
        if ((nxtLink.is('ul')) && (nxtLink.is(':visible'))) {
            nxtLink.slideUp(300);
            $(this).removeClass("django-menu-up").addClass("django-menu-down");
        }
        if ((nxtLink.is('ul')) && (!nxtLink.is(':visible'))) {
            $('#django-main-menu').find('.django-menu-ul > li > ul:visible').slideUp(300);
            nxtLink.slideDown(300);
            $('#django-main-menu').find('.django-menu-ul > li:has(ul) > a').removeClass("django-menu-up").addClass("django-menu-down");
            $(this).addClass("django-menu-up");
        }
        if (nxtLink.is('ul')) {
            return false;
        } else {
            return true;
        }
    });
    
    /* MOBILE MENU */
    $("#django-menu-toggle").on('click', function () {
        $("#django-social-cell,#django-main-menu").toggle();
    });
    
    /* EVENTS */
    $(document).ready(function () {
        adjustPageTitle();
        cardImages();
        $('#django-main-menu').find('.django-menu-ul > li:has(ul) > a').addClass("django-menu-down");
        $('body').find('select').addClass('custom-select');
        $('body').find('.django-masonry-grid').css('opacity', '1');
    });
    
    $(window).on('resize orientationchange', function () {
        adjustPageTitle();
    });
    
    $(window).on('load', function () {
        var grid = $('body').find('.django-masonry-grid');
        salvattore.rescanMediaQueries(grid);
    });
    
})(jQuery);