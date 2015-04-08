function updatescore(){
  $.ajax({
    type: 'POST',
    url: '/game/highscore/',
    dataType: 'json',
    data: JSON.stringify (
      { platformer : localStorage.getItem('platformer_highscore'), 
        spaceinvader : localStorage.getItem('spaceinvader_highscore') 
      }),
    success : function(result) {
      localStorage.platformer_highscore = result.platformer;
      localStorage.spaceinvader_highscore = result.spaceinvader;      
    },           
  });
}

