import bpy
from . import logger

class CustomOperator(bpy.types.Operator):
    """Custom operator for demonstrating addon functionality"""
    bl_idname = "custom.operator"
    bl_label = "Custom Operator"
    bl_description = "Performs a custom operation on selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    # Example property
    scale_factor: bpy.props.FloatProperty(
        name="Scale Factor",
        description="Factor to scale the selected objects",
        default=1.0,
        min=0.1,
        max=10.0
    )

    @classmethod
    def poll(cls, context):
        """Check if the operator can be executed in the current context"""
        return context.selected_objects is not None and len(context.selected_objects) > 0

    def execute(self, context):
        """Execute the operator"""
        try:
            # Log the operation
            logger.log_operator_execution(self.bl_idname, context)

            # Get selected objects
            selected_objects = context.selected_objects

            # Perform operation on selected objects
            for obj in selected_objects:
                # Example operation: scale the object
                obj.scale *= self.scale_factor

            # Report success
            self.report({'INFO'}, f"Successfully processed {len(selected_objects)} objects")
            return {'FINISHED'}

        except Exception as e:
            # Log the error
            logger.log_error(str(e), exc_info=True)
            
            # Report error to user
            self.report({'ERROR'}, f"Error during execution: {str(e)}")
            return {'CANCELLED'}

    def invoke(self, context, event):
        """Called when the operator is invoked"""
        # Show the properties dialog
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        """Draw the operator properties dialog"""
        layout = self.layout
        layout.prop(self, "scale_factor")