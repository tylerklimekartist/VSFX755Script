import maya.cmds as cmds
from random import uniform, choice

def add_string(attrname, paths):
	
	attrname = 'mtoa_constant_' + attrname
	shapes = []
	selections = cmds.ls(sl=True)
	for sel in selections:
		shapes = cmds.listRelatives(sel, shapes=True)
		# sel in a group
		if shapes == None:
			transforms = cmds.listRelatives(sel, children=True)
			shapes = []
			for tran in transforms:
				shapes.extend(cmds.listRelatives(tran,shapes=True))
				
		if len(shapes) == 0 or len(shapes[0]) == 0:
			print('Cannot find a shape to add attribute')
			continue
		for shape in shapes:
			if cmds.attributeQuery(attrname, node= shape, exists=True) == False:
				cmds.addAttr(shape, ln=attrname, sn=attrname, nn=attrname, dt="string")
			
			path= choice(paths)
			cmds.setAttr(shape + '.' + attrname, path, type ="string")

#=======================================================================================

def add_rand_float(attrname, min_max_value, min_max=[0,10.0]):
	attrname = 'mtoa_constant_' + attrname
	#selections will be either a number of shapes (possibly only one shape),
	#or one or more groups that contain shapes.
	selections = cmds.ls(sl=True)
	for sel in selections:
		shapes = cmds.listRelatives(sel, shapes=True)
		# sel in a group
		if shapes == None:
			transforms = cmds.listRelatives(sel, children=True)
			shapes = []
			for tran in transforms:
				shapes.extend(cmds.listRelatives(tran,shapes=True))
				
		if len(shapes) == 0 or len(shapes[0]) == 0:
			print('Cannot find a shape to add attribute')
			return
		for shape in shapes:
			if cmds.attributeQuery(attrname, node=shape, exists=True) == False:
				cmds.addAttr(shape, ln=attrname, sn=attrname, nn= attrname, 
							k=True, at='double',
							min=min_max[0], max=min_max[1], dv=0)
			value = uniform(min_max_value[0], min_max_value[1])
			cmds.setAttr(shape + '.' + attrname, value)
			
#=======================================================================================

def add_rand_int(attrname, min_max_value, min_max=[0,10.0]):
	attrname = 'mtoa_constant_'+attrname
	shapes = []
	selections = cmds.ls(sl=True)
	for sel in selections:
		shapes = cmds.listRelatives(sel, s=True)
		# sel is a shape, therefore, does not have shape relatives
		if shapes == None:
			transforms = cmds.listRelatives(sel, children=True)
			shapes = []
			for tran in transforms:
				shapes.extend(cmds.listRelatives(tran, shapes=True))
		if len(shapes) == 0 or len(shapes[0]) == 0:
			print('Cannot find a shape to add attribute')
			continue
		for shape in shapes:
			if cmds.attributeQuery(attrname, node=shape, exists=True) == False:
				cmds.addAttr(shape, ln=attrname, sn=attrname, at='long',  
						min=min_max[0], max=min_max[1], dv=0)
			value = uniform(min_max_value[0], min_max_value[1])
			cmds.setAttr(shape + '.' + attrname, value)

#=======================================================================================		

def add_rand_color(attrname, min_rgb, max_rgb):
	attrname = 'mtoa_constant_'+ attrname
	shapes = []
	selections = cmds.ls(sl=True)
	for sel in selections:
		shapes = cmds.listRelatives(sel, s=True)
		if shapes == None:
			transforms = cmds.listRelatives(sel, children = True)
			shapes = []
			for tran in transforms:
				shapes.extend(cmds.listRelatives(tran, shapes = True))
		if len(shapes) == 0 or len (shapes[0]) ==0:
			print ('Cannot find a shape to add attribute')
			continue
	for shape in shapes:
		if cmds.attributeQuery(attrname, node=shape, exists=True) == False:
			cmds.addAttr(shape, ln=attrname, sn=attrname, nn=attrname, at='float3', 
						usedAsColor=True, k=True)
			red = attrname + "_r"
			green = attrname + "_g"
			blue = attrname + "_b"
			cmds.addAttr(shape, ln = red, at ="float", k=True, parent=attrname)
			cmds.addAttr(shape, ln = green, at ="float", k=True, parent=attrname)
			cmds.addAttr(shape, ln = blue, at ="float", k=True, parent=attrname)
			
		r = uniform(min_rgb[0], max_rgb[1])
		g = uniform(min_rgb[0], max_rgb[1])
		b = uniform(min_rgb[0], max_rgb[1])
		cmds.setAttr(shape + '.' + attrname,r,g,b, type="float3")





