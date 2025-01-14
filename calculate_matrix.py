#!/usr/bin/env python3

from pymatgen.core import Structure
import numpy as np

def calculate_transformation_matrix():
    primitive_file_path = input("Enter the path to the primitive cell POSCAR file (e.g., primitive.vasp): ").strip()
    supercell_file_path = input("Enter the path to the supercell POSCAR file (e.g., supercell.vasp): ").strip()

    primitive_structure = Structure.from_file(primitive_file_path)
    supercell_structure = Structure.from_file(supercell_file_path)

    primitive_lattice = primitive_structure.lattice.matrix
    supercell_lattice = supercell_structure.lattice.matrix

    transformation_matrix = np.linalg.inv(primitive_lattice).dot(supercell_lattice)
    transformation_matrix = np.rint(transformation_matrix).astype(int)

    print("\nTransformation Matrix:")
    print(transformation_matrix)

if __name__ == "__main__":
    calculate_transformation_matrix()
