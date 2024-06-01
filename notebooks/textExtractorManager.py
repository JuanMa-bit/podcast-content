import json
import os


class TextExtractorManager:
    def __init__(self,name_file):
        self.path_file_base = "/Users/jucampo/Desktop/Ideas/Podcast/podcast-content/data"
        self.datos = {}
        self.name_file = name_file
        self.path_file = os.path.join(self.path_file_base,self.name_file)
    def verificate_file(self):
        # Verificar si el archivo existe
        if not os.path.exists(self.path_file):
            # Si no existe, crear el archivo
            with open(self.path_file, 'w') as file:
                json.dump(self.datos, self.path_file, indent=4)
            print(f"Archivo creado en: {self.path_file}")
            
        else:
            print(f"El archivo ya existe en: {self.path_file}")
            print("archivo cargado")
            with open(self.path_file, 'r') as file:
                return json.load(file)
        
    def verificate_create_key(self, key, base_domain,section):
        """
        Verifica si una clave existe en un archivo JSON y, si no existe, la crea con un valor predeterminado.

        Args:
            ruta_archivo (str): La ruta del archivo JSON.
            clave (str): La clave que se va a verificar y, si es necesario, crear en el archivo JSON.
            valor_predeterminado (Any): El valor predeterminado que se asignará a la clave si no existe en el archivo JSON. Por defecto es None.

        Returns:
            dict: El contenido del archivo JSON actualizado.
        """

        try:
            with open(self.path_file, 'r') as file:
                contenido_json = json.load(file)
        except FileNotFoundError:
            contenido_json = {}
        
        if key not in contenido_json:
            contenido_json[key] = {base_domain:{section:{"text_extract":[],"idxs_advertisement":[]}}}
        else:
            if base_domain not in contenido_json[key]:
                contenido_json[key][base_domain]={section:{"text_extract":[],"idxs_advertisement":[]}}
            elif base_domain in contenido_json[key] and section not in contenido_json[key][base_domain].keys():
                contenido_json[key][base_domain][section]={"text_extract":[],"idxs_advertisement":[]}
             
        
        with open(self.path_file, 'w') as file:
            json.dump(contenido_json, file, indent=4)
    
    def add_text_extract(self, key, base_domain,section,l_text,l_idxs_advertisement):
        try:
            with open(self.path_file, 'r') as file:
                contenido_json = json.load(file)
        except FileNotFoundError:
            contenido_json = {}

        contenido_json[key][base_domain][section]={"text_extract":l_text,"idxs_advertisement":l_idxs_advertisement}
        with open(self.path_file, 'w') as file:
            json.dump(contenido_json, file, indent=4)
    def get_url(self,theme,idx_domain,idx_section):
        self.path_file = os.path.join(self.path_file_base,name_file)
        try:
            with open(self.path_file, 'r') as file:
                contenido_json = json.load(file)
        except FileNotFoundError:
            contenido_json = {}

        domain = list(contenido_json[theme].keys())[idx_domain]
        section = list(contenido_json[theme][domain].keys())[idx_section]
        url = domain + section
        print("url domain "+str(idx_domain)+" section"+str(idx_section)+": ",url)
        return url
    def get_text(self,theme,idx_domain,idx_section):
        dict_all = self.verificate_file()
        domain = list(dict_all[theme].keys())[idx_domain]
        section = list(dict_all[theme][domain].keys())[idx_section]
        dict_text = dict_all[theme][domain][section]
        return [valor for indice, valor in enumerate(dict_text['text_extract']) if indice not in dict_text['idxs_advertisement']]