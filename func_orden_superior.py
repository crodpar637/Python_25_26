def saludar(lang):
    def saludar_es():
        print ("Hola")
    def saludar_en():
        print ("Hello" )
    def saludar_fr():
        print ("Salut")
    lang_func ={"es":saludar_es,
                "en":saludar_en,
                "fr":  saludar_fr}
    
    return lang_func[lang]
    
f = saludar("es")
f()
f = saludar("en")
f()

saludar("fr")()


