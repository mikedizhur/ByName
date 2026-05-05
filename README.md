# Select By Name
Blender addon to select objects in a scene if they contain a string. Like "select pattern" but I think that didn't exist when the addon was written. 
Unlike "select pattern" doesn't use regex, just simple string matching. Adds an option to unhide hidden objects if they match the string (the only reason to use this instead of "select pattern" now).

## Usage
You can find the option in the `3D view > Select` menu.

If multiple strings separated by spaces are entered, selects objects that match ALL of them.
