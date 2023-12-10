import bpy
import bmesh
import sys
import random
from sys import path

path.append(bpy.path.abspath("//") + '/RQGA')
from RQGA import rqga


# sys.stdout = open('output.txt', 'w')

def clean_scene():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_all(action='SELECT')

    bpy.ops.object.delete()

    # Optionally, remove any remaining data blocks (e.g., materials, textures) that are not in use
    bpy.ops.outliner.orphans_purge()

    # Add a monkey mesh to the scene
    monkey = bpy.ops.mesh.primitive_monkey_add(location=(0, 0, 0))


clean_scene()
list_splines_model = []
list_splines = []
keyframes = []
action = bpy.data.actions.new("MeshAnimation")
data_path = "vertices[%d].co"


def insert_keyframe(fcurves, frame, values):
    for fcu, val in zip(fcurves, values):
        fcu.keyframe_points.insert(frame, val, options={'FAST'})


def init_list_splines_model(object_name):
    obj = bpy.data.objects.get(object_name)

    if obj.type == 'MESH':
        mesh_data = obj.data
        vertices = mesh_data.vertices

        for vertex in vertices:
            x, y, z = vertex.co
            list_splines_model.append([round(x * 32 + 32), round(y * 32 + 32), round(z * 32 + 32)])
            vertex.co = (x * 32 + 32, y * 32 + 32, z * 32 + 32)
    else:
        print("Please select a 'MESH' object.")


def init_list_splines(val):
    for _ in range(len(list_splines_model)):
        list_splines.append([val, val, val])


def to_curve(object_name):
    obj = bpy.data.objects.get(object_name)

    if obj is not None:
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)

        bpy.ops.object.mode_set(mode='EDIT')

        bpy.ops.mesh.select_all(action='SELECT')

        bpy.ops.mesh.delete(type='ONLY_FACE')

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.convert(target='CURVE')
        bpy.context.object.data.bevel_depth = 1
        bpy.ops.object.shade_smooth(use_auto_smooth=True)
    else:
        print(f"L'objet '{object_name}' n'a pas été trouvé dans la scène.")


def create_obj(x, name, vertices, action):
    new_mesh = bpy.data.meshes.new("mesh")
    new_object = bpy.data.objects.new(name, new_mesh)

    new_mesh.animation_data_create()
    new_mesh.animation_data.action = action

    new_object.location = (x, 0, 0)

    bpy.context.collection.objects.link(new_object)

    bpy.context.view_layer.objects.active = new_object
    new_object.select_set(True)

    mesh_data = new_object.data
    mesh_data.from_pydata(vertices, [], [(0 + i, 1 + i, 2 + i, 3 + i) for i in range(len(vertices) - 4)])
    mesh_data.update()
    mesh_data.update(calc_edges=True)


def splines_evolution_v2(object_name, action):
    obj = bpy.data.objects.get(object_name)
    mesh_data = obj.data
    vertices = mesh_data.vertices
    vertice = 0

    for i in range(len(vertices)):
        fcurves = [action.fcurves.new(data_path % mesh_data.vertices[i].index, index=j) for j in range(3)]
        co_kf = (mesh_data.vertices[i].co.x, mesh_data.vertices[i].co.y, mesh_data.vertices[i].co.z)
        insert_keyframe(fcurves, i, co_kf)

        vertices[i].co = (rqga(list_splines_model[vertice][0], 7), \
                          rqga(list_splines_model[vertice][1], 7), \
                          rqga(list_splines_model[vertice][2], 7))
        vertice += 1

        co_kf = (mesh_data.vertices[i].co.x, mesh_data.vertices[i].co.y, mesh_data.vertices[i].co.z)
        insert_keyframe(fcurves, i + 1, co_kf)


model_name = "Suzanne"

init_list_splines_model(model_name)

to_curve(model_name)
init_list_splines(63)
create_obj(100, "Suzanne_evolutive", list_splines, action)
splines_evolution_v2("Suzanne_evolutive", action)

