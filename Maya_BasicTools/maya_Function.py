import maya.cmds as cmds

def editName(*arg):

	#query name in textField
	textFieldInfo = cmds.textField("nameTextField", query=True, text=True)

	#count hashTag symbol
	numberHashTag = textFieldInfo.count("#")
	if(numberHashTag == 0):
		cmds.warning("FORGOT ADD HASHTAG")
		return
	totalHashTag = numberHashTag * "#"

	#create selection list
	objects = cmds.ls(selection = True)

	for i in range(len(objects)):
		cmds.rename(objects[i], textFieldInfo.replace(totalHashTag, str(i+1).zfill(numberHashTag)))

def addPrefix(*arg):

	#query prefix
	prefix = cmds.textField("prefixTextField", query = True, text = True)

	#add prefix
	objects = cmds.ls(selection = True)
	for i in objects:
		newName = prefix + i
		cmds.rename(i, newName)

def addSuffix(*arg):
	
	#query Suffix
	suffix = cmds.textField("suffixTextField", query = True, text = True)

	#add suffix
	objects = cmds.ls(selection = True)
	for i in objects:
		newName = i + suffix
		cmds.rename(i, newName)

def searchAndReplace(*arg):
	searchText =  cmds.textFieldGrp("searchTFG", q=True, text=True)
	replaceText = cmds.textFieldGrp("replaceTFG", q=True, text=True)

	objectsList = cmds.ls(sl=True)

	for i in objectsList:
		cmds.rename(i, i.replace(searchText,replaceText))

def changeColorsViewport(canvasNumber, *arg):
	RGB = cmds.canvas(f"canvas{canvasNumber}", q=True, rgb=True)
	allObjs = cmds.ls(sl=True)
	for obj in allObjs:
		shapes = cmds.listRelatives(obj, shapes=True)
		for shape in shapes:
			cmds.setAttr(f"{shape}.overrideEnabled", 1)
			cmds.setAttr(f"{shape}.overrideRGBColors", 1)
			cmds.setAttr(f"{shape}.overrideColorRGB", *RGB)
				
def changeColorsOutliner(canvasNumber, *arg):
	RGB = cmds.canvas(f"canvas{canvasNumber}", q=True, rgb=True)
	allObjs =  cmds.ls(sl=True)
	for obj in allObjs:
			cmds.setAttr(f"{obj}.useOutlinerColor", 1)
			cmds.setAttr(f"{obj}.outlinerColor", *RGB)

def changeColorGeneral(canvasNumber, *arg):
	viewportStatus = cmds.checkBox("colorViewport", q=True, v=True)
	outlinerStatus = cmds.checkBox("colorOutliner", q=True, v=True)

	if viewportStatus:
		changeColorsViewport(canvasNumber)
	
	if outlinerStatus:
		changeColorsOutliner(canvasNumber)

def unFreeTransform(*arg):
	selections = cmds.ls(sl=True)
	for obj in selections:
		parent = cmds.listRelatives(obj, parent=True)
		if parent:
			cmds.parent(obj, world=True)
			resetFretransform(obj)
			cmds.parent(obj, parent)
		else:
			resetFreetransform(obj)

def resetFreetransform(obj, *arg):
	cmds.makeIdentity(obj, apply=True, t=True)
	currentPosition = cmds.xform(obj, query=True, rp=True, ws=True)
	worldPivotParameter = [currentPosition[0]*-1,currentPosition[1]*-1,currentPosition[2]*-1] 
	cmds.xform(obj, t=worldPivotParameter, ws=True)
	cmds.makeIdentity(obj, apply=True, t=True)
	cmds.xform(obj, t=currentPosition, ws=True)
