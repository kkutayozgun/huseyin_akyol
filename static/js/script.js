(function ($) {
    "use strict";

    // Windows load

    $(window).on("load", function () {

        // Site loader 

        $(".loader-inner").fadeOut();
        $(".loader").delay(200).fadeOut("slow");

    });


    // Back-top

    $(function () {
        $(window).scroll(function () {
            if ($(this).scrollTop() > 100) {
                $('.scroll-to-top').addClass('active');
            } else {
                $('.scroll-to-top').removeClass('active');
            }
        });
    });


    // Scroll to

    $('a.scroll').smoothScroll({
        speed: 800,
        offset: -71
    });


    //Popup video

    $('.popup-youtube, .popup-vimeo').magnificPopup({
        disableOn: 700,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false
    });


    // Jarallax setup


    jarallax(document.querySelectorAll('.jarallax'), {
        speed: 0.5,
        disableParallax: /iPad|iPhone|iPod|Android/,
        disableVideo: /iPad|iPhone|iPod|Android/
    });


    // swiperjs - sliders
    $(function () {
        var swiper = new Swiper(".homeswiper", {
            autoplay: {
                delay: 3000,
                disableOnInteraction: false,
            },
            loop: true,
            loopFillGroupWithBlank: true,
            loopPreventsSlide: false,
            effect: "fade",
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
            },
        });
        var homeswiper_text = new Swiper(".homeswiper_text", {
            autoplay: {
                delay: 3000,
                disableOnInteraction: false,
            },
            loop: true,
            loopFillGroupWithBlank: true,
            loopPreventsSlide: false,
            effect: "fade",
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
            },
        });
        var groupslider = new Swiper(".groupslider", {
            slidesPerGroup: 1,
            loop: true,
            loopFillGroupWithBlank: true,
            loopPreventsSlide: false,
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            }
        });
        var journeysliderSmall = new Swiper(".journeyslider", {
            slidesPerView: 1,
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
            },
        });

        const imgHolder = $('#popup-img-holder')

        $('#imgPopup').on('show.bs.modal', function (e) {
            imgHolder[0].src === e.relatedTarget.src || imgHolder.attr('src', e.relatedTarget.src)
        })

    });

})(jQuery);