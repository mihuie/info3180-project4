game.resources = [
	/**
	 * Graphics.
	 */
  // the main player spritesheet
	{name: "gripe_run_right",     type:"image",	src: "/static/img/platformer/sprite/gripe_run_right.png"},
	// our level tileset
	{name: "area01_level_tiles",  type:"image",	src: "/static/img/platformer/map/area01_level_tiles.png"},
  // the spinning coin spritesheet
	{name: "spinning_coin_gold",  type:"image",	src: "/static/img/platformer/sprite/spinning_coin_gold.png"},
  // our enemty entity
	{name: "wheelie_right",       type:"image",	src: "/static/img/platformer/sprite/wheelie_right.png"},
	// the parallax background
	{name: "area01_bkg0",         type:"image",	src: "/static/img/platformer/background/area01_bkg0.png"},
	{name: "area01_bkg1",         type:"image",	src: "/static/img/platformer/background/area01_bkg1.png"},
  // game font
	{name: "32x32_font",          type:"image",	src: "/static/img/platformer/font/32x32_font.png"},
  // game font
	{name: "title_screen",          type:"image",	src: "/static/img/platformer/gui/title_screen.png"},
	/* 
	 * Maps. 
 	 */
	{name: "area01",              type: "tmx",	src: "/static/map/area01.tmx"},

	/* 
	 * Background music. 
	 */	
	{name: "dst-inertexponent", type: "audio", src: "/static/bgm/"},
	
	/* 
	 * Sound effects. 
	 */
	{name: "cling", type: "audio", src: "/static/sfx/"},
	{name: "stomp", type: "audio", src: "/static/sfx/"},
	{name: "jump",  type: "audio", src: "/static/sfx/"}
];