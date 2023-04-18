
import bpy 

# Creating box1 with lid1
bpy.ops.mesh.primitive_cube_add(location= (0,0,0))
box1 = bpy.context.active_object
box1.name = "box1"
box1.scale = (3,3,3)

bpy.ops.mesh.primitive_cube_add(location=(0, 0, 3 + 0.5/2))
lid1 = bpy.context.active_object
lid1.name = "lid1"
lid1.scale = (3.25, 3.25, 0.5)


# Creating box2 with lid2
bpy.ops.mesh.primitive_cube_add(location= (0,7,0))
box2 = bpy.context.active_object
box2.name = "box2"
box2.scale = (2,2,2)

bpy.ops.mesh.primitive_cube_add(location=(0, 7, 2 + 0.5/2))
lid2 = bpy.context.active_object
lid2.name = "lid2"
lid2.scale = (2.25, 2.25, 0.5)

# Creating a sphere 
sphere_radius = 2
bpy.ops.mesh.primitive_uv_sphere_add(radius=sphere_radius, location=(0, 12, 0))
sphere = bpy.context.active_object
sphere.name = "sphere"

# import pencilbox.obj file created using luma ai 
file_loc = r"C:\Users\user\Desktop\ESE\ESE_sem_8\sem8_computer integrated manufacturing\Blender\pencilbox\pencilbox.obj"
imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
pencilbox = bpy.context.selected_objects[0]
pencilbox.location = (0,16,0)
pencilbox.name = "pencilbox"

