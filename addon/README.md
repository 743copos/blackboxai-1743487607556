# Custom Blender Addon

A professional Blender addon that demonstrates core functionality by providing tools for scaling objects with a custom UI panel and comprehensive logging.

## Features

- Custom UI panel in the 3D Viewport sidebar
- Object scaling operator with adjustable scale factor
- Comprehensive logging system
- Unit testing suite
- Error handling and user feedback

## Requirements

- Blender 3.0.0 or newer
- Python 3.7 or newer (typically bundled with Blender)

## Installation

1. Download the addon as a ZIP file
2. Open Blender
3. Go to Edit > Preferences > Add-ons
4. Click "Install..." and select the downloaded ZIP file
5. Enable the addon by checking the checkbox next to it

## Usage

1. Open the 3D Viewport
2. Look for the "Custom Tab" in the sidebar (press N if the sidebar is hidden)
3. Select one or more objects in the viewport
4. Adjust the scale factor in the panel
5. Click "Scale Objects" to apply the scaling

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/custom-blender-addon.git
```

2. Create a symbolic link from the addon directory to Blender's addon directory:
```bash
ln -s /path/to/custom-blender-addon/addon /path/to/blender/version/scripts/addons/custom_addon
```

3. Enable the addon in Blender's preferences

## Testing

The addon includes a comprehensive test suite in `test_addon.py`. To run the tests:

1. Open Blender
2. Switch to the Scripting workspace
3. Open the `test_addon.py` file
4. Click "Run Script" or press Alt+P

The test results will be displayed in Blender's system console.

## File Structure

```
addon/
├── __init__.py          # Addon entry point and registration
├── operators.py         # Custom operator definitions
├── panels.py           # UI panel definitions
├── logger.py           # Logging utility
├── test_addon.py       # Unit tests
├── README.md           # This file
└── CHANGELOG.md        # Version history
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the tests
5. Submit a pull request

## Debugging

- Check Blender's system console for detailed error messages and logs
- Enable debug logging in `logger.py` by changing the log level to `logging.DEBUG`
- Use Blender's built-in Python console for interactive debugging

## Common Issues

1. **Addon doesn't appear in the sidebar**
   - Make sure the addon is enabled in preferences
   - Press N to show the sidebar
   - Check Blender's system console for registration errors

2. **Scale operator not working**
   - Ensure objects are selected before using the operator
   - Check if you're in Object mode
   - Look for error messages in the system console

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Version History

See [CHANGELOG.md](CHANGELOG.md) for a complete version history.

## Support

For support, please:
1. Check the documentation
2. Look for similar issues in the issue tracker
3. Create a new issue with detailed information about your problem

## Authors

- Your Name - Initial work

## Acknowledgments

- Blender Foundation for the excellent Python API
- The Blender community for inspiration and support