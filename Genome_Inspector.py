import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from Bio.Seq import Seq
from Bio.SeqUtils import seq3
from Bio.SeqUtils import nt_search 
from Bio.SeqUtils import MeltingTemp as mt

def count_base(dna_sequence):
    seq = Seq(dna_sequence)
    return len(seq)

def dna_to_rna(dna_sequence):
    seq = Seq(dna_sequence)
    rna_seq = seq.transcribe()
    return str(rna_seq)

def dna_complementary_sequence(dna_sequence):
    seq = Seq(dna_sequence)
    comp_seq = seq.complement()
    return str(comp_seq)

def dna_to_amino_acid(dna_sequence):
    seq = Seq(dna_sequence)
    aa_seq = seq.translate()
    return str(aa_seq)

def dna_aa_3letter(dna_sequence):
    seq = Seq(dna_sequence)
    aa_seq = seq.translate()
    seqn3 =  seq3(aa_seq)
    return str(seqn3)

def reverse_complement(dna_sequence):
    seq = Seq(dna_sequence)
    rev_comp_seq = seq.reverse_complement()
    return str(rev_comp_seq)

def gc_content(dna_sequence):
    seq = Seq(dna_sequence)
    seq_length = len(seq)
    if seq_length == 0:
        return 0
    gc_content = (seq.count("G") + seq.count("C")) / seq_length * 100
    return gc_content

def melting_temperature(dna_sequence):
    return mt.Tm_NN(dna_sequence)

def annealing_temperature(dna_sequence):
    tm = mt.Tm_NN(dna_sequence)
    return tm - 5  # Subtracting 5°C from the melting temperature for a basic approximation

def find_restriction_sites(dna_sequence, enzyme_site):
    sites = nt_search(dna_sequence, enzyme_site)
    return sites[1:]

def count_nucleotides(dna_sequence):
    return {
        'A': dna_sequence.count('A'),
        'T': dna_sequence.count('T'),
        'G': dna_sequence.count('G'),
        'C': dna_sequence.count('C')
    }

def find_orfs(dna_sequence):
    seq = Seq(dna_sequence)
    orfs = []
    for frame in range(3):
        for pro in seq[frame:].translate().split("*"):
            if len(pro) > 10:
                orfs.append(pro)
    return orfs

def translate_reading_frame(dna_sequence, frame):
    seq = Seq(dna_sequence)
    return str(seq[frame:].translate())

def select_option(option):
    # Hide the logo
    image_label.grid_forget()
    for button in option_buttons:
        button.grid_forget()
    button_quick_analysis.grid_forget()
    home_button.grid(row=0, column=3, pady=10, columnspan=3)
    input_label.grid(row=1, column=1, pady=(10, 5), columnspan=3)
    entry.grid(row=2, column=1, pady=(5, 10), columnspan=3)
    browse_file_button.grid(row=3, column=1, pady=(5, 10), columnspan=3)
    process_button.config(command=lambda: process_sequence(option))
    process_button.grid(row=4, column=1, pady=(10, 5), columnspan=3)
    result_text.grid(row=7, column=1, pady=(10, 5), columnspan=3, sticky="nsew")
    result_text.delete("1.0", tk.END)
    if option == "DNA to RNA":
        result_text.insert(tk.END, "DNA to RNA selected.")
    elif option == "DNA complement":
        result_text.insert(tk.END, "DNA complementary sequence selected.")
    elif option == "DNA to Amino acid":
        result_text.insert(tk.END, "DNA to Amino acid one letter code selected.")
    elif option == "GC content in sequence":
        result_text.insert(tk.END, "GC content in sequence selected.")
    elif option == "Melting Temperature":
        result_text.insert(tk.END, "Melting Temperature selected.")
    elif option == "Annealing Temperature":
        result_text.insert(tk.END, "Annealing Temperature selected.")
    elif option == "Reverse Complement":
        result_text.insert(tk.END, "Reverse Complement selected.")
    elif option == "Find Restriction Sites":
        restriction_site_entry.grid(row=5, column=2, pady=0, columnspan=1)
        restriction_site_label.grid(row=4, column=2, pady=0, columnspan=1)
        process_button.grid(row=6, column=1, pady=(10, 5), columnspan=3)
        result_text.grid(row=8, column=1, pady=(10, 5), columnspan=3, sticky="nsew")
       # restriction_site_label.pack(pady=(5, 5))  # Show restriction site label and entry
        #restriction_site_entry.pack(pady=(5, 5))
        result_text.insert(tk.END, "Find Restriction Sites selected.")
    elif option == "Count Nucleotide Frequencies":
        result_text.insert(tk.END, "Count Nucleotide Frequencies selected.")
    elif option == "Find ORFs":
        result_text.insert(tk.END, "Find ORFs selected.")
    elif option == "Translate Reading Frame":
        result_text.insert(tk.END, "Translate Reading Frame selected.")
    elif option == "Quick Analysis":
        result_text.insert(tk.END, "Quick Analysis selected.")

def process_sequence(option):
    if option == "Find Restriction Sites":
        save_button.grid(row=7, column=1, pady=(5, 10), columnspan=3)
    else:
        save_button.grid(row=5, column=1, pady=(5, 10), columnspan=3)
    sequence = entry.get().upper()
    if not set(sequence).issubset({'A', 'T', 'G', 'C'}):
        messagebox.showerror("Error", "Input sequence should contain only nucleotide characters (A/T/G/C) without any special characters or spaces.")
        return
    result_text.delete("1.0", tk.END)
    if option == "DNA to RNA":
        result_text.insert(tk.END, "DNA to RNA: {}\n".format(dna_to_rna(sequence)))
    elif option == "DNA complement":
        result_text.insert(tk.END, "DNA complementary sequence: {}\n".format(dna_complementary_sequence(sequence)))
    elif option == "DNA to Amino acid":
        result_text.insert(tk.END, "Amino acid one letter code: {}\n".format(dna_to_amino_acid(sequence)))
        result_text.insert(tk.END, "Amino acid 3 letter code: {}\n".format(dna_aa_3letter(sequence)))
    elif option == "GC content in sequence":
        result_text.insert(tk.END, "GC content in sequence: {:.2f}%\n".format(gc_content(sequence)))
    elif option == "Melting Temperature":
        result_text.insert(tk.END, "Melting Temperature: {:.2f}°C\n".format(melting_temperature(sequence)))
    elif option == "Annealing Temperature":
        result_text.insert(tk.END, "Annealing Temperature: {:.2f}°C\n".format(annealing_temperature(sequence)))
    elif option == "Reverse Complement":
        result_text.insert(tk.END, "Reverse Complement: {}\n".format(reverse_complement(sequence)))
    elif option == "Find Restriction Sites":
        enzyme_site = restriction_site_entry.get().upper()
        if not enzyme_site:
            messagebox.showerror("Error", "Please enter a restriction site.")
            return
        sites = find_restriction_sites(sequence, enzyme_site)
        result_text.insert(tk.END, "Restriction Sites for '{}': {}\n".format(enzyme_site, sites if sites else "None found"))

    elif option == "Count Nucleotide Frequencies":
        counts = count_nucleotides(sequence)
        result_text.insert(tk.END, "Nucleotide Frequencies: {}\n".format(counts))
    elif option == "Find ORFs":
        orfs = find_orfs(sequence)
        result_text.insert(tk.END, "ORFs: {}\n".format(orfs))
    elif option == "Translate Reading Frame":
        frame = 0  # Default to frame 0; you can add a UI element to select the frame
        result_text.insert(tk.END, "Translation (Frame {}): {}\n".format(frame, translate_reading_frame(sequence, frame)))
    elif option == "Quick Analysis":
        result_text.insert(tk.END, "Base count: {} bases\n".format(count_base(sequence)))
        result_text.insert(tk.END, "GC content in sequence: {:.2f}%\n".format(gc_content(sequence)))
        result_text.insert(tk.END, "Melting Temperature: {:.2f}°C\n".format(melting_temperature(sequence)))
        result_text.insert(tk.END, "Annealing Temperature: {:.2f}°C\n".format(annealing_temperature(sequence)))
        counts = count_nucleotides(sequence)
        result_text.insert(tk.END, "Nucleotide Frequencies: {}\n".format(counts))

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("FASTA files", "*.fasta;*.fa"), ("FASTQ files", "*.fastq"), ("Text files", "*.txt")])
    if not file_path:
        return
    try:
        with open(file_path, "r") as file:
            sequence = file.read().strip().upper()
            entry.delete(0, tk.END)
            entry.insert(0, sequence)
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")

def home():
    entry.delete(0, tk.END)
    # Show the logo again
    image_label.grid(row=0, column=1, pady=10, columnspan=3)
    for i, button in enumerate(option_buttons):
        row_num = i // 3 + 1
        col_num = i % 3 + 1
        button.grid(row=row_num, column=col_num, padx=5, pady=5, sticky="nsew")
    button_quick_analysis.grid(row=(len(options) // 3) + 2, column=2, columnspan=1, pady=(30, 0), sticky="nsew")
    input_label.grid_forget()
    entry.grid_forget()
    browse_file_button.grid_forget()
    process_button.grid_forget()
    restriction_site_label.grid_forget()
    restriction_site_entry.grid_forget()
    result_text.grid_forget()
    save_button.grid_forget()
    home_button.grid_forget()

def save_results():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not file_path:
        return
    try:
        with open(file_path, "w") as file:
            file.write(result_text.get("1.0", tk.END))
        messagebox.showinfo("Success", f"Results saved to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving file: {e}")


def on_enter(event):
    event.widget['bg'] = '#569cdf'

def on_leave(event):
    event.widget['bg'] = '#80bcf6'

def on_process_enter(event):
    event.widget['bg'] = '#33cf5b'

def on_process_leave(event):
    event.widget['bg'] = '#33e660'

def on_browse_enter(event):
    event.widget['bg'] = '#b6c3c5'

def on_browse_leave(event):
    event.widget['bg'] = '#d5dcdd'

def on_quick_analysis_enter(event):
    event.widget['bg'] = '#f7cd25'

def on_quick_analysis_leave(event):
    event.widget['bg'] = '#e6b800'

# Create GUI
root = tk.Tk()
root.title("Genome Inspector 1.0")
root.geometry("575x550")
root.configure(bg="#eef1ea")

# Customizing button style for option buttons
option_button_style = {
    "bg": "#80bcf6",
    "fg": "#1a1c1f",
    "width": 25,
    "height": 3,
    "bd": 0,
    "relief": "flat"
}

save_button_style = {
    "bg": "#d5dcdd",
    "fg": "#1a1c1f",
    "width": 10,
    "height": 1,
    "bd": 0,
    "relief": "flat"
}

# Customizing quick analysis button style for option buttons
quick_analysis_style = {
    "bg": "#e6b800",
    "fg": "#1a1c1f",
    "width": 20,
    "height": 2,
    "bd": 0,
    "relief": "flat"
}

# Customizing button style for Process buttons
process_button_style = {
    "bg": "#33e660",
    "fg": "#1a1c1f",
    "width": 15,
    "height": 2,
    "bd": 0,
    "relief": "flat"
}

# Customizing button style for Browse File button
browse_file_button_style = {
    "bg": "#d5dcdd",
    "fg": "#1a1c1f",
    "width": 10,
    "height": 1,
    "bd": 0,
    "relief": "flat"
}

# Customizing button style for Home button
home_button_style = {
    "bg": "#ff6666",
    "fg": "#1a1c1f",
    "width": 7,
    "height": 1,
    "bd": 0,
    "relief": "flat"
}

# Define the style for the Entry widget
entry_style = {
    'bg': '#fff',
    'fg': 'black',
    'insertbackground': 'red',
    'highlightthickness': 1,
    'highlightbackground': 'black',
    'highlightcolor': '#2f26c1',
    'width': 40
}

# Load and display the logo
logo_image = tk.PhotoImage(file="/etc/genome_inspector/assets/logo.png")  # Replace "logo.png" with the path to your logo image file
logo_label = tk.Label(root, text="Genome Inspector", font=("Helvetica", 24), bg="#eef1ea")

# Calculate the new dimensions
new_width = 160
new_height = 160

# Resize the image
resized_image = logo_image.subsample(logo_image.width() // new_width, logo_image.height() // new_height)

# Display the resized image using a label
image_label = tk.Label(root, image=resized_image)
image_label.grid(row=0, column=1, pady=10, columnspan=3)

# Option buttons
options = [
    "DNA to RNA", "DNA Complement", "DNA to Amino acid",
    "Translate Reading Frame", "Reverse Complement", "Find Restriction Sites",
    "Find ORFs", "Count Nucleotide Frequencies", "GC content in sequence",
    "Melting Temperature", "Annealing Temperature"
]

option_buttons = []
for i, option in enumerate(options):
    button = tk.Button(root, text=option, **option_button_style, command=lambda opt=option: select_option(opt))
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    row_num = i // 3 + 1
    col_num = i % 3 + 1
    button.grid(row=row_num, column=col_num, padx=5, pady=5, sticky="nsew")
    option_buttons.append(button)

# Quick analysis button
button_quick_analysis = tk.Button(root, text="Quick Analysis", command=lambda: select_option("Quick Analysis"), **quick_analysis_style)
button_quick_analysis.grid(row=(len(options) // 3) + 2, column=2, columnspan=1, pady=(30, 0), sticky="nsew")
button_quick_analysis.bind("<Enter>", on_quick_analysis_enter)
button_quick_analysis.bind("<Leave>", on_quick_analysis_leave)

# Entry for DNA sequence input
input_label = tk.Label(root, text="Enter DNA Sequence:", bg="#eef1ea", fg="#062a32", font=("Helvetica", 12))
entry = tk.Entry(root, **entry_style)

# Browse file button
browse_file_button = tk.Button(root, text="Browse File", command=browse_file, **browse_file_button_style)
browse_file_button.bind("<Enter>", on_browse_enter)
browse_file_button.bind("<Leave>", on_browse_leave)

restriction_site_label = tk.Label(root, text="Enter restriction site:", bg="#eef1ea")
restriction_site_entry = tk.Entry(root, width=20)

# Process button
process_button = tk.Button(root, text="Process", **process_button_style)
process_button.bind("<Enter>", on_process_enter)
process_button.bind("<Leave>", on_process_leave)

# Result display
result_text = tk.Text(root, height=25, width=72, bg="#fff")

# Home button
home_button = tk.Button(root, text="Home", command=home, **home_button_style)

save_button = tk.Button(root, text="Save Results", command=save_results, **save_button_style)
save_button.bind("<Enter>", on_browse_enter)
save_button.bind("<Leave>", on_browse_leave)

root.mainloop()
