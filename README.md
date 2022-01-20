# parseYamlVariable
####在yml用例描述中实现函数/变量的定义和调用


在Python语言中，函数的调用形式包含如下四种形式：
- 无参数：func()
- 顺序参数：func(a, b)
- 字典参数：func(a=1, b=2)
- 混合类型参数：func(1, 2, a=3, b=4)

于是，以上四种类型的函数定义在YAML/JSON中就会写成如下样子。

- 无参数：${func()}
- 顺序参数：${func(a, b)}
- 字典参数：${func(a=1, b=2)}
- 混合类型参数：${func(1, 2, a=3, b=4)}

yml文件是文本文件，无法直接写python代码，因此在加载yml文件时，需要识别出函数并完成调用。

#####目录结构：
annoymousLogin.yaml   ---用例文件

extract.yaml          ---存放变量的yml文件

parse.py              ---解析yaml文件内的函数与变量，输出结果

debugtalk.py          ---存放自定义函数的文件，其余py文件内的自定义函数可导入debugtalk.py内

yaml_util.py          ---读取用例并实现变量解析过程 


