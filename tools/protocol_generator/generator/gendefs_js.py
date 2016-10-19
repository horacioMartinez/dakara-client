

class Packet:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def get_header_fmt(self):
        return """
function {name} (buffer) {{
    
        this.id = {base_name}ID.{name} /* {packet_id} */;
        if (buffer){{
        buffer.ReadByte(); /* PacketID */
{ctor_fields_bytequeue}
        }}
    this.serialize = function(buffer) {{
        buffer.WriteByte({base_name}ID.{name}); /* PacketID: {packet_id} */
{serialize_fields}
        buffer.flush();
    }};

    this.dispatch = function (d){{
        d.handle{name}(this);

    }};

}}
"""
    def get_builder_fmt(self):
        return """
    Build{name}({header_fields_signature}) {{
        var e = new {name}();
{items_assign_build}
        return e;
    }}

"""

    def get_parametros_fmt(self):
        return """    
{parametros_fields}
            handler.handle{name}( {parametros_args} );
"""

    def get_argumentosHandler_fmt(self):
        return """{parametros_args}
"""
#    def get_handler_fmt(self):
#        return """
#{items_assign_build}
#"""

    def get_handler_fmt(self):
        return """
    send{name}({header_fields_signature}) {{
        p = this.protocolo.Build{name}({header_fields_signature} );
        p.serialize(this.byteQueue);
    }}
"""

    def get_ctor_fields_bytequeue_fmt(self, is_array):
        if is_array:
            return "    var i; this.{arg_name}= []; for (i=0; i<{array_size}; ++i) this.{arg_name}[i] = buffer.{type_reader_name}();\n"
        else:
            return "        this.{arg_name} = buffer.{type_reader_name}();\n"

    def get_parametros_fields_fmt(self, is_array):
        if is_array:
            return "        var i; var {arg_name}= []; for (i=0; i<{array_size}; ++i) {arg_name}[i] = buffer.{type_reader_name}();\n"
        else:
            return "            var {arg_name} = buffer.{type_reader_name}();\n"

    def get_parametros_args_fmt(self, is_array):
        if is_array:
            return "{arg_name},"
        else:
            return "{arg_name},"

    def get_serialize_fields_fmt(self, is_array):
        if is_array:
            return "    var i; for (i=0; i<{array_size}; ++i) buffer.{type_writer_name}(this.{arg_name}[i]);\n"
        else:
            return "        buffer.{type_writer_name}(this.{arg_name});\n"

class PacketGMHeader(Packet):
    def __init__(self, name, args):
        Packet.__init__(self, name, args)

    def get_header_fmt(self):
        return """
function {name} (buffer) {{

        this.id = {base_name}ID.{name} /* {packet_id} */;
        if (buffer){{
        buffer.ReadByte(); /* PacketID */
    {ctor_fields_bytequeue}
        }}
    this.serialize = function(buffer) {{
    {serialize_fields}
    }};

    this.dispatch = function (d){{
        d.handle{name}(this);

    }};
}}
"""

class PacketGMCommand(Packet):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def get_header_fmt(self):
        return """
function {name} (buffer) {{
    
        this.id = {base_name}ID.{name} /* {packet_id} */;
        if (buffer){{
        buffer.ReadByte(); /* PacketID */
{ctor_fields_bytequeue}
        }}
    this.serialize = function(buffer) {{
        buffer.WriteByte(ClientPacketID_GMCommands);
        buffer.WriteByte({base_name}ID.{name}); /* PacketID: {packet_id} */
{serialize_fields}
        buffer.flush();
    }};

    this.dispatch = function (d){{
        d.handle{name}(this);
    }};
}}

"""

class PacketWithCount(Packet):
    def __init__(self, name, args, reader_type):
        Packet.__init__(self, name, args)
        self.reader_type = reader_type

    def get_header_fmt(self):
        return """
function {name} (buffer) {{

        this.id = {base_name}ID.{name} /* {packet_id} */;
        this.Items = [];
        if (buffer) {{
        buffer.ReadByte(); /* PacketID */
        var Count = buffer.__COUNTREADER__();
        var i; 
        for (i=0; i<Count; ++i) {{
            var e = {{
{ctor_fields_bytequeue}            
            }};
            this.Items.push(e);
        }}
    }}
    """.replace("__COUNTREADER__", TYPE_TO_READER_NAME[self.reader_type]) + """
    this.serialize = function(buffer) {{
        buffer.WriteByte({base_name}ID.{name}); /* PacketID: {packet_id} */
        var Count = Items.length;
        buffer.__COUNTWRITER__(Count);
        var i; 
        for (i=0; i<Count; ++i) {{
            e = Items[i];
{serialize_fields}
        buffer.flush();
        }}
    }};
    
    this.dispatch = function (d){{
        d.handle{name}(this);
    }};

    this.addItem = function({header_fields_signature}) {{
        var e = {{
{items_assign_e}
        }};
        this.Items.push(e);
    }}
}}""".replace("__COUNTWRITER__", TYPE_TO_WRITER_NAME[self.reader_type])
    
    def get_handler_fmt(self):
        return """ /*ACA*/
        var e = {{
{items_assign_e}
        }};
        this.Items.push(e);
    }}"""

    def get_parametros_fmt(self):
        return """    
        /* Packet con count! */
        var Items = [];
        var Count = buffer.__COUNTREADER__();
        var i; 
        for (i=0; i<Count; ++i) {{
            var e = {{
{ctor_fields_bytequeue}            
            }};
            Items.push(e);
        }}
        handler.handle{name}(Items);
""".replace("__COUNTREADER__", TYPE_TO_READER_NAME[self.reader_type])

    def get_argumentosHandler_fmt(self):
        return """Items
"""

#    def get_handler_fmt(self):
#        return """
#{items_assign_build}



#"""

    def get_ctor_fields_bytequeue_fmt(self, is_array):
        if is_array:            
            return "            {{ var i; e.{arg_name} = []; for (i=0; i<{array_size}; ++i) e.{arg_name}[i] = buffer.{type_reader_name}(); }}\n"
        else:
            return "                {arg_name} : buffer.{type_reader_name}(),\n"

    def get_serialize_fields_fmt(self, is_array):
        if is_array:
            return "            {{ var i; for (i=0; i<{array_size}; ++i) buffer.{type_writer_name}(e.{arg_name}[i]); }}\n"
        else:
            return "            buffer.{type_writer_name}(e.{arg_name});\n"

TYPE_UNICODE_STRING = 0
TYPE_UNICODE_STRING_FIXED = 1
TYPE_BINARY_STRING = 2
TYPE_BINARY_STRING_FIXED = 3
TYPE_I8 = 4
TYPE_I16 = 5
TYPE_I32 = 6
TYPE_SINGLE = 7 # Float
TYPE_DOUBLE = 8 # Double
TYPE_BOOL = 9
TYPE_ARRAY = (1 << 8)

TYPE_TO_STR = {
    TYPE_UNICODE_STRING: 'var',
    TYPE_UNICODE_STRING_FIXED: 'var',
    TYPE_BINARY_STRING: 'var',
    TYPE_BINARY_STRING_FIXED: 'var',
    TYPE_I8: 'var',
    TYPE_I16: 'var',
    TYPE_I32: 'var',
    TYPE_SINGLE: 'var',
    TYPE_DOUBLE: 'var',
    TYPE_BOOL: 'var',
}

TYPE_TO_SIGNATURE_STR = {
    TYPE_UNICODE_STRING: '',
    TYPE_UNICODE_STRING_FIXED: '',
    TYPE_BINARY_STRING: '',
    TYPE_BINARY_STRING_FIXED: '',
    TYPE_I8: '',
    TYPE_I16: '',
    TYPE_I32: '',
    TYPE_SINGLE: '',
    TYPE_DOUBLE: '',
    TYPE_BOOL: '',
}

TYPE_TO_READER_NAME = {
    TYPE_UNICODE_STRING: 'ReadUnicodeString',
    #TYPE_UNICODE_STRING_FIXED: '',
    #TYPE_BINARY_STRING: '',
    #TYPE_BINARY_STRING_FIXED: 'ReadBinaryFixed',
    TYPE_I8: 'ReadByte',
    TYPE_I16: 'ReadInteger',
    TYPE_I32: 'ReadLong',
    TYPE_SINGLE: 'ReadSingle',
    TYPE_DOUBLE: 'ReadDouble',
    TYPE_BOOL: 'ReadBoolean',
}

TYPE_TO_WRITER_NAME = {
    TYPE_UNICODE_STRING: 'WriteUnicodeString',
    #TYPE_UNICODE_STRING_FIXED: '',
    #TYPE_BINARY_STRING: '',
    #TYPE_BINARY_STRING_FIXED: 'ReadBinaryFixed',
    TYPE_I8: 'WriteByte',
    TYPE_I16: 'WriteInteger',
    TYPE_I32: 'WriteLong',
    TYPE_SINGLE: 'WriteSingle',
    TYPE_DOUBLE: 'WriteDouble',
    TYPE_BOOL: 'WriteBoolean',
}

TYPE_SIZE = {
    TYPE_UNICODE_STRING: 2,
    #TYPE_UNICODE_STRING_FIXED: 0,
    TYPE_BINARY_STRING: 2,
    #TYPE_BINARY_STRING_FIXED: 0,
    TYPE_I8: 1,
    TYPE_I16: 2,
    TYPE_I32: 4,
    TYPE_SINGLE: 4,
    TYPE_DOUBLE: 8,
    TYPE_BOOL: 1,
}
