"""
Create UI script
"""
from imp import reload
from functools import partial
import maya.cmds as cmds
import huyScript.maya_Function as func
import huyScript.projectManager as manager
reload(func)

def createUI():

	#delete UI window
	if cmds.window("UIwindow", exists = True):
		cmds.deleteUI("UIwindow")

	#create UI window
	cmds.window("UIwindow", title = "Tools", menuBar=True)

	#create UI menu
	cmds.menu(label="General Scripts", tearOff=True)
	cmds.menuItem(divider=True)
	cmds.menuItem(l="unFreeTransform", c=func.unFreeTransform)
	cmds.menuItem(divider=True, dividerLabel = "personal")

	#Main Layout
	cmds.columnLayout("MainLayout",w=300)
	renameFrameLayout()
	colorFrameLayout()
	projectManagerLayout()

	#show UI window
	cmds.showWindow("UIwindow")

def renameFrameLayout():
	#Frame
	cmds.frameLayout("renameFrameLayout",label="    RENAME", w=300, cll = True, cl=False, bgc = [0.022,0.171,0.337], p="MainLayout")

	generalRenameUI()
	
	addPrefixSuffixUI()
	
	searchAndReplaceUI()

def projectManagerLayout():

	cmds.frameLayout("projectManagerLayout", l="    PROJECT MANAGER", w=300, cll = True, cl=False, bgc = [0.9,0.32,0.24], p="MainLayout")

	projectManagerUI()
	
def generalRenameUI():
	#Rename
	cmds.rowLayout(w=300, h=25, nc=2, p="renameFrameLayout")
	cmds.textField("nameTextField", w=250, h=25, pht="Example: project_object_#####")
	cmds.button(l="Rename", w=50, h=25, bgc=[1,0.171,0.337], c=func.editName)
	cmds.setParent("..")

def addPrefixSuffixUI():
	cmds.rowLayout(w=300, h=25, nc=4, p="renameFrameLayout")
	cmds.textField("prefixTextField", w=98.5, h=25, pht="prefix_")
	cmds.button(l="Add", w=50, h=25, bgc=[1,0.171,0.337], c=func.addPrefix)
	cmds.textField("suffixTextField", w=98.5, h=25, pht="_suffix")
	cmds.button(l="Add", w=50, h=25, bgc=[1,0.171,0.337], c=func.addSuffix)
	cmds.setParent("..")
	
def searchAndReplaceUI():
	cmds.columnLayout(w=300, p="renameFrameLayout")
	cmds.textFieldGrp("searchTFG", l="Search for:", w=300, h=25, cw=[(1,70),(2,227)])
	cmds.textFieldGrp("replaceTFG", l="Replace for:", w=300, h=25, cw=[(1,70),(2,227)])
	cmds.button(l="Search and Replace", w=300, h=40, c=func.searchAndReplace)

def colorFrameLayout():
	#Frame
	cmds.frameLayout("colorFrameLayout",label="    COLOR", w=300, cll = True, cl=False, bgc = [0.066,0.404,0.016], p="MainLayout")
	colorLayout()

def colorLayout():
	cmds.rowLayout(nc=2, w=300, p="colorFrameLayout")
	cmds.columnLayout(w=70)
	cmds.checkBox("colorViewport", l="Viewport", v=True)
	cmds.checkBox("colorOutliner", l="Outliner", v=False)
	cmds.setParent("..")

	cmds.rowColumnLayout(nc=6)
	cmds.canvas("canvas1", w=36, h=22, rgb=[1,0,0], pc=partial(func.changeColorGeneral, 1))
	cmds.canvas("canvas2", w=36, h=22, rgb=[0,1,0], pc=partial(func.changeColorGeneral, 2))
	cmds.canvas("canvas3", w=36, h=22, rgb=[0,0,1], pc=partial(func.changeColorGeneral, 3))
	cmds.canvas("canvas4", w=36, h=22, rgb=[1,1,0], pc=partial(func.changeColorGeneral, 4))
	cmds.canvas("canvas5", w=36, h=22, rgb=[0,1,1], pc=partial(func.changeColorGeneral, 5))
	cmds.canvas("canvas6", w=36, h=22, rgb=[1,0,1], pc=partial(func.changeColorGeneral, 6))

	
	cmds.canvas("canvas7", w=36, h=22, rgb=[1,0.3,0.2], pc=partial(func.changeColorGeneral, 7))
	cmds.canvas("canvas8", w=36, h=22, rgb=[0.3,1,0.2], pc=partial(func.changeColorGeneral, 8))
	cmds.canvas("canvas9", w=36, h=22, rgb=[0.3,0.2,1], pc=partial(func.changeColorGeneral, 9))
	cmds.canvas("canvas10", w=36, h=22, rgb=[1,1,1], pc=partial(func.changeColorGeneral, 10))
	cmds.canvas("canvas11", w=36, h=22, rgb=[0,0,0], pc=partial(func.changeColorGeneral, 11))
	cmds.canvas("canvas12", w=36, h=22, rgb=[1,1,1], pc=partial(func.changeColorGeneral, 12))

def projectManagerUI():
	cmds.rowColumnLayout(nc=2, w=300)

	cmds.textScrollList("projectTSL", w=140, selectCommand=manager.findFileName)

	cmds.textScrollList("fileTSL", w=140, doubleClickCommand=manager.openMayaFile, selectCommand = popupMenuMayaFile)

	cmds.setParent("..")

	cmds.button(l="Refresh", w=300, h=20, c=manager.findProjectName)

	manager.findProjectName()

def popupMenuMayaFile():
	selectedFile = cmds.textScrollList("fileTSL", query=True, selectItem=True)[0]

	if cmds.popupMenu("mayaFilePM", exixts=True)
		cmds.deleteUI("mayaFilePM")

	cmds.popupMenu("mayaFilePM", parent="fileTSL")
	cmds.menuItem(label = f"import:  {selectedFile}", command=partial(manager.importMayaFile, selectedFile))
	cmds.menuItem(label = f"reference:  {selectedFile}", command=partial(manager.referenceMayaFile, selectedFile))
