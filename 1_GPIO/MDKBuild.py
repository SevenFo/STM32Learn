import os
import sys
# """
# Command	Description
# -b	Builds the last current target of a project and exits after the build process finished. Refer to option -t to change the target. For multi-projects, the command builds the targets as defined in the dialog Project - Batch Build.

# Examples:
# UV4 -b PROJECT1.uvprojx
# -c	Clean all project targets of a project. For a multi-project, the command cleans all targets that have been selected in the dialog Project - Batch Build. Refer to the note on Project Menu and Commands for details about the cleaning process.

# Examples:
# UV4 -c PROJECT1.uvprojx
# -cr	Clean all project targets and re-translate the last current target of a project. Refer to option -t to change the target. For multi-projects, the command cleans all targets and re-translates the targets as selected in the dialog Project - Batch Build. Refer to the note on Project Menu and Commands for details about the cleaning process.

# Examples:
# UV4 -cr PROJECT1.uvprojx
# -d	Starts µVision in Debugging Mode. Use this command together with a debug initialization file to execute automated test procedures. Exit the debugging session with the EXIT command.

# Examples:
# UV4 -d PROJECT1.uvprojx
# -f	Downloads the program to Flash and exits after the download process finished.

# Examples:
# UV4 -f PROJECT1.uvprojx -t"MCB2100 Board"
# -r	Re-translates the last current project target and exits after the build process finished. Refer to option -t to change the target. For multi-projects, the command re-translates the targets as defined in the dialog Project - Batch Build.

# Examples:
# UV4 -r PROJECT1.uvprojx -t"Simulator"
# -5	Converts a µVision 4 uvproj file into a µVision 5 uvprojx file. The only valid option with this command is -l for writing a log file.

# Examples:
# UV4 -5 myoldproject.uvproj -l log.txt
# If the conversion fails, error code 20 will be returned.
# -et	Exports a project target to <projectName>.<targetName>.cprj file. Use the option -t targetname to specify the target to be exported, otherwise the current target is used. Note that -et command with option -t, does not change the current target configuration in the project. No other options are supported with this command.

# Examples:
# UV4 -et myProject.uvprojx
# Export current target in myProject.uvprojx to myProject.<targetName>.cprj file.

# UV4 -et myProject.uvprojx -t "my-target"
# Export target "my-target" in myProject.uvprojx to myProject.my-target.cprj file.
# -ep	Exports all project targets to respective <projectName>.<targetName>.cprj files.

# Examples:
# UV4 -ep myProject.uvproj


# Option	Description
# -j0	Hides the µVision GUI. Messages are suppressed. Use this option for batch testing.
# -i import_file.xml	Creates a new project or updates an existing project using the data provided by an XML file, which has to be compliant to the schema project_import.xsd available in the directory ..\UV4. The target name may be specified with the option -t. If a project is created from the command line without -t, the device name is used as the name of the target. The GUI is suppressed automatically when using this option.

# Examples:
# UV4 MyProject.uvprojx –i MyImport.xml
# -l logfile	Saves the output of the command in the specified logfile.

# Examples:
# UV4 -5 myoldproject.uvproj -l log.txt
# If the conversion fails, error code 20 will be returned.
# -n device_name	Creates a new project with the specified device_name. The target name can be specified with the option -t. By default, the target name is set to the device name. The GUI is suppressed automatically when using this option.

# Examples:
# UV4 MyProject.uvprojx –n Device1234
# UV4 MyProject.uvprojx –i MyImport.xml –n Device5678 -t FlashDebug
# -t targetname	Sets targetname as the current target. If not specified, then the last known target is used.

# Examples:
# UV4 -r PROJECT1.uvprojx -t"MCB2100 Board"
# -o outputfile	Specifies the output log file.

# Examples:
# UV4 -r PROJECT1.uvprojx -o"listmake.prn"
# UV4 -r "C:\MyProjects\ARM\Example-mpw.uvmpw" -o "c:\temp\log.txt"
# -q	Re-builds the selected targets of a multiple-project. Ensure that each target has another object output folder. Use the menu Projects - Options for Target - Output - Select Folder for Objects.

# Examples:
# UV4 -r "C:\MyProjects\ARM\Example-mpw.uvmpwx" -q -o "c:\temp\log.txt"
# -z	Re-builds all targets of a project or multiple-project. Ensure that each target has another object output folder. Use the menu Projects - Options for Target - Output - Select Folder for Objects.

# Examples:
# UV4 -b PROJECT1.uvproj -z -o "c:\temp\log.txt"
# UV4 -b "C:\MyProjects\ARM\Example-mpw.uvmpwx" -q -z -o "c:\temp\log.txt"
# -x	Enables DDE mode and returns complete command output. This option can be used only with the command -d.
# -y	Enables DDE mode and returns only command confirmations. This option can be used only with the command -d.
# """
UVCommand = "-f"
pjFile=  "test.u"
UVCommand = sys.argv[1]
pjFile = sys.argv[2]
logFile = os.path.abspath(os.getcwd())+"\\output.log"
cmd = "C:\\Keil_v5\\UV4\\UV4.exe "+UVCommand+" "+'"'+pjFile+'"'+" "+"-j0 -o "+'"'+logFile+'"'
print(cmd)
print(os.system(cmd))
with open(logFile,"r+") as f:
    for l in f.readlines():
        print(l)
