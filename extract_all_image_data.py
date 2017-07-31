from xml.dom import minidom
import sys

def read_image_file(image_name):
	filename = "concept-art/" + image_name + ".svg"
	output_string = ""
	doc = minidom.parse(filename)
	layers = [layer for layer in doc.getElementsByTagName('g')]
	for layer in layers:
	    layer_id = layer.getAttribute('inkscape:label')
	    output_string += "\t\t\"" + layer_id + "\": {"
	    for path in layer.getElementsByTagName('path'):
	        piece = path.getAttribute('id').split("-")[0]
	        pathstring = path.getAttribute('d')
	        output_string += "\"" + piece + "\":" + '"' + pathstring + '", '
	    output_string += "\t\t},"
	doc.unlink()
	return output_string

# python extract_all_image_data.py

def write_string_to_file(string, filename):
	target = open(filename, 'w')
	target.write(string)
	target.close()

full_file_string = ''

full_file_string += 'var image_data = {'

full_file_string += '\n'

full_file_string += '\t"fish":{'

full_file_string += '\n'

D_fish = read_image_file("fish")

full_file_string += D_fish

full_file_string += '\n'

full_file_string += '\t\t"colors": {"body":col1, "fin":col2, "crest":col2, "eye":white, "pupil":black, "target1":white, "target2":null, "target3":col3}'

full_file_string += '\n'

full_file_string += '\t},'

full_file_string += '\n'

full_file_string += '\t"flower":{'

full_file_string += '\n'

D_flower = read_image_file("flower")

full_file_string += D_flower

full_file_string += '\n'

full_file_string += '\t\t"colors": {"target1":col1, "target3":col5, "target2":col2, "stem":col1, "flowerfront":col3, "flowerback":Ecosystem.darken(col3), "center":col4}'

full_file_string += '\n'

full_file_string += '\t},'

full_file_string += '\n'

full_file_string += '\t"bug":{'

full_file_string += '\n'

D_bug = read_image_file("bug")

full_file_string += D_bug

full_file_string += '\n'

full_file_string += '\t\t"colors": {"legs":col1, "head":col2, "body":col3, "pupils":black, "eyes":white, "target1":col4, "target2":col5}'

full_file_string += '\n'

full_file_string += '\t},'

full_file_string += '\n'

full_file_string += '\t"bird":{'

full_file_string += '\n'

D_bird = read_image_file("bird")

full_file_string += D_bird

full_file_string += '\n'

full_file_string += '\t\t"colors": {"target1":col1, "target2":col1, "beak":yellow, "legs":col2, "body":col2, "head":col2, "wing":col3, "eye":black, "eye2":black, "eyebkg":white, "eyebkg2":white, "feet":gray}'

full_file_string += '\n'

full_file_string += '\t},'

full_file_string += '\n'

full_file_string += '\t"tree":{'

full_file_string += '\n'

D_tree = read_image_file("tree")

full_file_string += D_tree

full_file_string += '\n'

full_file_string += '\t\t"colors":{"target1":col1, "target2": col2, "trunk":col3, "branches":null}'

full_file_string += '\n'

full_file_string += '};'

write_string_to_file(full_file_string, 'ecosystem_data.js')
