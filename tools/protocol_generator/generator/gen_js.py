#!/bin/env python
# coding: utf-8

"""
Dakara Online protocol generator, by Alejandro Santos
"""

from genpackets import *
from gendefs_js import *

BUILDERS = []
HANDLERS = []
DECODE_DISPATCH = []
ARGS_HANDLER = []
def write_packets_from(f, fph, base_name, namespace, P):


    # Enum with IDs
    if base_name != "ServerPacket" :
    	f.write("""var {base_name}ID = {{ \n""".format(base_name=base_name))
    	for i, x in enumerate(P):
    		if x:
    			f.write("    {name} : {packet_id}".format(base_name=base_name, name=x.name, packet_id=i))
    			f.write(",\n")
    	f.write("""    {base_name}ID_PACKET_COUNT : {packet_id}\n}};\n""".format(base_name=base_name, packet_id=len(P)))

# Factory
    '''
    f.write("""
function {base_name}Factory(buffer) {{
    if (buffer.length() < 1) return 0;
    var p;
    PacketID = buffer.PeekByte();

    switch (PacketID) {{
""".format(base_name=base_name))

    for i, x in enumerate(P):
        if not x: continue
        f.write("""
        case {i}:
            p = new {name}(buffer);
            break;
""".format(i=i, name=x.name))

    f.write("""
    }}
    return p;
}}
""".format())
    '''
    
    for i, x in enumerate(P):
        if not x: continue

        header_fields = []
        header_fields_signature = []
        items_assign_e = []
        items_assign_build = []
        ctor_fields = ""
        min_byte_count = 0
        ctor_fields_bytequeue = ""
        parametros_fields = ""
        parametros_args = ""
        serialize_fields = ""

        if x.name == "MultiMessage":
            escribir_multimessage(f)
            continue

        for y in x.args:
            arg_name = y[0]
            arg_type = y[1] & 0xff
            arg_type_str = TYPE_TO_STR[arg_type]
            arg_type_sig_str = TYPE_TO_SIGNATURE_STR[arg_type]
            arg_is_array = ((y[1] & TYPE_ARRAY) == TYPE_ARRAY)
            type_reader_name = TYPE_TO_READER_NAME[arg_type]
            type_writer_name = TYPE_TO_WRITER_NAME[arg_type]

            ctor_fields += ", " + arg_name + "()"

            items_assign_e.append("            {arg_name}: {arg_name},".format(arg_name=arg_name))
            items_assign_build.append("    e.{arg_name}= {arg_name};".format(arg_name=arg_name))

            if arg_is_array:
                array_size=y[2]
                min_byte_count += TYPE_SIZE[arg_type] * array_size
                header_fields.append("    {arg_name}; ".format(arg_type_str=arg_type_str, arg_name=arg_name, array_size=array_size))
                header_fields_signature.append("{arg_name} ".format(arg_type_str=arg_type_sig_str, arg_name=arg_name, array_size=array_size))
                ctor_fields_bytequeue += x.get_ctor_fields_bytequeue_fmt(arg_is_array).format(arg_name=arg_name, type_reader_name=type_reader_name, array_size=array_size)
               	parametros_fields += x.get_parametros_fields_fmt(arg_is_array).format(arg_name=arg_name, type_reader_name=type_reader_name, array_size=array_size)
               	parametros_args += x.get_parametros_args_fmt(arg_is_array).format(arg_name=arg_name, type_reader_name=type_reader_name, array_size=array_size)
                serialize_fields += x.get_serialize_fields_fmt(arg_is_array).format(arg_name=arg_name, type_writer_name=type_writer_name, array_size=array_size)
            else:
                min_byte_count += TYPE_SIZE[arg_type]
                header_fields.append("    {arg_type_str} {arg_name}; ".format(arg_type_str=arg_type_str, arg_name=arg_name))
                header_fields_signature.append("{arg_type_str} {arg_name}".format(arg_type_str=arg_type_sig_str, arg_name=arg_name))
                ctor_fields_bytequeue += x.get_ctor_fields_bytequeue_fmt(arg_is_array).format(arg_name=arg_name, type_reader_name=type_reader_name)
                parametros_fields += x.get_parametros_fields_fmt(arg_is_array).format(arg_name=arg_name, type_reader_name=type_reader_name)
                parametros_args += x.get_parametros_args_fmt(arg_is_array).format(arg_name=arg_name, type_reader_name=type_reader_name)
                serialize_fields += x.get_serialize_fields_fmt(arg_is_array).format(arg_name=arg_name, type_writer_name=type_writer_name)

        format_args = {
            'base_name': base_name,
            'name': x.name,
            'header_fields': '\n'.join(header_fields),
            'header_fields_signature': ', '.join(header_fields_signature),
            'items_assign_e': '\n'.join(items_assign_e),
            'items_assign_build': '\n'.join(items_assign_build),
            'ctor_fields': ctor_fields,
            'packet_id': i,
            'min_byte_count': min_byte_count,
            'ctor_fields_bytequeue': ctor_fields_bytequeue,
            'serialize_fields': serialize_fields,
            'parametros_fields' : parametros_fields,
            'parametros_args' : parametros_args
        }

        # Individual packet header
        if base_name != "ServerPacket" :
        	f.write(x.get_header_fmt().format(**format_args))
        	BUILDERS.append(x.get_builder_fmt().format(**format_args))

        if base_name == "ServerPacket" :
            HANDLERS.append(x.get_handler_fmt().format(**format_args))

        #para el serverpacketdecodeanddispatch (sin tener que crear packetes)
        if base_name == "ServerPacket" :
        	dec_dispatch = x.get_parametros_fmt().format(**format_args);
        	#le saco la ultima coma si es que tiene:
        	pos = dec_dispatch.rfind(",")
        	if pos > 0:
        		dec_dispatch = dec_dispatch[:pos] + dec_dispatch[pos+1:]
        	DECODE_DISPATCH.append(dec_dispatch)

        if base_name == "ServerPacket" :
            args_handler = x.get_argumentosHandler_fmt().format(**format_args);
            #le saco la ultima coma si es que tiene:
            pos = args_handler.rfind(",")
            if pos > 0:
            	args_handler = args_handler[:pos] + args_handler[pos+1:]
            #le saco fin de linea
            pos = args_handler.rfind("\n")
            args_handler = args_handler[:pos] + args_handler[pos+1:]
            ARGS_HANDLER.append(args_handler)





    
    # Decode and Dispatch, keeping the Packet in the stack
    # Suggested by hmk
    if base_name == "ServerPacket" :
        f.write("""
function {base_name}DecodeAndDispatch(buffer, handler) {{
    if (buffer.length() < 1) return;
    var PacketID = buffer.ReadByte();

    switch (PacketID) {{
""".format(base_name=base_name))

        for i, x in enumerate(P):
            if not x: continue
            f.write("""
        case {i}:
        {{
            {decode_dispatch}
            break;
        }}
""".format(i=i, decode_dispatch=DECODE_DISPATCH.pop(0)))

        f.write("""
        default:
        {{
            msg = "error decoding packet id: " + PacketID;
            throw new Error(msg);
        }}
    }}
}}
""".format())

        fph.write("""
/** ESTE ARCHIVO SOLO ESTA PARA FACILITAR ESCRIBIR LOS HANLDLES POR PRIMERA VEZ, NO TINENE NINGUN USO ***************************************************************************************************************************************************/
""".format(base_name=base_name))
        for i, x in enumerate(P):
            if not x: continue
            fph.write("""\n\thandle{name}: function ({arg_handler}){{ \n""".format(base_name=base_name, name=x.name, arg_handler = ARGS_HANDLER.pop(0)))
             #fph.write(HANDLERS.pop(0))
            fph.write("""\t\tlog.network("TODO: handle{name} ");\n\t}},\n""".format(base_name=base_name, name=x.name))

        for i, x in enumerate(P):
            if not x: continue
              #fph.write("""\n\thandle{name}: function (p){{ \n""".format(base_name=base_name, name=x.name))
            #fph.write(HANDLERS.pop(0))
              #fph.write("""\t\talert("TODO: handle{name} ");\n\t}},\n""".format(base_name=base_name, name=x.name))

        fph.write("""
/** ESTE ARCHIVO SOLO ESTA PARA FACILITAR ESCRIBIR LOS HANLDLES POR PRIMERA VEZ, NO TINENE NINGUN USO ***************************************************************************************************************************************************/
""")


def write_packets():
    f = open("protocol.js", "w")
    fph = open("protocolhandlerAux.js", "w")

    f.write("""
/* Automatically generated file */

define(['enums'], function (Enums) {
""")

    write_packets_from(f,fph, "ClientPacket", "client", CLIENT_PACKETS)
    write_packets_from(f,fph, "ClientGMPacket", "clientgm", CLIENT_GM_PACKETS)
    write_packets_from(f,fph, "ServerPacket", "server", SERVER_PACKETS)

    #Multimessages hardcodeado: // TODO ; hacerlo bien
    f.write("""
    class Protocolo{
""")
    for builder in BUILDERS:
        f.write(builder)

    f.write("""
    ServerPacketDecodeAndDispatch(buffer, handler){
        ServerPacketDecodeAndDispatch(buffer, handler);
    }
    """)
    f.write("""
    }

    return Protocolo;
}); """)





    f.close()
    fph.close()



def escribir_multimessage(f):
    DECODE_DISPATCH.append('''

                var msgIdx = buffer.ReadByte();
                switch (msgIdx) {

                    case Enums.eMessage.NPCHitUser:
                        handler.handleNPCHitUser(buffer.ReadByte(), buffer.ReadInteger());
                        break;

                    case Enums.eMessage.UserHitNPC:
                        handler.handleUserHitNPC(buffer.ReadLong());
                        break;

                    case Enums.eMessage.UserAttackedSwing:
                        handler.handleUserAttackedSwing(buffer.ReadInteger());
                        break;

                    case Enums.eMessage.UserHittedByUser:
                        handler.handleUserHittedByUser(buffer.ReadInteger(), buffer.ReadByte(), buffer.ReadInteger());
                        break;

                    case Enums.eMessage.UserHittedUser:
                        handler.handleUserHittedUser(buffer.ReadInteger(), buffer.ReadByte(), buffer.ReadInteger());
                        break;

                    case Enums.eMessage.WorkRequestTarget:
                        handler.handleWorkRequestTarget(buffer.ReadByte());
                        break;

                    case Enums.eMessage.HaveKilledUser:
                        handler.handleHaveKilledUser(buffer.ReadInteger(),buffer.ReadLong());
                        break;

                    case Enums.eMessage.UserKill:
                        handler.handleUserKill(buffer.ReadInteger());
                        break;

                    case Enums.eMessage.Home:
                        handler.handleHome(buffer.ReadByte(),buffer.ReadInteger(),buffer.ReadUnicodeString());
                        break;

                    case Enums.eMessage.DontSeeAnything:
                        handler.handleDontSeeAnything();
                        break;

                    case Enums.eMessage.NPCSwing:

                        handler.handleNPCSwing();
                        break;

                    case Enums.eMessage.NPCKillUser:

                        handler.handleNPCKillUser();
                        break;

                    case Enums.eMessage.BlockedWithShieldUser:

                        handler.handleBlockedWithShieldUser();
                        break;

                    case Enums.eMessage.BlockedWithShieldOther:

                        handler.handleBlockedWithShieldOther();
                        break;

                    case Enums.eMessage.UserSwing:

                        handler.handleUserSwing();
                        break;

                    case Enums.eMessage.SafeModeOn:

                        handler.handleSafeModeOn();
                        break;

                    case Enums.eMessage.SafeModeOff:

                        handler.handleSafeModeOff();
                        break;

                    case Enums.eMessage.ResuscitationSafeOff:

                        handler.handleResuscitationSafeOff();
                        break;

                    case Enums.eMessage.ResuscitationSafeOn:

                        handler.handleResuscitationSafeOn();
                        break;

                    case Enums.eMessage.NobilityLost:

                        handler.handleNobilityLost();
                        break;

                    case Enums.eMessage.CantUseWhileMeditating:

                        handler.handleCantUseWhileMeditating();
                        break;

                    case Enums.eMessage.EarnExp:

                        handler.handleEarnExp();
                        break;

                    case Enums.eMessage.FinishHome:

                        handler.handleFinishHome();
                        break;

                    case Enums.eMessage.CancelHome:

                        handler.handleCancelHome();
                        break;

                    default:
                        throw new Error("Multimessage: " + msgIdx + " no reconocido por el protocolo");
                }
''')
    ARGS_HANDLER.append("msgIdx,args")


def main():
    write_packets()

if __name__ == '__main__':
    main()