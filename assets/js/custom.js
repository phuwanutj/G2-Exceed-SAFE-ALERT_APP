/**	
	* Template Name: Kindle
	* Version: 1.0	
	* Template Scripts
	* Author: MarkUps
	* Author URI: http://www.markups.io/

	Custom JS
	
	1. FIXED MENU
	2. MENU SMOOTH SCROLLING
	3. GOOGLE MAP
	4. READER TESTIMONIALS ( SLICK SLIDER )
	5. MOBILE MENU CLOSE 
	
**/

(function ($) {
  /* ----------------------------------------------------------- */
  /*  1. FIXED MENU
	/* ----------------------------------------------------------- */

  jQuery(window).bind("scroll", function () {
    if ($(window).scrollTop() > 150) {
      $("#mu-header").addClass("mu-fixed-nav");
    } else {
      $("#mu-header").removeClass("mu-fixed-nav");
    }
  });

  /* ----------------------------------------------------------- */
  /*  2. MENU SMOOTH SCROLLING
	/* ----------------------------------------------------------- */

  //MENU SCROLLING WITH ACTIVE ITEM SELECTED

  // Cache selectors
  var lastId,
    topMenu = $(".mu-menu"),
    topMenuHeight = topMenu.outerHeight() + 13,
    // All list items
    menuItems = topMenu.find("a[href^=\\#]"),
    // Anchors corresponding to menu items
    scrollItems = menuItems.map(function () {
      var item = $($(this).attr("href"));
      if (item.length) {
        return item;
      }
    });

  // Bind click handler to menu items
  // so we can get a fancy scroll animation
  menuItems.click(function (e) {
    var href = $(this).attr("href"),
      offsetTop = href === "#" ? 0 : $(href).offset().top - topMenuHeight + 22;
    jQuery("html, body").stop().animate(
      {
        scrollTop: offsetTop,
      },
      1500
    );
    e.preventDefault();
  });

  // Bind to scroll
  jQuery(window).scroll(function () {
    // Get container scroll position
    var fromTop = $(this).scrollTop() + topMenuHeight;

    // Get id of current scroll item
    var cur = scrollItems.map(function () {
      if ($(this).offset().top < fromTop) return this;
    });
    // Get the id of the current element
    cur = cur[cur.length - 1];
    var id = cur && cur.length ? cur[0].id : "";

    if (lastId !== id) {
      lastId = id;
      // Set/remove active class
      menuItems
        .parent()
        .removeClass("active")
        .end()
        .filter("[href=\\#" + id + "]")
        .parent()
        .addClass("active");
    }
  });

  /* ----------------------------------------------------------- */
  /*  3. GOOGLE MAP
	/* ----------------------------------------------------------- */

  $("#mu-google-map").click(function () {
    $("#mu-google-map iframe").css("pointer-events", "auto");
  });

  $("#mu-google-map").mouseleave(function () {
    $("#mu-google-map iframe").css("pointer-events", "none");
  });

  /* ----------------------------------------------------------- */
  /*  4. READER TESTIMONIALS (SLICK SLIDER)
	/* ----------------------------------------------------------- */

  $(".mu-testimonial-slide").slick({
    arrows: false,
    dots: true,
    infinite: true,
    speed: 500,
    autoplay: true,
    cssEase: "linear",
  });

  /* ----------------------------------------------------------- */
  /*  5. MOBILE MENU CLOSE 
	/* ----------------------------------------------------------- */

  jQuery(".mu-menu").on("click", "li a", function () {
    $(".mu-navbar .in").collapse("hide");
  });

  /**
   * 6. CURRENT TIME
   */
  const url = "http://158.108.182.2:50006/";
  setInterval(() => {
    $.get(url + "infor", function (data, status) {
      $("#last-enter").html(
        dayjs(data.S_lastest_time_enter * 1000).format("DD/MM/YYYY HH:mm:ss")
      );
      $("#last-exit").html(
        dayjs(data.S_lastest_time_left * 1000).format("DD/MM/YYYY HH:mm:ss")
      );
      $("#total").html(data.Total);
    });

    $.get(url + "queue", function (data, status) {
      const queues = data.Result;
      const waitList = queues.filter((queue) => queue.Q_status === 0).length;
      $("#pending-queue").html("People In Queue: " + waitList);
      $("#time-estimated").html(
        "Estimated Time: " + waitList * 30 + " minutes"
      );
    });
    $.ajax({
      type: "POST",
      url: url + "get_wristband",
      data: JSON.stringify({
        Wr_status: 0,
      }),
      success: (res0) => {
        $.ajax({
          type: "POST",
          url: url + "get_wristband",
          data: JSON.stringify({
            Wr_status: 1,
          }),
          success: (res1) => {
            console.log("resss", res1);
            $("#people-in-shop").html(
              res1.Result.length +
                " / " +
                (res1.Result.length + res0.Result.length)
            );
          },
          contentType: "application/json",
          dataType: "json",
        });
      },
      contentType: "application/json",
      dataType: "json",
    });
  }, 1000);
})(jQuery);
