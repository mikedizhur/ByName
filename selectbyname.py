bl_info = {
    "name": "Select by name",
    "author": "Mike Dizhur",
    "version": (1, 1),
    "blender": (5, 1, 1),
    "location": "View3D > Select",
    "description": "Select multiple objects with similar name with one button.",
    "category": "Object",
}

import bpy
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    PropertyGroup,
)
from bpy.props import (StringProperty, BoolProperty)


def strsinstr(keywords, searched):
    """function for checking if all words in a list are in a string"""
    for word in keywords:
        if not (word.lower() in searched.lower()):
            return False
    return True


class OBJECT_OT_namedselect(Operator):
    bl_label = "Select by Name"
    bl_idname = "object.named_select"
    bl_description = "Selects all object with a certain name (also unhides them)"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'REGISTER', 'UNDO'}

    selectnames: bpy.props.StringProperty(
        name='Names',
        default='Cube',
        description="Strings separated by spaces that objects names are matched against",
        )

    unhide: bpy.props.BoolProperty(
        name="Unhide Selection",
        default=False,
        description="Unhide objects if the name matches",
        )

    def execute(self, context):
        select_keywords = self.selectnames.split()
        bpy.ops.object.select_all(action='DESELECT')
        for object in bpy.data.objects:
            if strsinstr(select_keywords, object.name.lower()):
                if object.hide_get() and not self.unhide:
                    continue
                object.hide_set(False)
                object.select_set(True)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(OBJECT_OT_namedselect.bl_idname)


def register():
    bpy.utils.register_class(OBJECT_OT_namedselect)
    bpy.types.VIEW3D_MT_select_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_namedselect)
    bpy.types.VIEW3D_MT_select_object.remove(menu_func)


if __name__ == "__main__":
    register()
