import unittest
import bpy
import sys
import os

# Add addon directory to path so we can import our modules
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from . import operators
from . import panels
from . import logger

class TestCustomAddon(unittest.TestCase):
    """Test cases for Custom Blender Addon"""

    def setUp(self):
        """Setup for all tests"""
        # Create a test cube
        bpy.ops.mesh.primitive_cube_add()
        self.test_cube = bpy.context.active_object
        
        # Ensure we're in object mode
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

    def tearDown(self):
        """Cleanup after all tests"""
        # Delete test objects
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        
        # Clear any custom properties
        for prop in self.test_cube.keys():
            del self.test_cube[prop]

    def test_operator_registration(self):
        """Test if the operator can be registered"""
        try:
            bpy.utils.register_class(operators.CustomOperator)
            self.assertTrue(True, "Operator registered successfully")
        except Exception as e:
            self.fail(f"Failed to register operator: {str(e)}")
        finally:
            # Cleanup
            try:
                bpy.utils.unregister_class(operators.CustomOperator)
            except:
                pass

    def test_panel_registration(self):
        """Test if the panel can be registered"""
        try:
            bpy.utils.register_class(panels.CustomPanel)
            self.assertTrue(True, "Panel registered successfully")
        except Exception as e:
            self.fail(f"Failed to register panel: {str(e)}")
        finally:
            # Cleanup
            try:
                bpy.utils.unregister_class(panels.CustomPanel)
            except:
                pass

    def test_operator_execution(self):
        """Test if the operator executes correctly"""
        # Register operator
        bpy.utils.register_class(operators.CustomOperator)
        
        try:
            # Store original scale
            original_scale = self.test_cube.scale.copy()
            
            # Set scale factor
            scale_factor = 2.0
            
            # Execute operator
            bpy.ops.custom.operator(scale_factor=scale_factor)
            
            # Check if scale was applied correctly
            expected_scale = original_scale * scale_factor
            self.assertEqual(self.test_cube.scale.x, expected_scale.x)
            self.assertEqual(self.test_cube.scale.y, expected_scale.y)
            self.assertEqual(self.test_cube.scale.z, expected_scale.z)
            
        except Exception as e:
            self.fail(f"Operator execution failed: {str(e)}")
        finally:
            # Cleanup
            bpy.utils.unregister_class(operators.CustomOperator)

    def test_logger_setup(self):
        """Test if logger setup works correctly"""
        try:
            test_logger = logger.setup_logger()
            self.assertIsNotNone(test_logger)
            self.assertTrue(test_logger.handlers)
            self.assertEqual(test_logger.level, logger.logging.INFO)
        except Exception as e:
            self.fail(f"Logger setup failed: {str(e)}")

def main():
    """
    Run the test suite from Blender's text editor
    """
    # Create a TestLoader
    loader = unittest.TestLoader()
    
    # Create a TestSuite
    suite = unittest.TestSuite()
    
    # Add the tests to the suite
    suite.addTests(loader.loadTestsFromTestCase(TestCustomAddon))
    
    # Create a TextTestRunner
    runner = unittest.TextTestRunner(verbosity=2)
    
    # Run the suite
    runner.run(suite)

if __name__ == "__main__":
    main()