m = 'Меня видно везде'

def a():
    ma = 'Меня видно в b() и a()'

    def b():
        print(m)
        print(ma)
        mb = 'Меня видно в c() и b(), но не видно в a()'

        def c():
            print(m)
            print(ma)
            print(mb)
            mc = 'Меня видно только в c()'

        # print(mc)
        c()
    b()
a()