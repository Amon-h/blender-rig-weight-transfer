# Blender GTA V Vertex Group Conversion Tool

A Blender Python tool I developed to automate repetitive vertex-group preparation when converting characters from a standard rig to a GTA V-compatible rig.

## What It Does

The tool automatically renames vertex groups from a source rig to their corresponding GTA V vertex-group names.

When the source rig contains multiple vertex groups that correspond to a single GTA V group, the tool also combines those groups into the appropriate GTA V vertex group.

This turns a repetitive manual conversion process into a one-click workflow.

## Example

### Before Conversion

The character uses vertex groups from the original character rig, with different naming conventions and, in some body areas, multiple groups where GTA V uses a single corresponding group.

![Before Vertex Group Conversion]<img width="1103" height="687" alt="pic1" src="https://github.com/user-attachments/assets/4f6a0e0e-edf6-41de-83db-7c4fbb3812ac" />


### After Conversion

The tool automatically renames the relevant vertex groups and combines groups where necessary to match the GTA V rig structure.

![After Vertex Group Conversion]<img width="426" height="590" alt="pic2" src="https://github.com/user-attachments/assets/5c075cae-da09-4716-8dac-4496135aa612" />


## Workflow

1. Start with a character using its original vertex-group structure.
2. Run the Blender tool.
3. The tool identifies and renames corresponding vertex groups.
4. Groups that need to be combined are merged automatically.
5. The character is left with a GTA V-compatible vertex-group structure.

## Benefits

* Automates repetitive vertex-group conversion work
* Renames vertex groups automatically
* Combines multiple source groups when required
* Reduces manual preparation time
* Converts the process into a one-click workflow
* Improves efficiency in my personal GTA V modding pipeline

## Technology

* Blender
* Python
* Vertex Groups
* Character Rigging
* GTA V Modding
* Asset Preparation

## Author

Amanueal Hailu
3D Game Artist | Technical Artist
