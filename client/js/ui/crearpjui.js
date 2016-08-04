/**
 * Created by horacio on 2/27/16.
 */

define(['enums', 'utils/util'], function (Enums, Utils) {
    class CrearPjUI {
        constructor(assetManager, mensaje) {
            this.assetManager = assetManager;
            this.mensaje = mensaje;
            this._inicializado = false;
            this.LARGO_MINIMO_PASSWORD = 5;
            this.offsetSelectedCabeza = 0;

            this.$imgCabezaIzq = $('#crearPjSeleccionCabezaImagenIzq');
            this.$imgCabezaCentro = $('#crearPjSeleccionCabezaImagenCenter');
            this.$imgCabezaDer = $('#crearPjSeleccionCabezaImagenDer');

            this.$imagenCuerpo = $('#crearPjImagenPersonaje');
            this.$imagenCabezaCuerpo = $('#crearPjImagenCabezaPersonaje');
        }

        inicializar() {
            if (this._inicializado) {
                return;
            } else {
                this._inicializado = true;
            }

            var self = this;

            var id = "crearSelectCiudad";
            var $sel = $('#' + id);
            this.modificarSlotInput($sel, id, Enums.Ciudad.Ullathorpe, "Ullathorpe");
            this.modificarSlotInput($sel, id, Enums.Ciudad.Nix, "Nix");
            this.modificarSlotInput($sel, id, Enums.Ciudad.Banderbill, "Banderbill");
            this.modificarSlotInput($sel, id, Enums.Ciudad.Lindos, "Lindos");
            this.modificarSlotInput($sel, id, Enums.Ciudad.Arghal, "Arghal");

            id = "crearSelectRaza";
            $sel = $('#' + id);
            this.modificarSlotInput($sel, id, Enums.Raza.humano, "Humano");
            this.modificarSlotInput($sel, id, Enums.Raza.elfo, "Elfo");
            this.modificarSlotInput($sel, id, Enums.Raza.elfoOscuro, "Elfo Oscuro");
            this.modificarSlotInput($sel, id, Enums.Raza.gnomo, "Gnomo");
            this.modificarSlotInput($sel, id, Enums.Raza.enano, "Enano");
            $sel.change(function () {
                self._updatePJ();
            });

            id = "crearSelectClase";
            $sel = $('#' + id);
            this.modificarSlotInput($sel, id, Enums.Clase.mago, "Mago");
            this.modificarSlotInput($sel, id, Enums.Clase.clerigo, "Clérigo");
            this.modificarSlotInput($sel, id, Enums.Clase.guerrero, "Guerrero");
            this.modificarSlotInput($sel, id, Enums.Clase.asesino, "Asesino");
            this.modificarSlotInput($sel, id, Enums.Clase.ladron, "Ladrón");
            this.modificarSlotInput($sel, id, Enums.Clase.bardo, "Bardo");
            this.modificarSlotInput($sel, id, Enums.Clase.druida, "Druida");
            this.modificarSlotInput($sel, id, Enums.Clase.bandido, "Bandido");
            this.modificarSlotInput($sel, id, Enums.Clase.paladin, "Paladín");
            this.modificarSlotInput($sel, id, Enums.Clase.cazador, "Cazador");
            this.modificarSlotInput($sel, id, Enums.Clase.trabajador, "Trabajador");
            this.modificarSlotInput($sel, id, Enums.Clase.pirata, "Pirata");

            id = "crearSelectGenero";
            $sel = $('#' + id);
            this.modificarSlotInput($sel, id, Enums.Genero.hombre, "Hombre");
            this.modificarSlotInput($sel, id, Enums.Genero.mujer, "Mujer");
            $sel.change(function () {
                self._updatePJ();
            });

            $('#crearPjSeleccionCabezaBotonIzq').click(() => {
                this.offsetSelectedCabeza--;
                this._updatePJ();
            });
            $('#crearPjSeleccionCabezaBotonDer').click(() => {
                this.offsetSelectedCabeza++;
                this._updatePJ();
            });
            this._updatePJ();
        }

        _getGenero() {
            return parseInt($("#crearSelectGenero").val());
        }

        _getRaza() {
            return parseInt($("#crearSelectRaza").val());
        }

        modificarSlotInput($sel, id, slot, texto) {
            var elemento = $('#' + id + ' option[value=' + slot + ']');
            if (!elemento.length) { // nuevo elemento
                $sel.append($("<option>").attr('value', slot).text(texto));
            }
            else {
                $(elemento).text(texto);
            }
        }

        setBotonTirarDadosCallback(cb) {

            $('#crearBotonTirarDados').click(function () {
                cb();
            });
        }

        setBotonVolverCallback(cb) {
            $('#crearBotonVolver').click(function () {
                cb();
            });
        }

        setBotonCrearCallback(cb) {
            var self = this;
            $('#crearBotonCrear').click(function () {
                var nombre = $("#crearNombreInput").val();
                var password = $("#crearPasswordInput").val();
                var password2 = $("#crearRepetirPasswordInput").val();
                var mail = $("#crearMailInput").val();
                var raza = $("#crearSelectRaza").val();
                var genero = $("#crearSelectGenero").val();
                var clase = $("#crearSelectClase").val();
                var ciudad = $("#crearSelectCiudad").val();
                var cabeza = self._getCabezaNum(self.offsetSelectedCabeza);

                if (!cabeza) {
                    self.mensaje.show("Debes elegir una cabeza");
                }

                if (!(nombre && password && password2 && raza && genero && clase && cabeza && mail && ciudad)) {
                    self.mensaje.show("Debes completar todos los campos");
                    return;
                }
                if (!self.emailValido(mail)) {
                    self.mensaje.show("Mail invalido");
                    return;
                }
                if (!self.passwordValido(password)) {
                    self.mensaje.show("El password debe contener " + self.LARGO_MINIMO_PASSWORD + " o mas caracteres");
                    return;
                }

                if (!( password === password2)) {
                    self.mensaje.show("Los passwords ingresados no coinciden");
                    return;
                }

                cb(nombre, password, raza, genero, clase, cabeza, mail, ciudad);
            });
        }

        _getCabezaNum(offset) {
            var cabezas = this.getPrimerYUltimaCabezaNum();
            var incremento = Utils.modulo(offset, (cabezas.ultima - cabezas.primera));

            return cabezas.primera + incremento;
        }

        _updatePJ() {
            this._actualizarAlturaPJ();
            this._updateCabezas();
            this._updateCuerpo();
        }

        _actualizarAlturaPJ() {
            let raza = this._getRaza();
            let petizo = (raza === Enums.Raza.gnomo || raza === Enums.Raza.enano);
            if (petizo) {
                this.$imagenCabezaCuerpo.addClass('petizo');
            } else {
                this.$imagenCabezaCuerpo.removeClass('petizo');
            }
        }

        _updateCabezas() {
            var cabezaIzq = this._getCabezaNum(this.offsetSelectedCabeza - 1);
            var cabezaCentro = this._getCabezaNum(this.offsetSelectedCabeza);
            var cabezaDer = this._getCabezaNum(this.offsetSelectedCabeza + 1);
            var numGrafIzq = this.assetManager.getFaceGrafFromNum(cabezaIzq);
            var numGrafCentro = this.assetManager.getFaceGrafFromNum(cabezaCentro);
            var numGrafDer = this.assetManager.getFaceGrafFromNum(cabezaDer);

            var url = "url(graficos/" + numGrafIzq + ".png)";
            this.$imgCabezaIzq.css('background-image', url);
            url = "url(graficos/" + numGrafDer + ".png)";
            this.$imgCabezaDer.css('background-image', url);
            url = "url(graficos/" + numGrafCentro + ".png)";
            this.$imgCabezaCentro.css('background-image', url);
            this.$imagenCabezaCuerpo.css('background-image', url);
        }

        _updateCuerpo() {
            var raza = $("#crearSelectRaza").val();
            var genero = $("#crearSelectGenero").val();

            var numCuerpo = this._getCuerpoNum(genero, raza);
            var numGraf = this.assetManager.getBodyGrafFromNum(numCuerpo);
            var url = "url(graficos/" + numGraf + ".png)";
            this.$imagenCuerpo.css('background-image', url);
        }

        updateDados(Fuerza, Agilidad, Inteligencia, Carisma, Constitucion) {
            $('#crearDadoFuerza').text("Fuerza: " + Fuerza);
            $('#crearDadoAgilidad').text("Agilidad: " + Agilidad);
            $('#crearDadoInteligencia').text("Inteligencia: " + Inteligencia);
            $('#crearDadoCarisma').text("Carisma: " + Carisma);
            $('#crearDadoConstitucion').text("Constitucion: " + Constitucion);
        }

        emailValido(email) {
            // Regex borrowed from http://stackoverflow.com/a/46181/393005
            var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(email);
        }

        passwordValido(pw) {
            return (!(pw.length < this.LARGO_MINIMO_PASSWORD))
        }

        getPrimerYUltimaCabezaNum() {
            let genero = this._getGenero();
            let raza = this._getRaza();

            var HUMANO_H_PRIMER_CABEZA = 1;
            var HUMANO_H_ULTIMA_CABEZA = 51;
            var ELFO_H_PRIMER_CABEZA = 101;
            var ELFO_H_ULTIMA_CABEZA = 122;
            var DROW_H_PRIMER_CABEZA = 201;
            var DROW_H_ULTIMA_CABEZA = 221;
            var ENANO_H_PRIMER_CABEZA = 301;
            var ENANO_H_ULTIMA_CABEZA = 319;
            var GNOMO_H_PRIMER_CABEZA = 401;
            var GNOMO_H_ULTIMA_CABEZA = 416;
            //**************************************************
            var HUMANO_M_PRIMER_CABEZA = 70;
            var HUMANO_M_ULTIMA_CABEZA = 89;
            var ELFO_M_PRIMER_CABEZA = 170;
            var ELFO_M_ULTIMA_CABEZA = 188;
            var DROW_M_PRIMER_CABEZA = 270;
            var DROW_M_ULTIMA_CABEZA = 288;
            var ENANO_M_PRIMER_CABEZA = 370;
            var ENANO_M_ULTIMA_CABEZA = 384;
            var GNOMO_M_PRIMER_CABEZA = 470;
            var GNOMO_M_ULTIMA_CABEZA = 484;

            if (genero === Enums.Genero.hombre) {
                switch (raza) {
                    case Enums.Raza.humano:
                        return {primera: HUMANO_H_PRIMER_CABEZA, ultima: HUMANO_H_ULTIMA_CABEZA};
                        break;
                    case Enums.Raza.elfo:
                        return {primera: ELFO_H_PRIMER_CABEZA, ultima: ELFO_H_ULTIMA_CABEZA};
                        break;
                    case Enums.Raza.elfoOscuro:
                        return {primera: DROW_H_PRIMER_CABEZA, ultima: DROW_H_ULTIMA_CABEZA};
                        break;
                    case Enums.Raza.enano:
                        return {primera: ENANO_H_PRIMER_CABEZA, ultima: ENANO_H_ULTIMA_CABEZA};
                        break;
                    case Enums.Raza.gnomo:
                        return {primera: GNOMO_H_PRIMER_CABEZA, ultima: GNOMO_H_ULTIMA_CABEZA};
                        break;
                    default:
                        log.error("raza invalida")
                }
            }
            if (genero === Enums.Genero.mujer) {
                switch (raza) {
                    case Enums.Raza.humano:
                        return {primera: HUMANO_M_PRIMER_CABEZA, ultima: HUMANO_M_ULTIMA_CABEZA};
                        break;
                    case Enums.Raza.elfo:
                        return {primera: ELFO_M_PRIMER_CABEZA, ultima: ELFO_M_ULTIMA_CABEZA};
                        break;
                    case Enums.Raza.elfoOscuro:
                        return {primera: DROW_M_PRIMER_CABEZA, ultima: DROW_M_ULTIMA_CABEZA};
                        break;
                    case Enums.Raza.enano:
                        return {primera: ENANO_M_PRIMER_CABEZA, ultima: ENANO_M_ULTIMA_CABEZA};
                        break;
                    case Enums.Raza.gnomo:
                        return {primera: GNOMO_M_PRIMER_CABEZA, ultima: GNOMO_M_ULTIMA_CABEZA};
                        break;
                    default:
                        log.error("raza invalida")
                }
            }
        }

        _getCuerpoNum() {
            let genero = this._getGenero();
            let raza = this._getRaza();

            var HUMANO_H_CUERPO_DESNUDO = 21;
            var ELFO_H_CUERPO_DESNUDO = 210;
            var DROW_H_CUERPO_DESNUDO = 32;
            var ENANO_H_CUERPO_DESNUDO = 53;
            var GNOMO_H_CUERPO_DESNUDO = 222;
            //**************************************************
            var HUMANO_M_CUERPO_DESNUDO = 39;
            var ELFO_M_CUERPO_DESNUDO = 259;
            var DROW_M_CUERPO_DESNUDO = 40;
            var ENANO_M_CUERPO_DESNUDO = 60;
            var GNOMO_M_CUERPO_DESNUDO = 260;
            if (genero === Enums.Genero.hombre) {
                switch (raza) {
                    case Enums.Raza.humano:
                        return HUMANO_H_CUERPO_DESNUDO;
                        break;
                    case Enums.Raza.elfo:
                        return ELFO_H_CUERPO_DESNUDO;
                        break;
                    case Enums.Raza.elfoOscuro:
                        return DROW_H_CUERPO_DESNUDO;
                        break;
                    case Enums.Raza.enano:
                        return ENANO_H_CUERPO_DESNUDO;
                        break;
                    case Enums.Raza.gnomo:
                        return GNOMO_H_CUERPO_DESNUDO;
                        break;
                    default:
                        log.error("raza invalida")
                }
            }
            if (genero === Enums.Genero.mujer) {
                switch (raza) {
                    case Enums.Raza.humano:
                        return HUMANO_M_CUERPO_DESNUDO;
                        break;
                    case Enums.Raza.elfo:
                        return ELFO_M_CUERPO_DESNUDO;
                        break;
                    case Enums.Raza.elfoOscuro:
                        return DROW_M_CUERPO_DESNUDO;
                        break;
                    case Enums.Raza.enano:
                        return ENANO_M_CUERPO_DESNUDO;
                        break;
                    case Enums.Raza.gnomo:
                        return GNOMO_M_CUERPO_DESNUDO;
                        break;
                    default:
                        log.error("raza invalida")
                }
            }

        }
    }

    return CrearPjUI;
});

