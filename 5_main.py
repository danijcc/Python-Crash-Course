#funciona bien con la version 2.9.7 y 3.10.4 de python
#doc https://kivymd.readthedocs.io/en/latest/
#doc https://kivymd.readthedocs.io/en/0.104.1/index.html
#doc https://kivymd.readthedocs.io/en/0.104.2/components/text-field/index.html
from turtle import title
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
#set windows size
Window.size=(500,800)

KV='''
Screen:
    ScrollView:
        GridLayout:
            id: container_y
            size_hint_y: None
            cols: 1
            row_default_height: root.height*0.2
            height: self.minimum_height
            MDCard:
                size_hint: None, None
                size:500,1000
                pos_hint: {"center_x": 0.5, "center_y": 0.6}
                elevation: 10
                padding: 50
                spacing: 35
                orientation : 'vertical'
                MDIcon:
                    icon: 'engine'
                    icon_color: 0,0,0,0
                    halign: 'center'
                    font_size: 130
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                MDLabel:
                    text: "<<Calcular Relacion de Compresion>>" 
                    id: text
                    icon_left: "circle-slice-4"
                    width: 220
                    font_size: 20
                    halign: 'center'
                MDTextField:
                    id: valor1
                    icon_left: "circle-slice-4"
                    hint_text: "Diametro del cilindro"
                    helper_text: "Ingrese este dato en Pulgadas Cubicas"
                    foreground_color: 1,0,1,1
                    size_hint_x: None
                    width: 220
                    font_size: 20
                    pos_hint: {"center_x": 0.5, "center_y": 0.1}
                    mode: "fill"
                    fill_color: 0, 0, 0, .4
                    size_hint_x: .8
                    required: True
                    helper_text_mode: "on_error"
                MDTextField:
                    id: stroke
                    icon_left: "arrow-expand-vertical"
                    hint_text: "Carrera o Stroke del Piston"
                    helper_text: "Ingrese este dato en Pulgadas Cubicas"
                    foreground_color: 1,0,1,1
                    size_hint_x: None
                    width: 220
                    font_size: 20
                    pos_hint: {"center_x": 0.5}
                    mode: "fill"
                    fill_color: 0, 0, 0, .4
                    size_hint_x: .8
                    required: True
                    helper_text_mode: "on_error"
                MDTextField:
                    id: valor2
                    icon_left: "arrow-split-horizontal"
                    hint_text: "Volumen de la camara"
                    helper_text: "Ingrese este dato en Centimetros Cubicos"
                    foreground_color: 1,0,1,1
                    size_hint_x: None
                    width: 220
                    font_size: 20
                    pos_hint: {"center_x": 0.5}
                    mode: "fill"
                    fill_color: 0, 0, 0, .4
                    size_hint_x: .8
                    required: True
                    helper_text_mode: "on_error"
                MDTextField:
                    id: valor6
                    icon_left: "circle-slice-4"
                    hint_text: "Diametro de la empacadura"
                    helper_text: "Ingrese este dato en Pulgadas Cubicas"
                    foreground_color: 1,0,1,1
                    size_hint_x: None
                    width: 220
                    font_size: 20
                    pos_hint: {"center_x": 0.5}
                    mode: "fill"
                    fill_color: 0, 0, 0, .4
                    size_hint_x: .8
                    required: True
                    helper_text_mode: "on_error"
                MDTextField:
                    id: valor3
                    icon_left: "arrow-up-down-bold"
                    hint_text: "Espesor de la Empacadura"
                    helper_text: "Ingrese este dato en Pulgadas Cubicas"
                    foreground_color: 1,0,1,1
                    size_hint_x: None
                    width: 220
                    font_size: 20
                    pos_hint: {"center_x": 0.5}
                    mode: "fill"
                    fill_color: 0, 0, 0, .4
                    size_hint_x: .8
                    required: True
                    helper_text_mode: "on_error"
                MDTextField:
                    id: valor4
                    icon_left: "arrow-up-down-bold"
                    hint_text: "Espesor entre el piston y el punto muerto superior"
                    helper_text: "Ingrese este dato en Pulgadas Cubicas"
                    foreground_color: 1,0,1,1
                    size_hint_x: None
                    width: 220
                    font_size: 20
                    pos_hint: {"center_x": 0.3}
                    mode: "fill"
                    fill_color: 0, 0, 0, .4
                    size_hint_x: .9
                    required: True
                    helper_text_mode: "on_error"
                MDTextField:
                    id: valor5
                    icon_left: "arrow-split-horizontal"
                    hint_text: "Volumen de la corona o crown de la cabeza del piston"
                    helper_text: "Ingrese este dato en Centimetros Cubicos"
                    foreground_color: 1,0,1,1
                    size_hint_x: None
                    width: 220
                    font_size: 20
                    pos_hint: {"center_x": 0.3}
                    mode: "fill"
                    fill_color: 0, 0, 0, .4
                    size_hint_x: .9
                    required: True
                    helper_text_mode: "on_error"
                MDFillRoundFlatButton:
                    text: "CALCULAR RELACION DE COMPRESION"
                    font_size: 15
                    pos_hint: {"center_x": 0.5}
                    on_press: app.garage()
                MDLabel:
                    text: "<<---Design by Dani Colmenares--->>" 
                    id: text
                    icon_left: "circle-slice-4"
                    width: 220
                    font_size: 20
                    halign: 'center'
                    hint_text: "required = True"
                MDLabel:
                    text: "<<---danicolmenares7@gmail.com--->>" 
                    id: text
                    icon_left: "circle-slice-4"
                    width: 220
                    font_size: 20
                    halign: 'center'
                    hint_text: "required = True"


'''

class GarageApp(MDApp):
    

    def build(self):
        return Builder.load_string(KV)

    def garage(self):
        valor1 = self.root.ids.valor1.text
        stroke = self.root.ids.stroke.text
        valor2 = self.root.ids.valor2.text
        valor6 = self.root.ids.valor6.text
        valor3 = self.root.ids.valor3.text
        valor4 = self.root.ids.valor4.text
        valor5 = self.root.ids.valor5.text


        v1 = float(valor1) * float(valor1) * float(stroke)* 0.7854
        v2 = float(valor2) * 1 / 16.3871 
        v3 = float(valor6) * float(valor6) * float(valor3) * 0.7854
        v4 = float(valor1) * float(valor1) * float(valor4) * 0.7854
        v5 = float(valor5)* 1 / 16.3871
 
        v1 = round(v1,4)
        v2 = round(v2,4)
        v3 = round(v3,4)
        v4 = round(v4,4)
        v5 = round(v5,4)

        print(f'''
        ############################################################################
        VOLUMEN DE CILINDRO:.............................................[{v1}]
        VOLUMEN DE LA CAMARA:............................................[{v2}]
        VOLUMEN DE LA EMPACADURA:........................................[{v3}]
        VOLUMEN ENTRE PISTON Y BLOQUE DTC PUNTO MUERTO SUPERIOR:.........[{v4}]
        VOLUMEN CABEZA DEL PISTON:.......................................[{v5}]
        ############################################################################
        ''')

        volumen_de_la_camara_plano =  v2+v3+v4+v5
        volumen_del_cilindro_plano =  v1+v2+v3+v4+v5 
        volumen_de_la_camara_domo =  v2+v3+v4-v5
        volumen_del_cilindro_domo =  v1+v2+v3+v4-v5 

        resultado_piston_plano = volumen_del_cilindro_plano / volumen_de_la_camara_plano
        resultado_piston_domo = volumen_del_cilindro_domo / volumen_de_la_camara_domo 

        resultado_piston_plano = round(resultado_piston_plano,4)
        resultado_piston_domo = round(resultado_piston_domo,4)

        print(f'''
        ############################################################################
        RELACION DE COMPRESION PARA PISTON FLAT O PLANO:................[{resultado_piston_plano} A 1]
        RELACION DE COMPRESION PARA PISTON DOME O DOMO:.................[{resultado_piston_domo} A 1]
        ############################################################################

        ''')


    def close(self):
        self.dialog.dismiss()
        
GarageApp().run()        
                
            



       

