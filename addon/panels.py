import bpy
from . import logger

class CustomPanel(bpy.types.Panel):
    """Creates a custom panel in the 3D Viewport's sidebar"""
    bl_label = "Custom Addon Panel"
    bl_idname = "VIEW3D_PT_custom_addon"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Custom Tab'
    
    def draw_header(self, context):
        """Draws the panel header"""
        layout = self.layout
        layout.label(text="", icon='PLUGIN')

    def draw(self, context):
        """Draw the panel layout"""
        layout = self.layout
        
        # Add a label
        row = layout.row()
        row.label(text="Object Scaling Tools")
        
        # Add some spacing
        layout.separator()
        
        # Add operator button with properties
        box = layout.box()
        col = box.column(align=True)
        
        # Show number of selected objects
        selected_count = len(context.selected_objects)
        col.label(text=f"Selected Objects: {selected_count}")
        
        # Add the operator button
        op_row = col.row(align=True)
        op_row.operator("custom.operator", text="Scale Objects")
        
        # Add some information about usage
        if selected_count == 0:
            info_box = layout.box()
            info_box.label(text="Select objects to enable scaling", icon='INFO')
        
        # Add version information at the bottom
        layout.separator()
        layout.label(text="Addon Version: 1.0.0")

    @classmethod
    def poll(cls, context):
        """Determine if the panel should be drawn"""
        return context.mode in {'OBJECT', 'EDIT_MESH'}