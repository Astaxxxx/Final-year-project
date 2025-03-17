extends Node

var socket = PacketPeerUDP.new()

func _ready():
    socket.connect_to_host("127.0.0.1", 5555)

func _process(delta):
    if socket.get_available_packet_count() > 0:
        var message = socket.get_packet().get_string_from_utf8()
        get_node("ai_assistant").update_status(message)
