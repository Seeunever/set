a = [{ "nickname" : "one", "age" : 20},  
{ "nickname" : "two", "age" : 22 }, 
{ "nickname" : "three", "age" : 21 }, 
{ "nickname" : "four" , "age" : 30 }] 
  
  
# 按 age 降序排序
print ("列表通过 age 降序排序: ")
print (sorted(a, key = lambda i: i['age'],reverse=True) )

# sorted()
# reverse = True 降序
# key 指定排序参数
# lambda 简化函数 i为函数接口 i['age']为函数体