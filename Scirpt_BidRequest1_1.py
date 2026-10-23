import re

keywords_list = []
except_keywords_list = []
new_log = []
l = 0

def keywords_except_def(texto):
    for l in range(3):
        l += 1
    return except_keywords_list

def keywords_def(texto):
    keywords_list.append(texto)
    filtrar_log(keywords_list)
    
    return keywords_list

def filtrar_log(keywords_list, ruta_entrada="process_bids.log", ruta_salida="Script_Bids_Mod.log"):
    if not keywords_list:
            print("Aun no has agregado nada")
            return []

    with open(ruta_entrada, "r", encoding="utf-8") as f_input:
        for line in f_input:
            for keyword in keywords_list:
                line_wrote = False
                searching_for_keyword = re.findall(keyword.lower(),line.lower())
                if len(searching_for_keyword) > 0 and (line not in new_log):
                    new_log.append((line))
                    line_wrote = True
                if line_wrote:
                    break
        
    with open(ruta_salida, "w", encoding="utf-8") as f_output:
        for line in new_log:
            f_output.write(line)
        print(line)
    return ruta_salida