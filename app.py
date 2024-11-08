from flask import Flask, render_template 

app =  Flask (__name__)
@app.route ('/')
def index ():
    return render_template ('index.html')

@app.route ('/redes')
def redes():
    return render_template ('redes.html')

@app.route ('/contacto')
def contacto():
    return render_template ('contacto.html')














if __name__=="__main__":
     app.run(debug =True, port = 100)
