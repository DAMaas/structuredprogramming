import web
from web import form

urls = (
  '/', 'Index'
)

SERVER_NAME = "ShopServ v0.1"
DISCLAIMER = "    Welcome to the webshop. TICT-AAI-GP-17_18  "

WEB_TEXT = dict()
WEB_TEXT['title'] = SERVER_NAME
WEB_TEXT['disclaimer'] = DISCLAIMER


# N.B. Gebruik hier een echte database.
# Zie dus ook http://webpy.org/tutorial3.en#databasing

# producten
COWBOYPAK = "cowboypak"
FOPSPEEN = "fopspeen"
HORLOGE = "horloge"
OORBELLEN = "oorbellen"
RAMMELAAR = "rammelaar"
ROMPERTJE = "rompertje"
SPEELGOEDAUTO = "speelgoedauto"
SPEELGOEDPOP = "speelgoedpop"

#categorie
CAT_BABY_KLEDING = "Kleding voor de baby"
CAT_BABY_SPEELGOED = "Speelgoed voor de baby"
CAT_SIERADEN = "Sieraden"

#doelgroep
DOEL_VOLWASSENEN = "Volwassenen"
DOEL_BABIES = "Babies"

recommend_db = {}

recommend_db[COWBOYPAK] = [DOEL_BABIES, CAT_BABY_SPEELGOED, [FOPSPEEN, RAMMELAAR, SPEELGOEDAUTO]]
recommend_db[RAMMELAAR] = [DOEL_BABIES, CAT_BABY_SPEELGOED, [FOPSPEEN, RAMMELAAR, SPEELGOEDAUTO]]
recommend_db[SPEELGOEDAUTO] = [DOEL_BABIES, CAT_BABY_SPEELGOED, [FOPSPEEN, RAMMELAAR, SPEELGOEDAUTO]]
recommend_db[SPEELGOEDPOP] = [DOEL_BABIES, CAT_BABY_SPEELGOED, [FOPSPEEN, RAMMELAAR, SPEELGOEDAUTO]]

recommend_db[FOPSPEEN] = [DOEL_BABIES, CAT_BABY_KLEDING, [ROMPERTJE, OORBELLEN, ""]]
recommend_db[ROMPERTJE] = [DOEL_BABIES, CAT_BABY_KLEDING, [FOPSPEEN, OORBELLEN, ""]]

recommend_db[OORBELLEN] = [DOEL_VOLWASSENEN, CAT_SIERADEN, [HORLOGE, FOPSPEEN,ROMPERTJE]]
recommend_db[HORLOGE] = [DOEL_VOLWASSENEN, CAT_SIERADEN, [OORBELLEN, "",""]]

class Index(object):
    
    def GET(self):
        render = web.template.render('templates')
        return render.start_form(WEB_TEXT)

    def POST(self):
        render = web.template.render('templates')
        form_f = web.input(zoeken="naamloos", type="zoeken")

        if form_f.zoeken in recommend_db:
            db_line = recommend_db[form_f.zoeken]
            
            prod_info = dict()
            prod_info["name"] = form_f.zoeken
            prod_info["target"] = db_line[0]
            prod_info["category"] = db_line[1]
            prod_info["rec0"] = db_line[2][0]
            prod_info["rec1"] = db_line[2][1]
            prod_info["rec2"] = db_line[2][2]

            prod_info["name_png"] = "static/producten/" + form_f.zoeken  + ".png"
            prod_info["rec0_png"] = "static/producten/" + db_line[2][0]  + ".png"
            prod_info["rec1_png"] = "static/producten/" + db_line[2][1]  + ".png"
            prod_info["rec2_png"] = "static/producten/" + db_line[2][2]  + ".png"

            render = web.template.render('templates')
            return render.product_page(WEB_TEXT, prod_info)

        else:
            return "Product niet gevonden. Probeer: cowboypak, rammelaar, fopspeen, oorbellen."


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
