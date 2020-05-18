import json
import os
import sys
import shutil
import conf
"""
@ params: armDir：arm-gcc的安装路径；STMModle: stm的型号，如STM32F429xx
"""
def generateCPJson(armDir="C:\\Program Files (x86)\\GNU Tools Arm Embedded\\9 2019-q4-major\\",STMModle="STM32F429xx"):
    c_cpp_properties = {
    "configurations": [
            {
                "name": "Win32",
                "includePath": [
                    "${workspaceFolder}/**",
                    "${workspaceFolder}/Inc",
                    "${workspaceFolder}/Drivers/STM32F4xx_HAL_Driver/Inc",
                    "${workspaceFolder}/Drivers/STM32F4xx_HAL_Driver/Inc/Legacy",
                    "${workspaceFolder}/Drivers/CMSIS/Device/ST/STM32F4xx/Include",
                    "${workspaceFolder}/Drivers/CMSIS/Include",
                    "${workspaceFolder}/Drivers/CMSIS/Include",
                    # "c:\\program files (x86)\\gnu tools arm embedded\\9 2019-q4-major\\bin\\../lib/gcc/arm-none-eabi/9.2.1/../../../../arm-none-eabi/include/c++/9.2.1",
                    # "c:\\program files (x86)\\gnu tools arm embedded\\9 2019-q4-major\\bin\\../lib/gcc/arm-none-eabi/9.2.1/../../../../arm-none-eabi/include/c++/9.2.1/arm-none-eabi",
                    # "c:\\program files (x86)\\gnu tools arm embedded\\9 2019-q4-major\\bin\\../lib/gcc/arm-none-eabi/9.2.1/../../../../arm-none-eabi/include/c++/9.2.1/backward",
                    #"c:\\program files (x86)\\gnu tools arm embedded\\9 2019-q4-major\\bin\\../lib/gcc/arm-none-eabi/9.2.1/include",
                    # "c:\\program files (x86)\\gnu tools arm embedded\\9 2019-q4-major\\bin\\../lib/gcc/arm-none-eabi/9.2.1/include-fixed",
                    # "c:\\program files (x86)\\gnu tools arm embedded\\9 2019-q4-major\\bin\\../lib/gcc/arm-none-eabi/9.2.1/../../../../arm-none-eabi/include"
                    armDir+"arm-none-eabi\\include\\c++\\9.2.1",
                    armDir+"arm-none-eabi\\include\\c++\\9.2.1\\arm-none-eabi",
                    armDir+"arm-none-eabi\\include\\c++\\9.2.1\\backward",
                    armDir+"lib\\gcc\\arm-none-eabi\\9.2.1\\include",
                    armDir+"lib\\gcc\\arm-none-eabi\\9.2.1\\include-fixed",
                    armDir+"arm-none-eabi\\include"
                ],
                "defines": [
                    "_UNICODE",
                    "USE_HAL_DRIVER",
                    "__GNUC__",
                    STMModle
                ],
                "windowsSdkVersion": "10.0.18362.0",
                "compilerPath": armDir+"bin\\arm-none-eabi-gcc.exe",
                "cStandard": "c11",
                "cppStandard": "c++17",
                "intelliSenseMode": "gcc-x64",
                "compilerArgs": []
            }
        ],
        "version": 4
    }
    return c_cpp_properties
def generateLaucnJson(configFiles = ["stlink.cfg","stm32f4x.cfg"],svdFile = "STM32F429x.svd",projectName = "GPIOFromCube"):
    lauch = {
    # 使用 IntelliSense 了解相关属性。 
    # 悬停以查看现有属性的描述。
    # 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug (J-Link)",
            "type": "cortex-debug",
            "request": "launch",
            "servertype": "openocd",
            "cwd": "${workspaceFolder}",#work directory
            "executable": "build/"+projectName+".elf",
            "device": "STM32F429IG",
            //"interface": "jtag",
            "preLaunchTask": "Build",#先运行Build任务
            "configFiles":configFiles,
            "svdFile": svdFile
        }

    ]
    }
    return lauch
def generateTaskJson():
    tasks = {
    "tasks": [
        {
            "type": "shell",
            "label": "Build",
            "command": "make",
            "group": "build",
            "problemMatcher":"$gcc"
        }
    ],
    "version": "2.0.0"
    }
    return tasks

def copyFile(svdDir = "C:\\Users\\Fseven\\.vscode\\extensions\\marus25.cortex-debug-dp-stm32f4-1.0.0\\data\\",openocdDir = "C:\\Program Files (x86)\\OpenOCD-20200503-0.10.0\\"):
    try:
        shutil.copy(svdDir+conf.svdModleName+".svd",conf.projectDir)
        shutil.copy(openocdDir+"share\\openocd\\scripts\\interface\\stlink.cfg",conf.projectDir)
        shutil.copy(openocdDir+"share\\openocd\\scripts\\interface\\jlink.cfg",conf.projectDir)
        shutil.copy(openocdDir+"share\\openocd\\scripts\\target\\"+conf.openocdModleName+".cfg",conf.projectDir)
        shutil.copy(openocdDir+"share\\openocd\\scripts\\target\\swj-dp.tcl",conf.projectDir)
        shutil.copy(openocdDir+"share\\openocd\\scripts\\mem_helper.tcl",conf.projectDir)
        print("copy SUCCESSED")
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())

def stmconfChanger():
    with open(conf.openocdModleName+".cfg","r") as f:
        fileContent = f.read()
        fileContent = fileContent.replace("target/swj-dp.tcl","swj-dp.tcl")
    with open(conf.openocdModleName+".cfg","w") as f:
        f.write(fileContent)
    print("changed")
