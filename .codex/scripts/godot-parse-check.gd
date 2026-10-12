extends SceneTree
## Explicit Godot GDScript load/reload observer, adapted from Claude Code Game Studios.
## Read .codex/docs/run-and-observe.md for selected-project invocation and limits.
## Loading/reloading is engine execution and can have project/plugin/cache effects.
## Exit 0: supplied GDScripts loaded/reloaded; 1: failed load/reload; 2: invalid input.

func _initialize() -> void:
	var paths := OS.get_cmdline_user_args()
	if paths.is_empty():
		printerr("NOT ASSESSED: pass selected-project res:// GDScript paths after --.")
		quit(2)
		return
	for path in paths:
		if not path.begins_with("res://") or not path.ends_with(".gd") or ".." in path.split("/"):
			printerr("NOT ASSESSED: expected a project-local res://...gd path: ", path)
			quit(2)
			return
	var failed := false
	for path in paths:
		var script := ResourceLoader.load(path, "Script", ResourceLoader.CACHE_MODE_IGNORE) as Script
		if script == null:
			printerr("LOAD FAILED: ", path)
			failed = true
			continue
		var result := script.reload()
		if result != OK:
			printerr("RELOAD FAILED: ", path, " error=", result)
			failed = true
		else:
			print("LOADED/RELOADED: ", path, " can_instantiate=", script.can_instantiate(), " (observation only)")
	quit(1 if failed else 0)
