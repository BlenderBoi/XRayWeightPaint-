

bl_info = {
    "name": "Simple Tweaks",
    "author": "BlenderBoi",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "3D View",
    "description": "A Collection of Minor Tweaks to Blender",
    "warning": "",
    "doc_url": "",
    "category": "Utility",
}



from . import WeightPaintBrush_Menu


modules =  [WeightPaintBrush_Menu] 

def register():


    for module in modules:
        module.register()

def unregister():

    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
