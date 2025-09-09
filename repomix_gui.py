import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import subprocess
from datetime import datetime

class RepomixGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Repomix Generator")
        self.root.geometry("850x550")
        self.root.minsize(750, 500)
        self.root.resizable(True, True)
        
        # Set uniform LIGHTER background color for whole window (like behind title originally)
        window_bg = "#e8e8e8"  # Lighter grey for entire window
        self.root.configure(bg=window_bg)
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure custom styles for uniform lighter background
        self.style.configure("Custom.TLabelframe", background=window_bg)
        self.style.configure("Custom.TLabelframe.Label", foreground="#333333")
        self.style.configure("Custom.TFrame", background=window_bg)
        
        # Custom colors
        self.accent_color = "#2E86C1"
        self.success_color = "#27AE60"
        self.error_color = "#E74C3C"
        self.button_green = "#4CAF50"  # Exact same green for both buttons
        
        self.selected_folder = ""
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="20", style="Custom.TFrame")
        main_frame.pack(fill="both", expand=True)
        
        # Title with custom styling
        title_label = tk.Label(main_frame, text="🗂️ Repomix Generator", 
                              font=("Segoe UI", 24, "bold"),
                              fg=self.accent_color, bg="#e8e8e8")
        title_label.pack(pady=(0, 20))
        
        # Description
        desc_label = tk.Label(main_frame, 
                             text="Select a repository folder to generate a comprehensive text summary",
                             font=("Segoe UI", 11), fg="#555",
                             bg="#e8e8e8")
        desc_label.pack(pady=(0, 30))
        
        # Folder selection section
        folder_section = ttk.LabelFrame(main_frame, text="📁 Repository Selection", 
                                       padding="15", style="Custom.TLabelframe")
        folder_section.pack(fill="x", pady=(0, 20))
        
        self.folder_label = tk.Label(folder_section, text="No folder selected", 
                                   relief="solid", anchor="w", bg="white", 
                                   font=("Consolas", 10), fg="#666",
                                   padx=10, pady=8)
        self.folder_label.pack(fill="x", pady=(0, 10))
        
        # Browse button - EXACT same green and styled font as Generate button
        browse_btn = tk.Button(folder_section, text="Browse Folder",
                              command=self.browse_folder,
                              bg=self.button_green, fg="white",
                              font=("Segoe UI", 13, "bold"),  # Scaled down from Generate button
                              pady=8, padx=15,
                              relief="flat",
                              cursor="hand2")
        browse_btn.pack(pady=5)
        
        # Output preview section
        preview_section = ttk.LabelFrame(main_frame, text="📄 Output Preview", 
                                        padding="15", style="Custom.TLabelframe")
        preview_section.pack(fill="x", pady=(0, 20))
        
        self.output_label = tk.Label(preview_section, text="Select a folder to see output filename", 
                                   relief="solid", anchor="w", bg="#f8f9fa",
                                   font=("Consolas", 10), fg="#666",
                                   padx=10, pady=8)
        self.output_label.pack(fill="x")
        
        # Generate button - using exact same green as Browse button
        generate_btn = tk.Button(main_frame, text="🚀 Generate Repomix", 
                               command=self.run_repomix, 
                               bg=self.button_green, fg="white", 
                               font=("Segoe UI", 16, "bold"),
                               pady=15, relief="flat",
                               cursor="hand2")
        generate_btn.pack(pady=20, ipadx=20)
        
        # Status with icon
        self.status_label = tk.Label(main_frame, text="✅ Ready to generate repomix", 
                                   fg=self.success_color, font=("Segoe UI", 12),
                                   bg="#e8e8e8")
        self.status_label.pack(pady=(0, 15))
        
        # Console output with better styling
        console_section = ttk.LabelFrame(main_frame, text="📊 Process Output", 
                                        padding="10", style="Custom.TLabelframe")
        console_section.pack(fill="both", expand=True)
        
        # Console with scrollbar
        console_frame = tk.Frame(console_section, bg="#e8e8e8")
        console_frame.pack(fill="both", expand=True)
        
        self.console_text = tk.Text(console_frame, height=8, 
                                   font=("Consolas", 9),
                                   bg="#1e1e1e", fg="#00ff00",
                                   insertbackground="white")
        
        scrollbar = ttk.Scrollbar(console_frame, command=self.console_text.yview)
        self.console_text.config(yscrollcommand=scrollbar.set)
        
        self.console_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def browse_folder(self):
        folder_path = filedialog.askdirectory(title="Select Repository Folder")
        if folder_path:
            self.selected_folder = folder_path
            folder_name = os.path.basename(folder_path)
            self.folder_label.config(text=f"📁 {folder_name}\n📍 {folder_path}", 
                                   font=("Consolas", 10), fg="#333")
            
            # Update output preview
            timestamp = datetime.now().strftime('%m%d%y_%H%M')
            output_filename = f"{folder_name}-summary_{timestamp}.txt"
            self.output_label.config(text=f"📄 {output_filename}", 
                                   font=("Consolas", 10), fg="#333")
            
            self.status_label.config(text="✅ Folder selected - ready to generate!", 
                                   fg=self.success_color)
    
    def run_repomix(self):
        if not self.selected_folder:
            messagebox.showerror("Error", "Please select a folder first!")
            return
        
        try:
            folder_name = os.path.basename(self.selected_folder)
            timestamp = datetime.now().strftime('%m%d%y_%H%M')
            output_filename = f"{folder_name}-summary_{timestamp}.txt"
            
            self.status_label.config(text="⚡ Running Repomix...", fg="#FF8C00")
            self.console_text.delete(1.0, tk.END)
            self.console_text.insert(tk.END, f"🚀 Starting Repomix generation...\n")
            self.console_text.insert(tk.END, f"📁 Target folder: {folder_name}\n")
            self.console_text.insert(tk.END, f"📄 Output file: {output_filename}\n")
            self.console_text.insert(tk.END, f"{'='*50}\n\n")
            self.root.update()
            
            cmd = [
                "npx", "repomix", 
                "--output", output_filename,
                "--ignore", ".env,*.log"
            ]
            
            result = subprocess.run(
                cmd,
                cwd=self.selected_folder,
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='replace',
                shell=True
            )
            
            if result.stdout:
                self.console_text.insert(tk.END, "📊 Output:\n" + result.stdout + "\n")
            if result.stderr and result.returncode != 0:
                self.console_text.insert(tk.END, "⚠️ Errors:\n" + result.stderr + "\n")
            
            if result.returncode == 0:
                self.status_label.config(text="🎉 Success! Repomix file generated!", 
                                       fg=self.success_color)
                self.console_text.insert(tk.END, "\n✅ Generation complete!\n")
                
                messagebox.showinfo("Success! 🎉", 
                                  f"Repomix completed successfully!\n\n📄 File: {output_filename}\n📍 Location: {self.selected_folder}")
            else:
                self.status_label.config(text="❌ Error during generation", 
                                       fg=self.error_color)
                messagebox.showerror("Error ❌", f"Repomix failed.\n\nCheck output for details.")
            
            self.console_text.see(tk.END)
                
        except FileNotFoundError:
            error_msg = "npx or repomix not found. Make sure Node.js is installed."
            messagebox.showerror("Error ❌", error_msg)
            self.status_label.config(text="❌ npx/repomix not found", fg=self.error_color)
        except Exception as e:
            messagebox.showerror("Error ❌", f"An error occurred: {str(e)}")
            self.status_label.config(text="❌ Unexpected error", fg=self.error_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = RepomixGUI(root)
    root.mainloop()
