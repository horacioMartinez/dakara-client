define(['character', 'player', 'timer', 'enums'], function (Character, Player, Timer) {

    var Updater = Class.extend({
        init: function (game) {
            this.game = game;
        },

        update: function () {
            if (this.game.logeado) {
                if (this.game.player)
                    this.updateComenzarMovimientoPlayer();
            }
        },

        updateComenzarMovimientoPlayer: function () { // todo: hacerlo dentro de player y sacar por completo esta clase
            if (this.game.player.tratarDeMover()){
                this.game.renderer.updateTilesMov(this.game.player.getDirMov());
            }
        },

    });

    return Updater;
});
