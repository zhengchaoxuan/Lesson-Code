"""
lesson1:第一种调用方式

Version : 0.1
Author  : 郑超轩
Date   : 2020/01/22
"""

from module1 import foo

#输出为hello,world
foo()

from module2 import foo

#输出为goodbye!
foo()

"""
lesson1:第二种调用方式

Version : 0.2
Author  : 郑超轩
Date   : 2020/01/22
"""

import module1 as m1
import module2 as m2 

m1.foo()
m2.foo()

"""
lesson1:覆盖

Version : 0.1
Author  : 郑超轩
Date   : 2020/01/22
"""
from module1 import foo
from module2 import foo

# 输出goodbye, world!
foo()