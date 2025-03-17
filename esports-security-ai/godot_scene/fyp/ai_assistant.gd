extends Node3D

var status = "idle"

func _process(delta):
	if status == "safe":
		$MeshInstance3D.material_override.albedo_color = Color(0,1,0) # Green
	elif status == "scanning":
		$MeshInstance3D.material_override.albedo_color = Color(1,1,0) # Yellow
	elif status == "threat_detected":
		$MeshInstance3D.material_override.albedo_color = Color(1,0,0) # Red

func update_status(new_status):
	status = new_status
