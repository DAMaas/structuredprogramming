# Nadat een random product wordt gekozen en de lijst met producten is geladen uit de database wordt het product gezocht dat de grootste absolute afwijking heeft in prijs (het random kiezen en het berekenen gebeurt ook hier in het procedurele programma).
# Put all results in a list and just do a max() on the list. To get absolute differences do some math and pipe it to abs(). Or do if randomselection > new: rand - new /// else new - randomselection


# Import dependencies


import MongoDB as mdb
import PostgreSQL as pg


# Initialize variables
firstDocument = mdb.getFirstDocument()
allDocuments = mdb.getAllDocuments()
