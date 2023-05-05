import xml.etree.ElementTree as ET
import tkinter as tk

multiplier_options = {
    'XL': {'energycells': 17.2, 'metallicmicrolattice': 39.8},
    'L': {'energycells': 21.4, 'metallicmicrolattice': 49.6},
    'M': {'energycells': 8.77, 'metallicmicrolattice': 20.17},
    'S': {'energycells': 10.95, 'metallicmicrolattice': 25.4}
}

def convert_xml():
    xml_text = input_text.get(1.0, tk.END)
    try:
        root = ET.fromstring(f'<root>{xml_text}</root>')
        primary_elem = root.find('primary')
        if primary_elem is None:
            raise ValueError('No primary element found')
        multiplier_option = multiplier_var.get()
        multiplier_dict = multiplier_options[multiplier_option]
        for ware_elem in primary_elem.findall('ware'):
            if ware_elem.get('ware') == 'computronicsubstrate':
                primary_elem.remove(ware_elem)
            elif ware_elem.get('ware') in multiplier_dict:
                multiplier = multiplier_dict[ware_elem.get('ware')]
                ware_elem.set('amount', str(round(int(ware_elem.get('amount'))*multiplier)))
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, ET.tostring(primary_elem).decode())
    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f'Error: {e}')

# Create GUI window
root = tk.Tk()
root.title("XML Converter")

# Create input text box
input_label = tk.Label(root, text="Input XML code:")
input_label.pack()
input_text = tk.Text(root, height=10, width=50)
input_text.pack()

# Create multiplier options
multiplier_var = tk.StringVar()
multiplier_var.set('XL')
multiplier_label = tk.Label(root, text="Select multiplier option:")
multiplier_label.pack()
for option in multiplier_options:
    rb = tk.Radiobutton(root, text=option, variable=multiplier_var, value=option)
    rb.pack()

# Create convert button
convert_button = tk.Button(root, text="Convert", command=convert_xml)
convert_button.pack()

# Create output text box
output_label = tk.Label(root, text="Output XML code:")
output_label.pack()
output_text = tk.Text(root, height=10, width=50)
output_text.pack()

root.mainloop()
