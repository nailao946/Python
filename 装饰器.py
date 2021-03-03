def wardecide(fn):
    def canjoin(name, age, *args, **kwargs):
        # star = kwargs['star'] # 拿一个为star的数据，如果没有会报错，所以选择下面的
        star = kwargs.get('star', 0)  # 如果没有填写则自动返回0为默认值
        if age >= 18:
            fn(name, age)
        elif star >= 3:
            print('注意:\n未满18岁！\n3星级及以上用户，允许参加')
        else:
            print('你不能参加')

    return canjoin


@wardecide
def message(name, age):
    print('你符合条件：\n名字：{}\n年龄：{}'.format(name, age))


message('李耀', 17, star=8)
