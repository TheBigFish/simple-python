# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'types'))
	print(os.getcwd())
except:
	pass
# %% [markdown]
# # python functions and methods
# 
# Function:  
# 1. Function is block of code that is also called by its name. (independent)  
# 2. The function can have different parameters or may not have any at all. If any data  (parameters) are passed, they are passed explicitly.  
# 3. It may or may not return any data.  
# 4. Function does not deal with Class and its instance concept.  
# 
# Method:  
# 1. Method is called by its name, but it is associated to an object (dependent).  
# 2. A method is implicitly passed the object on which it is invoked.  
# 3. It may or may not return any data.  
# 4. A method can operate on the data (instance variables) that is contained by the corresponding class  
# 
# Difference between method and function:  
# 1. Simply, function and method both look similar as they perform in almost similar way, but the key difference is the concept of ‘Class and its Object‘.  
# 2. Functions can be called only by its name, as it is defined independently. But methods can’t be called by its name only, we need to invoke the class by a reference of that class in which it is defined, i.e. method is defined within a class and hence they are dependent on that class.
# 
# 
# 
# 

# %%
import types


# %%
class D:
    var = None
    def __init__(self, name):
        self.name = name
        self.msg = None
    def f(self):
        print("f:" + self.name)


# %%
def e(self):
    print(self.name)

# %% [markdown]
# D.f 是一个 function:

# %%
print(D.f.__class__)
D.f

# %% [markdown]
# e 是一个 function:

# %%
print(type(e))
e

# %% [markdown]
# d.f 是一个 method:

# %%
d = D("hello")
print(d.f.__class__)
d.f()


# %%
vars(D)

# %% [markdown]
# 将function赋给D的属性，等同于在类里面定义function:

# %%
D.e = e
print(D.e)
vars(D)

# %% [markdown]
# 实例d可以调用方法e,此时，会传入self参数：

# %%
d.e()

# %% [markdown]
# 可以看到 e 此时变成了 d 的一个绑定方法，因此调用 d.e 会传入 self

# %%
d.e

# %% [markdown]
# 新建一个 function：

# %%
def g(self, msg):
    self.msg = msg
    print(str(self) + self.name + " " + self.msg)

# %% [markdown]
# 将普通函数赋给d，不会产生绑定：

# %%
d.g = g
vars(d)

# %% [markdown]
# 调用 g 不会传入self:

# %%
try:
    d.g("msg")
except Exception as e:
    print(e)


# %%
del d.g

# %% [markdown]
# 使用 types.MethodType 将产生一个绑定到对象的method：

# %%
types.MethodType(g, d)

# %% [markdown]
# 该绑定方法可以调用，调用时会自动传入绑定的对象当作第一个参数，此处是 d 传给 self：

# %%
types.MethodType(g, d)("msg")

# %% [markdown]
# 注意，单独调用 types.MethodType，并不会对对象造成影响:

# %%
vars(d)

# %% [markdown]
# 所以一般做法是把绑定方法赋值给对象:

# %%
d.g = types.MethodType(g, d)
vars(d)

# %% [markdown]
# 此时可以调用该绑定方法：

# %%
d.g("msg-d")

# %% [markdown]
# **注意**  
# 
# 绑定方法会在内部绑定对象，该方法调用时会使用该绑定的对象作为第一个参数（self 或者 cls）  
# 下面可以看到，d.g 和 d1.g 绑定的是同一个对象 d。

# %%
d1 = D("hello")
d1.g = types.MethodType(g, d)
d1.g("msg-d1")
print(d.msg)

# %% [markdown]
# 也可以将绑定方法赋值给类：

# %%
def h(cls, data):
    cls.var = data
    print(str(cls) + str(cls.var))

D.h = types.MethodType(h, D)

vars(D)

# %% [markdown]
# D.h 已经将方法绑定到 D，无论是 d.h 还是 D.h 调用，绑定方法都会将已绑定的 D 传给方法的第一个参数，此处是 cls:

# %%
d.h(2)
D.h(3)
print(D.var)


# %%


# %% [markdown]
# 采用 types.MethodType 赋值给对象的方法和在类中定义function的方法不同。  
# 类中定义的函数（比如f)由 Function 创建，Function 类似于一个描述符，拥有一个 __get__ 方法:  
# ```python
# class Function(object):
#     . . .
#     def __get__(self, obj, objtype=None):
#         "Simulate func_descr_get() in Objects/funcobject.c"
#         if obj is None:
#             return self
#         return types.MethodType(self, obj)
# ```
# 这样，在实例调用方法时，d.f，会触发描述符协议，调用 Function 的 `__get__`，返回一个绑定方法 `types.MethodType`
# %% [markdown]
# ## 总结：
# 1. 将function绑定到实例，使用MethodType，只对当前实例有效，调用时，实例会作为第一个参数传入， self 作用的对象为该绑定实例   
# 2. 将function绑定到类，使用MethodType，调用时，类会作为第一个参数传入，cls 作用的对象为该绑定类  
# 3. 如果需要类的所有实例都有绑定效果，则直接将function赋值给类属性，不需要使用 MethodType 方法。

# %%


