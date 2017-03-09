$(function() {

  // Set Height of Timeline
  function setTimelineHeight() {
    timelineHeight = $('.timeline.swap').height();
    $('.timeline-wrap').height(timelineHeight + 52);
  }

  // Smooth Scroll
  $.scrollIt({
    topOffset: -50
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
    url: '/get-tweets',
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

  $('.contact-form').submit(function(e) {
    var data = {}
    var ch = true;
    var rules = {
      email: (/^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i),
      name: (/(.+)/),
      message: (/(.+)/)
    }
    $(this).find('input,textarea').each(function(){
      var name = $(this).attr('name');
      var value = $(this).val();
      data[name] = value;
      if(rules[name] && !rules[name].test(value) ) {
        ch = false;
        $('#'+name).parent().addClass('error');
      } else {
        $('#'+name).parent().removeClass('error');
      }
    });
    if(ch) {
      $.ajax({
        url: $(this).attr('action'),
        method: 'POST',
        data: data,
        success: function(data) {
          if(data == 1) {
            alert('Mesajınız gönderildi teşekkürler.');
            $('.contact-form input,.contact-form textarea').val('');
          } else if(data == 0) {
            alert('Mesajınız gönderilemedi. Tekrar deneyin.');
          }
        }
      })
    }
    e.preventDefault();
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
