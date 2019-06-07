function getStylesheet() {
      var currentTime = new Date().getHours();
      if (0 <= currentTime&&currentTime < 5) {
          $('#nightmode').html("<link rel='stylesheet' href='/css/night.css' type='text/css'>");
      }
      if (5 <= currentTime&&currentTime < 11) {
          $('#nightmode').html("<link rel='stylesheet' href='/css/day.css' type='text/css'>");
      }
      if (11 <= currentTime&&currentTime < 16) {
          $('#nightmode').html("<link rel='stylesheet' href='/css/day.css' type='text/css'>");
      }
      if (16 <= currentTime&&currentTime < 19) {
          $('#nightmode').html("<link rel='stylesheet' href='/css/day.css' type='text/css'>");
      }
      if (22 <= currentTime&&currentTime <= 24) {
          $('#nightmode').html("<link rel='stylesheet' href='/css/night.css' type='text/css'>");
      }
}

$(document).ready(function () {
    
    getStylesheet();

});