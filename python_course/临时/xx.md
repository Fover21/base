1. 根据要求实现如下功能：

   - 在python中有一个subprocess模块，可以通过代码去执行终端命令。

     - 在终端直接运行命令
       ![image-20210428114004136](../../../../视频教程/路飞Python/所有阶段-考试题/第3阶段（day24）/assets/image-20210428114004136.png)

     - 用python的subprocess模块执行命令

       ```python
       import subprocess
       
       cmd_object = subprocess.Popen(
           args='ls',
           shell=True,
           stdout=subprocess.PIPE,
           cwd="/Users/wupeiqi/PycharmProjects/luffyCourse/day24"
       )
       result = cmd_object.stdout.read()
       print(result)
       ```

       ![image-20210428113935357](../../../../视频教程/路飞Python/所有阶段-考试题/第3阶段（day24）/assets/image-20210428113935357.png)

   - 但，在 终端 会有一些特殊的命令。
     ![image-20210428114517012](../../../../视频教程/路飞Python/所有阶段-考试题/第3阶段（day24）/assets/image-20210428114517012.png)

     此时，如果使用subprocess的话，默认他会等到命令结束才读取结果（而命令默认会一直运行），所以，就导致无法读取结果。
     ![image-20210428114813558](../../../../视频教程/路飞Python/所有阶段-考试题/第3阶段（day24）/assets/image-20210428114813558.png)

2. 多进程，计算和数据隔离。