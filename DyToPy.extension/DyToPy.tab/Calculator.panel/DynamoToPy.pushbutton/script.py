"""Calcula totales de areas, volumenes y longitudes de elementos seleccionados."""

from Autodesk.Revit import DB

doc = __revit__.ActiveUIDocument.Document

#Seleccion de muros a utilizar
selection = __revit__.ActiveUIDocument.Selection.GetElementIds()
ElementSelection = [doc.GetElement(elId) for elId in selection]

total_length= 0.0
total_area=0.0
total_volume = 0.0
# Iterando sobre muros  
for wall in ElementSelection:
    length_param=wall.Parameter[DB.BuiltInParameter.CURVE_ELEM_LENGTH]
    area_param=wall.Parameter[DB.BuiltInParameter.HOST_AREA_COMPUTED]
    vol_param = wall.Parameter[DB.BuiltInParameter.HOST_VOLUME_COMPUTED]
    if vol_param or length_param or area_param:
        #Longitud en pies, se convierte a metros
        total_length = total_length + (length_param.AsDouble()/3.2808)
        #Area se convierte a metros
        total_area = total_area + (area_param.AsDouble()/10.764)

        #Volumen interno en pies cubicos, se convierte a metros cubicos
        total_volume = total_volume + (vol_param.AsDouble()/35.315)

# Enviando Valores totales a la interfaz de PyRevit
print("El Largo Total es: {} m".format(total_length))
print("El Area Total es: {} m2".format(total_area))
print("El Volumen Total es: {} m3".format(total_volume))
