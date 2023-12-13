import os
import maya.cmds as cmds


PROJECT_PATH = os.path.join(os.path.dirname(__file__), "maya_projects")

def findProjectName(*arg):
	porjectsList = os.listdir(PROJECT_PATH)
	cmds.textScrollList("projectTSL", edit=true, removeAll=True)
	for project in porjectsList:
		cmds.textScrollList("projectTSL", edit=True, append=project)

def findFileName(*arg):
	selectedProject = cmds.textScrollList("projectTSL", query=True, selectItem=True)[0]
	
	filepath = os.path.join(PROJECT_PATH, selectedProject, "scenes")
	filesname = os.listdir(filepath)

	cmds.textScrollList("fileTSL", edit=true, removeAll=True)
	for file in filesname:
		
		file_ma = file.rpartition(".ma")[1]
		file_mb = file.rpartition(".mb")[1]
		if(file_ma == ".ma" || file_mb == ".mb"):
			cmds.textScrollList("fileTSL", edit=True, append=file)

def findFilePath(*arg):
	selectedProject = cmds.textScrollList("projectTSL", query=True, selectItem=True)[0]
	selectedFile = cmds.textScrollList("fileTSL", query=True, selectItem=True)[0]

	FilePath = os.path.join(PROJECT_PATH, selectedProject, "scenes", selectedFile)

def importMayaFile(mayaFileName, *arg):
	filePath = findFilePath()
	cmds.file(FilePath, i=True, ignoreVersion=True, force=True, ns=mayaFileName)

def referenceMayaFile(mayaFileName, *arg):
	filePath = findFilePath()
	cmds.file(FilePath, reference=True, ignoreVersion=True, force=True, ns=mayaFileName)

def openMayaFile(*arg):
	filePath = findFilePath()
	cmds.file(FilePath, open=True, ignoreVersion=True, force=True)
