import web

urls=(
    '/','Index'
)

app=web.application(urls,globals())

render=web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting="HELLO WORLD funk you up"
        foo="dfwfqrewgtuhtyujuyjku"
        # return render.index(greeting=greeting)
        return render.foo(greeting=foo)
    #render调用templates包

if __name__=="__main__":
    app.run()