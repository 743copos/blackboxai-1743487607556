bl_info = {
    "name": "Custom Blender Addon",
    "author": "Your Name",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Custom Tab",
    "description": "A custom Blender addon that demonstrates core functionality",
    "warning": "",
    "doc_url": "",
    "category": "3D View"
}

import bpy
from . import operators
from . import panels
from . import logger

# List of all classes to register
classes = (
    operators.CustomOperator,
    panels.CustomPanel,
)

def register():
    """Register all addon classes"""
    logger.setup_logger()
    
    for cls in classes:
        try:
            bpy.utils.register_class(cls)
        except Exception as e:
            print(f"Error registering {cls.__name__}: {str(e)}")
            return

    print("Successfully registered Custom Blender Addon")

def unregister():
    """Unregister all addon classes"""
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except Exception as e:
            print(f"Error unregistering {cls.__name__}: {str(e)}")
            return

    print("Successfully unregistered Custom Blender Addon")

# This allows running the script directly from Blender's text editor
if __name__ == "__main__":
    register()