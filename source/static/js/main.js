$(function() {

  // Set Height of Timeline
  function setTimelineHeight() {
    timelineHeight = $('.timeline.swap').height();
    $('.timeline-wrap').height(timelineHeight + 52);
  }

  //setTimelineHeight(); // Run It Once...

// Smooth Scroll
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top-$('.main-nav').height()
        }, 500);
        return false;
      }
    }
  });

// Select Day
  $('.day-select a').each(function(i) {
    $(this).click(function(e) {
      e.preventDefault();
      $(this).addClass('active').siblings().removeClass('active');
      $('.timeline').eq(i).show().siblings().hide();
      //setTimelineHeight();
    })
  });

  // Toggle Mobile Navigation
  function toggleNav() {
    window.w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0) // Get Viewport Width

    if ( w < 769) {
      $('body').addClass('no-scroll');
      $('.main-nav').toggle();
    }
  }
  $('.toggle-mobile-nav, .main-nav a').click(function(e) {
    toggleNav();
    e.preventDefault();
  });

  $.ajax({
    url: '/get-tweets/',
    success: function(datas) {
      var tweets = datas;
      var tweetTimer;
      var i = 0;
      (tweetTimer = function() {
        $('.latest-tweet p').html(tweets[i].text);
        $('.latest-tweet a').attr('href', 'https://twitter.com/kodlaco/status/'+tweets[i].id_str);
        if(i == tweets.length-1)
          i=0;
        else
          i++;
      })()
      setInterval(tweetTimer, 5000)
    }
  });

});

// If Browser Window Width Has Changed Then Bring Navigation Bar Back
window.onresize = function(event) {
  if ( window.w > 768) {
    $('body').removeClass('no-scroll');
    $('.main-nav').toggle();
  }
  setTimelineHeight();
};
