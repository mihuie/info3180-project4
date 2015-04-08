game.ENDScreen = me.ScreenObject.extend({
    /**
     *  action to perform on state change
     */
  onResetEvent : function() {
    
    me.game.world.addChild(new (me.Renderable.extend ({
      // constructor
      init : function() {
        this._super(me.Renderable, 'init', [0, 0, me.game.viewport.width, me.game.viewport.height]);
        // font for the scrolling text
        this.font = new me.BitmapFont("32x32_font", 32);
      },
 
      update : function (dt) {
        return true;
      },
 
      draw : function (renderer) {
        this.font.draw(renderer, "GAME OVER", 180, 240);
        this.font.draw(renderer, "HIGHSCORE: ", 100, 300);
        this.font.draw(renderer, ~~game.data.score, 480, 300);
      },

    })), 2);
 
    // change to play state on press Enter or click/tap
    me.input.bindKey(me.input.KEY.ENTER, "enter", true);
    me.input.bindPointer(me.input.mouse.LEFT, me.input.KEY.ENTER);
    this.handler = me.event.subscribe(me.event.KEYDOWN, function (action, keyCode, edge) {        
      if (action === "enter") {
        // play something on tap / enter
        // this will unlock audio on mobile devices
        me.state.change(me.state.MENU);
      }
      updatescore();
    });
  },
 
  /**
   *  action to perform when leaving this screen (state change)
   */
  onDestroyEvent : function() {
    me.input.unbindKey(me.input.KEY.ENTER);
    me.input.unbindPointer(me.input.mouse.LEFT);
    me.event.unsubscribe(this.handler);
   }
});

    