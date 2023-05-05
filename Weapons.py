import tkinter as tk
from tkinter import messagebox
import xml.etree.ElementTree as ET

def convert_xml():
    try:
        xml_input = input_box.get('1.0', 'end-1c')
        root = ET.fromstring(xml_input)
        new_xml = '<primary>\n'
        for child in root:
            if child.attrib['ware'] == 'computronicsubstrate':
                ratio = 6/2
                new_xml += f'\t<ware ware="aicores" amount="{int(child.attrib["amount"])*ratio:.0f}" />\n'
            elif child.attrib['ware'] == 'metallicmicrolattice':
                ratio = 24/44
                new_xml += f'\t<ware ware="fusionbatteries" amount="{int(child.attrib["amount"])*ratio:.0f}" />\n'
            elif child.attrib['ware'] == 'energycells':
                ratio = 71/50
                new_xml += f'\t<ware ware="energycells" amount="{int(child.attrib["amount"])*ratio:.0f}" />\n'
            elif child.attrib['ware'] == 'siliconcarbide':
                ratio = 4/3
                new_xml += f'\t<ware ware="siliconcarbide" amount="{int(child.attrib["amount"])*ratio:.0f}" />\n'
        new_xml += '</primary>'
        output_box.delete('1.0', 'end')
        output_box.insert('1.0', new_xml)
    except Exception as e:
        messagebox.showerror('Error', str(e))

# Create a window
window = tk.Tk()
window.title('XML Converter')

# Create an input box
input_label = tk.Label(window, text='Input XML:')
input_label.pack()
input_box = tk.Text(window, height=10, width=50)
input_box.pack()

# Create a button to convert the XML
convert_button = tk.Button(window, text='Convert', command=convert_xml)
convert_button.pack()

# Create an output box
output_label = tk.Label(window, text='Output XML:')
output_label.pack()
output_box = tk.Text(window, height=10, width=50)
output_box.pack()

# Start the GUI
window.mainloop()
