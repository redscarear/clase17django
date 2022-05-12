from datetime import datetime
from django.template import Template, Context
from django.http import HttpResponse
def saludo(request):
    return HttpResponse("Hola Django - Coder")
def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")
def diaDeHoy(request):

    dia = datetime.now()

    documentoDeTexto = f"Hoy es día: <br> {dia}"


    return HttpResponse(documentoDeTexto)
def miNombreEs(self, nombre, edad):

      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre} <br><br> Mi edad es: {edad}"


      return HttpResponse(documentoDeTexto)
def calcular_cumpleanio(self, edad):
    anioactual = datetime.now().year
    cumpleanio = anioactual - int(edad)
    return HttpResponse(f'<br><br> Naci el: {cumpleanio}')

def calcular_edad(self, cumple):
    cumple = datetime.strptime(cumple, '%Y-%m-%d')
    print(type(cumple))
    delta_time = datetime.now() - cumple
    diasdelanio = 365.25

    http_response = '''
    <br><br>
    Yo tengo {anios} anios, {meses} meses, {dias} dias. '''.format(
        anios = int(delta_time.days // diasdelanio),
        meses = int((delta_time.days % diasdelanio) //30),
        dias = int((delta_time.days % diasdelanio) //30),
    )
    return HttpResponse(http_response)

def probandoTemplate(self):

    miHtml = open(r"D:\Programacion\python\PythonProyecto1\live_class\live_class\templates\template.html","r")

    template = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = template.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)