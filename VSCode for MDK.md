# VSCode for MDK

基于STM32F429

## keil uVision5 部分

先在Keil uVision5中新建好项目，加入必要的依赖文件等

## VSCode 部分

### 解决头文件依赖与全局宏定义

#### 配置c_cpp_properties.json与tasks.json

+ 用VSCode打开项目文件夹，直接新建子目录`.vscode`并在该目录下新建两个配置文件`c_cpp_properties.json` `tasks.json`。
  或通过在VSCode中输入命令（F1）`C/C++:编辑配置(UI)`来生成配置文件

  ![image-20200514135258395](C:\Users\Fseven\AppData\Roaming\Typora\typora-user-images\image-20200514135258395.png)

  ![image-20200514135549050](C:\Users\Fseven\AppData\Roaming\Typora\typora-user-images\image-20200514135549050.png)

  

  + `c_cpp_properties.json` 

    IntelliSense（智能感知） 的配置文件

    + 在 包含路径 中添加头文件所在的目录，相当于在keil中配置Include Path

     ![image-20200514140047896](C:\Users\Fseven\AppData\Roaming\Typora\typora-user-images\image-20200514140047896.png)

    + 在 定义 中添加全局宏定义
      ![image-20200514140314083](C:\Users\Fseven\AppData\Roaming\Typora\typora-user-images\image-20200514140314083.png)

      **注意要加上**`__CC_ARM`  

    + 其他配置项目可参考VSCode的官方手册https://code.visualstudio.com/docs/cpp/configure-intellisense-crosscompilation

    + 最终形成的配置文件如下
    
      ```json
      {
          "configurations": [
              {
                  "name": "Win32",
                  "includePath": [
                      "C:\\Keil_v5\\ARM\\ARMCC\\include\\**",
                      "${workspaceFolder}/**",
                      "${workspaceFolder}/CORE/**",
                      "${workspaceFolder}/USER/**",
                      "${workspaceFolder}/SYSTEM/**",
                      "${workspaceFolder}/HALLIB/STM32F4xx_HAL_Driver/Inc/**",
                      "${workspaceFolder}/HALLIB/STM32F4xx_HAL_Driver/Src/**"
                  ],
                  "defines": [
                      "_DEBUG",
                      "UNICODE",
                      "_UNICODE",
                      "USE_HAL_DRIVER",
                      "STM32F429xx",
                      "__CC_ARM"
                  ],
                  "windowsSdkVersion": "10.0.18362.0",
                  "compilerPath": "",
                  "cStandard": "c11",
                  "cppStandard": "c++17",
                  "intelliSenseMode": "msvc-arm"
              }
          ],
          "version": 4
      }
      ```
    
      
  
  + `tasks.json`
    