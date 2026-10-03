import bpy
bl_info = {
    "name": "AccuRIG Vertex Group Renamer and Combiner",
    "author": "Daggim Hailu",
    "version": (1, 4),
    "blender": (3, 50, 0),
    "location": "Object Data > Vertex Groups > AccuRIG Rename & Combine",
    "description": "Combine and rename AccuRIG vertex groups",
    "category": "Object",
}


# The mapping from AccuRIG group names to custom names
vertex_group_mapping = {
    'CC_Base_Hip': 'SKEL_Pelvis',
    'CC_Base_L_Foot': 'SKEL_L_Foot',
    'CC_Base_R_Foot': 'SKEL_R_Foot',
    'CC_Base_L_ToeBase': 'SKEL_L_Toe0',
    'CC_Base_R_ToeBase': 'SKEL_R_Toe0',
    'CC_Base_L_CalfTwist01': 'SKEL_L_Calf',
    'CC_Base_R_CalfTwist01': 'SKEL_R_Calf',
    'CC_Base_L_ThighTwist01': 'RB_L_ThighRoll',
    'CC_Base_R_ThighTwist01': 'RB_R_ThighRoll',
    'CC_Base_L_ThighTwist02': 'SKEL_L_Thigh',
    'CC_Base_R_ThighTwist02': 'SKEL_R_Thigh',
    'CC_Base_Waist': 'SKEL_Spine0',
    'CC_Base_Spine01': 'SKEL_Spine1',
    'CC_Base_Spine02': 'SKEL_Spine3',
    'CC_Base_Head': 'SKEL_Head',
    'CC_Base_L_Clavicle': 'SKEL_L_Clavicle',
    'CC_Base_R_Clavicle': 'SKEL_R_Clavicle',
    'CC_Base_L_ForearmTwist01': 'SKEL_L_Forearm',
    'CC_Base_R_ForearmTwist01': 'SKEL_R_Forearm',
    'CC_Base_L_ForearmTwist02': 'RB_L_ForeArmRoll',
    'CC_Base_R_ForearmTwist02': 'RB_R_ForeArmRoll',
    'CC_Base_L_Hand': 'SKEL_L_Hand',
    'CC_Base_R_Hand': 'SKEL_R_Hand',
    'CC_Base_L_UpperarmTwist01': 'RB_L_ArmRoll',
    'CC_Base_R_UpperarmTwist01': 'RB_R_ArmRoll',
    'CC_Base_L_UpperarmTwist02': 'SKEL_L_UpperArm',
    'CC_Base_R_UpperarmTwist02': 'SKEL_R_UpperArm',
    'CC_Base_L_Mid1': 'SKEL_L_Finger20',
    'CC_Base_L_Mid2': 'SKEL_L_Finger21',
    'CC_Base_L_Mid3': 'SKEL_L_Finger22',
    'CC_Base_R_Mid1': 'SKEL_R_Finger20',
    'CC_Base_R_Mid2': 'SKEL_R_Finger21',
    'CC_Base_R_Mid3': 'SKEL_R_Finger22',
    'CC_Base_L_Index1': 'SKEL_L_Finger10',
    'CC_Base_L_Index2': 'SKEL_L_Finger11',
    'CC_Base_L_Index3': 'SKEL_L_Finger12',
    'CC_Base_R_Index1': 'SKEL_R_Finger10',
    'CC_Base_R_Index2': 'SKEL_R_Finger11',
    'CC_Base_R_Index3': 'SKEL_R_Finger12',
    'CC_Base_L_Ring1': 'SKEL_L_Finger30',
    'CC_Base_L_Ring2': 'SKEL_L_Finger31',
    'CC_Base_L_Ring3': 'SKEL_L_Finger32',
    'CC_Base_R_Ring1': 'SKEL_R_Finger30',
    'CC_Base_R_Ring2': 'SKEL_R_Finger31',
    'CC_Base_R_Ring3': 'SKEL_R_Finger32',
    'CC_Base_L_Pinky1': 'SKEL_L_Finger40',
    'CC_Base_L_Pinky2': 'SKEL_L_Finger41',
    'CC_Base_L_Pinky3': 'SKEL_L_Finger42',
    'CC_Base_R_Pinky1': 'SKEL_R_Finger40',
    'CC_Base_R_Pinky2': 'SKEL_R_Finger41',
    'CC_Base_R_Pinky3': 'SKEL_R_Finger42',
    'CC_Base_L_Thumb1': 'SKEL_L_Finger00',
    'CC_Base_L_Thumb2': 'SKEL_L_Finger01',
    'CC_Base_L_Thumb3': 'SKEL_L_Finger02',
    'CC_Base_R_Thumb1': 'SKEL_R_Finger00',
    'CC_Base_R_Thumb2': 'SKEL_R_Finger01',
    'CC_Base_R_Thumb3': 'SKEL_R_Finger02',
    'CC_Base_NeckTwist01': 'RB_Neck_1',
    'CC_Base_NeckTwist02': 'SKEL_Neck_1',
    # ... add more mappings as needed
}

# Define the sets of groups to combine
combine_sets = [
    {
        'group_a': 'CC_Base_R_CalfTwist01',
        'group_b': 'CC_Base_R_CalfTwist02',
        'result': 'CC_Base_R_CalfTwist01',
    },
    {
        'group_a': 'CC_Base_L_CalfTwist01',
        'group_b': 'CC_Base_L_CalfTwist02',
        'result': 'CC_Base_L_CalfTwist01',
    },
    # Add more sets if needed
]


class OBJECT_OT_AccuRIGCombineAndRenameVertexGroups(bpy.types.Operator):
    """Combine and Rename AccuRIG Vertex Groups"""
    bl_idname = "object.accurig_combine_and_rename_vertex_groups"
    bl_label = "AccuRIG Combine and Rename Vertex Groups"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.type == 'MESH'

    def combine_vertex_groups(self, obj, group_a, group_b, result_name):
        # Check if the specified groups exist
        if group_a in obj.vertex_groups and group_b in obj.vertex_groups:
            # Add the Vertex Weight Mix modifier to combine the groups
            mod = obj.modifiers.new(
                name="VertexWeightMix", type='VERTEX_WEIGHT_MIX')
            mod.vertex_group_a = group_a
            mod.vertex_group_b = group_b
            mod.mix_mode = 'ADD'
            mod.mix_set = 'ALL'

            # Apply the modifier
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.modifier_apply(modifier=mod.name)

            # Rename the resulting group
            obj.vertex_groups[group_a].name = result_name

            return True
        return False

    def execute(self, context):
        obj = context.object
        renamed_groups = 0
        combined_groups = 0

        # Combine the vertex groups
        for group_set in combine_sets:
            if self.combine_vertex_groups(obj, group_set['group_a'],
                                          group_set['group_b'],
                                          group_set['result']):
                self.report({'INFO'},
                            f"Combined '{group_set['group_a']}' and '{group_set['group_b']}' into '{group_set['result']}'")
                combined_groups += 1

        # If no groups were combined, report it
        if combined_groups == 0:
            self.report(
                {'WARNING'}, "No groups were combined. Check group names.")

        # Rename the vertex groups
        for group in obj.vertex_groups:
            if group.name in vertex_group_mapping:
                group.name = vertex_group_mapping[group.name]
                renamed_groups += 1

        if renamed_groups:
            self.report({'INFO'}, f"Renamed {renamed_groups} vertex groups.")
        else:
            self.report(
                {'INFO'}, "No additional vertex groups found to rename.")

        return {'FINISHED'}


def add_object_button(self, context):
    self.layout.operator(
        OBJECT_OT_AccuRIGCombineAndRenameVertexGroups.bl_idname,
        text=OBJECT_OT_AccuRIGCombineAndRenameVertexGroups.bl_label,
    )


def register():
    bpy.utils.register_class(OBJECT_OT_AccuRIGCombineAndRenameVertexGroups)
    bpy.types.DATA_PT_vertex_groups.append(add_object_button)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_AccuRIGCombineAndRenameVertexGroups)
    bpy.types.DATA_PT_vertex_groups.remove(add_object_button)


if __name__ == "__main__":
    register()
