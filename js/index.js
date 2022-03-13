var etx = {
    init: function() {
      etx.callFontFlakes();
    },
    callFontFlakes: function() {
      window.setInterval(function() {
        etx.fontFlake();
      }, 100);
    },
    fontFlake: function() {
      // let set some bloody vars
      var stageWidth = $(window).width();
      var stageHeight = $(window).height();
      var items = Array("Anxiety", "Pain", "Hostile", "Cheating", "Conflict", "Conflict", "Fighting", "Fear", "Angry", "Angry", "Angry", "Affair", "Shut down", "Disconnected", "Angry", "Depression", "Depression", "Sadness", "Crisis");
      var text = items[Math.floor(Math.random() * items.length)];
      var randomEntry = Math.ceil(Math.random() * stageWidth);
      var preRandomFontSize = Math.ceil(Math.random() * 20);
      var randomFontSize = preRandomFontSize + 10;
      var flakeName = 'flake-' + randomEntry;
      var grayScale = Math.ceil(Math.random() * 256);
      var hue = 'rgb(0,0,0)';
  
      // ok time to create and animate this stupid thing.
      $('<div />', {
        text: text,
        id: flakeName,
      }).appendTo('#fallingtext').addClass('fontFlake').css('left', randomEntry).css('font-size', randomFontSize).css('color', hue).animate({
        "top": "+=" + stageHeight,
        opacity: 0
      }, 5000, function() {
        $('#' + flakeName).remove();
      });
    }
  };
  $(document).ready(function() {
    etx.init();
  });