
var game = {
  
  // an object where to store game information
    data : {
        // score
        score : 0,
        bonus : 10,
        speed : 1000,
        level : 1
    },

    // Run on page load.
    "onload" : function () {
        // Initialize the video.
        if (!me.video.init(640, 480, {wrapper : "screen", scale : 'auto'})) {
            alert("Your browser does not support HTML5 canvas.");
            return;
        }

        // add "#debug" to the URL to enable the debug Panel
        if (document.location.hash === "#debug") {
            window.onReady(function () {
                me.plugin.register.defer(this, me.debug.Panel, "debug", me.input.KEY.V);
            });
        }

        // Initialize the audio.
        me.audio.init("mp3,ogg");

        // Set a callback to run when loading is complete.
        me.loader.onload = this.loaded.bind(this);

        // Load the resources.
        me.loader.preload(game.resources);

        // Initialize melonJS and display a loading screen.
        me.state.change(me.state.LOADING);
    },



    // Run on game resources loaded.
    "loaded" : function () {
        // set the "Play/Ingame" Screen Object
        this.playScreen = new game.PlayScreen();
        this.endScreen = new game.ENDScreen();
        this.nextScreen = new game.NextScreen();
      
        me.state.set(me.state.MENU, new game.TitleScreen());
        me.state.set(me.state.PLAY, this.playScreen);
        me.state.set(me.state.READY, this.nextScreen)
        me.state.set(me.state.GAMEOVER, this.endScreen);
      
        me.state.transition("fade", "#000000", 250);

        // add our player entity in the entity pool
        me.pool.register("player", game.Player);
        me.pool.register("laser", game.Laser);
        me.pool.register("enemy", game.Enemy);

        // start the game
        me.state.change(me.state.MENU);
    }
};
