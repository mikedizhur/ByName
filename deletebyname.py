bl_info = {
    "name": "Delete by name",
    "author": "RamenSlayer",
    "version": (0, 0, 1),
    "blender": (2, 91, 2),
    "location": "View3D > Object",
    "description": "Delete any object(s) if they include the typed name.",
    "category": "Object",
}

import bpy
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    PropertyGroup,
)

from bpy.props import (StringProperty)

class OBJECT_OT_nameddelete(Operator):
    bl_label = "Delete by name"
    bl_idname = "object.named_delete"
    bl_description = "Deletes all object with a certain name"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'REGISTER', 'UNDO'}
    
    deletename: bpy.props.StringProperty(
        name = "Name",
        default = "Cube",
        description = "String used for identifying what objects should be deleted"
        )    

    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        for object in bpy.data.objects:
            if self.deletename.lower() in object.name.lower():
                object.hide_set(False)
                object.select_set(True)
        bpy.ops.object.delete(use_global=False)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(OBJECT_OT_nameddelete.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_nameddelete)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_nameddelete)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()