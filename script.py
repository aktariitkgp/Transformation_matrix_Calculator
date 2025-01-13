# Install pymatgen if not already installed
# pip install pymatgen

# Import required libraries
from pymatgen.core import Structure
import numpy as np

# Function to process files and compute the transformation matrix
def calculate_transformation_matrix():
    # Prompt the user to input the file paths
    primitive_file_path = input("Enter the path to the primitive cell POSCAR file (e.g., primitive.vasp): ").strip()
    supercell_file_path = input("Enter the path to the supercell POSCAR file (e.g., supercell.vasp): ").strip()

    # Load structures from the provided file paths
    primitive_structure = Structure.from_file(primitive_file_path)
    supercell_structure = Structure.from_file(supercell_file_path)

    # Extract the lattice matrices
    primitive_lattice = primitive_structure.lattice.matrix  # 3x3 matrix for primitive cell
    supercell_lattice = supercell_structure.lattice.matrix  # 3x3 matrix for supercell

    # Compute the transformation matrix
    transformation_matrix = np.linalg.inv(primitive_lattice).dot(supercell_lattice)
    transformation_matrix = np.rint(transformation_matrix).astype(int)  # Round for precision

    # Print the result
    print("\nTransformation Matrix:")
    print(transformation_matrix)

# Call the function
calculate_transformation_matrix()
